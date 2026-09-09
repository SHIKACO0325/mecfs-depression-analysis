"""Revised internal evaluation. Run: python run_analysis.py --data path/to/Data.csv.
Uses raw inputs only. Outputs go to results/ next to this script.
"""
from pathlib import Path
import argparse, json, hashlib, platform, warnings
import numpy as np
import pandas as pd
import sklearn, scipy, joblib, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import StratifiedKFold, GridSearchCV
from sklearn.metrics import accuracy_score, f1_score, recall_score, confusion_matrix, classification_report
from sklearn.inspection import permutation_importance

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results';OUT.mkdir(exist_ok=True)
CAT=['gender','pem_present','work_status','social_activity_level','exercise_frequency','meditation_or_mindfulness']
LABELS=['Both','Depression','ME/CFS']
GRIDS={'LR':{'model__C':[0.01,0.1,1.,10.]},
 'DT':{'model__max_depth':[3,5,8,None],'model__min_samples_leaf':[2,5,10]},
 'RF':{'model__max_depth':[5,8,None],'model__min_samples_leaf':[2,5],'model__max_features':['sqrt',0.7]}}

def main(path):
 d=pd.read_csv(path);X=d.drop(columns='diagnosis');y=d.diagnosis
 num=[c for c in X if c not in CAT]
 assert len(num)==9 and len(CAT)==6 and not y.isna().any()
 assert set(y)==set(LABELS)
 # Freeze this specification before any evaluation.
 spec={'input_sha256':hashlib.sha256(Path(path).read_bytes()).hexdigest(),'outer_folds':5,'inner_folds':3,'outer_seed':42,'inner_seed':43,'model_seed':42,'primary_metric':'f1_macro','grids':GRIDS,'numeric_imputation':'median','categorical_imputation':'most_frequent','prior_data_inspection':True,'data_provenance':'unverified; possibly synthetic','no_post_result_grid_changes':True}
 (OUT/'protocol.json').write_text(json.dumps(spec,indent=2))
 env={'python':platform.python_version(),'numpy':np.__version__,'pandas':pd.__version__,'scipy':scipy.__version__,'scikit-learn':sklearn.__version__,'joblib':joblib.__version__,'matplotlib':matplotlib.__version__}
 (OUT/'environment.json').write_text(json.dumps(env,indent=2))
 (ROOT/'requirements.txt').write_text('\n'.join(f'{k}=={v}' for k,v in env.items() if k!='python')+'\n')
 audit={'shape':list(d.shape),'class_counts':y.value_counts().to_dict(),'missing':d.isna().sum().to_dict(),'rows_with_missing':int(X.isna().any(axis=1).sum()),'duplicate_rows':int(d.duplicated().sum()),'duplicate_predictor_rows':int(X.duplicated().sum()),'numeric_predictors':num,'categorical_predictors':CAT}
 (OUT/'data_audit.json').write_text(json.dumps(audit,indent=2))
 def pipe(name):
  prep=ColumnTransformer([('num',Pipeline([('impute',SimpleImputer(strategy='median')),('scale',StandardScaler())]),num),('cat',Pipeline([('impute',SimpleImputer(strategy='most_frequent')),('encode',OneHotEncoder(handle_unknown='ignore',sparse_output=False))]),CAT)])
  models={'LR':LogisticRegression(solver='lbfgs',C=1.,max_iter=5000,class_weight='balanced',random_state=42),'DT':DecisionTreeClassifier(criterion='gini',class_weight='balanced',random_state=42),'RF':RandomForestClassifier(n_estimators=200,class_weight='balanced',random_state=42,n_jobs=1)}
  return Pipeline([('prep',prep),('model',models[name])])
 folds=list(StratifiedKFold(5,shuffle=True,random_state=42).split(X,y))
 predrows=[];metrics=[];parameters=[];importances=[];logs=[]
 for fold,(train,test) in enumerate(folds,1):
  assert not set(train)&set(test)
  for name in ['LR','DT','RF','Majority']:
   with warnings.catch_warnings(record=True) as ww:
    warnings.simplefilter('always')
    if name=='Majority':
     model=DummyClassifier(strategy='most_frequent').fit(X.iloc[train],y.iloc[train])
    else:
     search=GridSearchCV(pipe(name),GRIDS[name],scoring='f1_macro',cv=StratifiedKFold(3,shuffle=True,random_state=43),n_jobs=2,refit=True,error_score='raise')
     search.fit(X.iloc[train],y.iloc[train]);model=search.best_estimator_
     parameters.append({'fold':fold,'model':name,'inner_macro_f1':search.best_score_,'parameters':search.best_params_})
     pd.DataFrame(search.cv_results_).to_csv(OUT/f'search_{name}_{fold}.csv',index=False)
     # Verify preprocessing statistics were learned from outer training rows only.
     np.testing.assert_allclose(model.named_steps['prep'].named_transformers_['num'].named_steps['impute'].statistics_,X.iloc[train][num].median().to_numpy())
     assert 'diagnosis' not in model.feature_names_in_
    pr=model.predict(X.iloc[test]);proba=model.predict_proba(X.iloc[test])
    tr=model.predict(X.iloc[train])
    metrics.append({'fold':fold,'model':name,'n_train':len(train),'n_test':len(test),'accuracy':accuracy_score(y.iloc[test],pr),'macro_f1':f1_score(y.iloc[test],pr,average='macro'),'macro_recall':recall_score(y.iloc[test],pr,average='macro'),'both_recall':recall_score(y.iloc[test],pr,labels=['Both'],average=None)[0],'train_macro_f1':f1_score(y.iloc[train],tr,average='macro')})
    for i,row in enumerate(test):
     r={'row_index':int(row),'fold':fold,'model':name,'label':y.iloc[row],'prediction':pr[i]}
     r.update({f'prob_{c}':float(proba[i,list(model.classes_).index(c)]) for c in LABELS});predrows.append(r)
    if name=='RF':
     imp=permutation_importance(model,X.iloc[test],y.iloc[test],scoring='f1_macro',n_repeats=10,random_state=100+fold,n_jobs=2)
     for j,c in enumerate(X):
      for rep,val in enumerate(imp.importances[j]):importances.append({'fold':fold,'feature':c,'repeat':rep+1,'macro_f1_decrease':float(val)})
    logs += [{'fold':fold,'model':name,'warning':str(w.message),'category':w.category.__name__} for w in ww]
   print('completed',fold,name,metrics[-1],flush=True)
 p=pd.DataFrame(predrows);m=pd.DataFrame(metrics)
 assert all(len(g)==len(d) and g.row_index.nunique()==len(d) for _,g in p.groupby('model'))
 assert np.allclose(p[['prob_'+c for c in LABELS]].sum(axis=1),1)
 p.to_csv(OUT/'oof_predictions.csv',index=False);m.to_csv(OUT/'fold_metrics.csv',index=False)
 (OUT/'selected_parameters.json').write_text(json.dumps(parameters,indent=2));(OUT/'warnings.json').write_text(json.dumps(logs,indent=2))
 summary={}
 for name,g in p.groupby('model',sort=False):
  report=classification_report(g.label,g.prediction,labels=LABELS,output_dict=True,zero_division=0)
  cm=confusion_matrix(g.label,g.prediction,labels=LABELS)
  mm=m[m.model==name]
  summary[name]={'pooled_accuracy':accuracy_score(g.label,g.prediction),'pooled_macro_f1':f1_score(g.label,g.prediction,average='macro'),'pooled_macro_recall':recall_score(g.label,g.prediction,average='macro'),'classification_report':report,'confusion_matrix':cm.tolist(),'fold_mean':mm.select_dtypes('number').mean().to_dict(),'fold_sd':mm.select_dtypes('number').std(ddof=1).to_dict()}
  assert int(np.trace(cm))==int((g.label==g.prediction).sum())
 (OUT/'summary.json').write_text(json.dumps(summary,indent=2))
 imp=pd.DataFrame(importances);imp.to_csv(OUT/'permutation_importance.csv',index=False)
 fi=imp.groupby(['feature','fold']).macro_f1_decrease.mean().groupby('feature').agg(['mean','std']).sort_values('mean',ascending=False)
 fi.to_csv(OUT/'importance_summary.csv')
 # Descriptive figures use observed raw values, never full-data imputation.
 plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
 def save(n):
  plt.tight_layout();plt.savefig(OUT/f'figure_{n:02}.png',dpi=200,bbox_inches='tight');plt.close()
 fig,ax=plt.subplots(figsize=(6,3));counts=y.value_counts().reindex(LABELS);ax.bar(LABELS,counts,color=['#a2b8c5','#d5ad78','#739b85']);ax.set_ylabel('Records')
 for i,v in enumerate(counts):ax.text(i,v+8,str(v),ha='center')
 ax.set_ylim(0,730);save(1)
 fig,axes=plt.subplots(2,2,figsize=(8,5))
 for ax,c,title in zip(axes.flat,['fatigue_severity_scale_score','depression_phq9_score','sleep_quality_index','brain_fog_level'],['Fatigue field','PHQ-9 field','Sleep quality field','Brain fog field']):
  vals=[X.loc[y==categ,c].dropna() for categ in LABELS];ax.boxplot(vals,tick_labels=LABELS);ax.set_title(title);ax.set_ylabel('Recorded value')
 save(2)
 corr=X[num].corr(method='spearman');corr.to_csv(OUT/'raw_spearman.csv')
 fig,ax=plt.subplots(figsize=(8,6));im=ax.imshow(corr,vmin=-1,vmax=1,cmap='RdBu_r');short=['Age','Sleep quality','Brain fog','Pain','Stress','PHQ-9','Fatigue','PEM duration','Sleep hours'];ax.set_xticks(range(9),short,rotation=45,ha='right');ax.set_yticks(range(9),short)
 for i in range(9):
  for j in range(9):ax.text(j,i,f'{corr.iloc[i,j]:.2f}',ha='center',va='center',fontsize=7,color='white' if abs(corr.iloc[i,j])>.5 else 'black')
 fig.colorbar(im,ax=ax,label='Spearman correlation');save(3)
 fig,ax=plt.subplots(figsize=(8,4));names=['LR','DT','RF'];x=np.arange(3)
 for k,(metric,col) in enumerate(zip(['accuracy','macro_f1','macro_recall'],['#7299b2','#c8a26c','#82a388'])):
  means=[summary[n]['fold_mean'][metric] for n in names];sd=[summary[n]['fold_sd'][metric] for n in names]
  ax.bar(x+(k-1)*.25,means,width=.25,yerr=sd,capsize=3,label=metric.replace('_',' '),color=col)
  for xx,v,s in zip(x+(k-1)*.25,means,sd):ax.text(xx,v+s+.016,f'{v:.3f}',ha='center',fontsize=8)
 ax.set_xticks(x,['Logistic regression','Decision tree','Random forest']);ax.set_ylim(0,1);ax.set_ylabel('Outer-fold mean ± SD');ax.legend(loc='lower right');save(4)
 fig,axes=plt.subplots(1,3,figsize=(11,3.5))
 for ax,name in zip(axes,names):
  cm=np.array(summary[name]['confusion_matrix']);pct=cm/cm.sum(axis=1)[:,None]*100;ax.imshow(pct,cmap='Blues',vmin=0,vmax=100)
  for i in range(3):
   for j in range(3):ax.text(j,i,f'{cm[i,j]}\n({pct[i,j]:.1f}%)',ha='center',va='center',fontsize=8,color='white' if pct[i,j]>65 else 'black')
  ax.set_xticks(range(3),LABELS,rotation=25);ax.set_yticks(range(3),LABELS);ax.set_title(name);ax.set_xlabel('Predicted label')
 axes[0].set_ylabel('Recorded label');save(5)
 fig,ax=plt.subplots(figsize=(8,5));plot=fi.head(10).iloc[::-1];ax.barh(plot.index,plot['mean'],xerr=plot['std'],color='#7299b2',capsize=3);ax.set_xlabel('Macro F1 decrease after permutation (mean ± fold SD)');save(6)
 print(json.dumps({k:{a:v for a,v in z.items() if a.startswith('pooled')} for k,z in summary.items()},indent=2),flush=True)
 print('DONE',flush=True)

if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--data',required=True);main(a.parse_args().data)

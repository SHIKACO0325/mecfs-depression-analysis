## Title/Abstract — paragraph 0

Before:
Machine Learning Classification of ME/CFS, Depression, and Combined Labels: A Secondary Analysis of Instructor-Provided Synthetic Data

After:
Machine Learning Classification of ME/CFS Depression and Combined Labels in an Instructor Provided Dataset

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## Title/Abstract — paragraph 3

Before:
本轮标记说明（2026-09-09）：以你此次上传的稿件为基准，淡蓝底标出本轮改写段落，黄色标出仍需补充的信息。旧轮高亮已清除，非Word原生修订追踪。原图和表内数值保留。文末附导师意见处理说明，投稿时移除。本轮为文字修订，尚未完成无泄漏重分析。

After:


Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## Title/Abstract — paragraph 5

Before:
Overlapping symptom profiles in myalgic encephalomyelitis/chronic fatigue syndrome (ME/CFS) and depression motivate research on symptom-based classification. This exploratory secondary analysis compared logistic regression, a decision tree, and a random forest using an instructor-provided synthetic dataset containing 1,620 records, 15 predictors, and three labels: ME/CFS, Depression, and Both. The original analysis used iterative numerical imputation, categorical mode imputation, one-hot encoding, standardization, an 80:20 stratified split, and ten-fold stratified hyperparameter searches. At the two-decimal precision shown in Figure 4, decision tree and random forest had the same accuracy, macro F1, and macro recall values of 0.82, 0.81, and 0.81, respectively; logistic regression had corresponding values of 0.80. The saved outputs showed higher Both recall for logistic regression (0.790) than for decision tree (0.728) or random forest (0.667). These descriptive differences do not establish model superiority: diagnosis-assisted imputation before splitting and preprocessing outside cross-validation folds compromised the evaluation. A corrected analysis is required before finalizing comparative performance claims. The results concern synthetic-label classification and do not establish clinical diagnostic validity. [需要作者补充：完成无泄漏重分析后，统一更新摘要中的流程、数值和结论。]

After:
Overlapping symptom profiles in myalgic encephalomyelitis/chronic fatigue syndrome (ME/CFS) and depression motivate investigation of symptom-based classification. This exploratory secondary analysis compared logistic regression, a decision tree, and a random forest using 1,620 instructor-provided records with 15 predictors and three recorded labels: ME/CFS, Depression, and Both. The dataset may be synthetic, but its origin and label-generation process have not been independently verified. A revised five-fold outer and three-fold inner stratified cross-validation procedure fitted imputation, encoding, and scaling within each training partition and selected hyperparameters using macro F1. Outer-fold mean accuracies were 0.778, 0.802, and 0.811 for logistic regression, decision tree, and random forest, respectively; corresponding macro F1 values were 0.773, 0.785, and 0.799. Both recall was highest for logistic regression (0.743), compared with decision tree (0.578) and random forest (0.659). Random forest had the highest mean aggregate scores, but the results do not establish statistically significant superiority. Permutation analyses identified PHQ-9, PEM presence, and fatigue fields as the largest contributors to random forest macro F1. These findings describe recorded-label prediction within the supplied dataset. Prior inspection of these data, uncertain provenance, and the absence of independent clinical validation preclude claims of clinical diagnostic validity.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## Title/Abstract — paragraph 6

Before:
Keywords: ME/CFS; depression; synthetic data; secondary analysis; multiclass classification; machine learning

After:
Keywords: ME/CFS; depression; secondary analysis; multiclass classification; nested cross-validation; machine learning

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 1 Introduction — paragraph 9

Before:
The interpretation of symptom-related predictors depends on the data source and outcome definitions. Although the PHQ-9 measures depressive symptom severity [3], a synthetic field named depression_phq9_score does not establish that a questionnaire was administered to patients. Likewise, a PEM field does not establish a clinical ME/CFS diagnosis. The label-generation rules are therefore essential for determining whether a classifier learns imposed synthetic relationships or patterns that might warrant subsequent clinical investigation.

After:
The interpretation of symptom-related predictors depends on the data source and outcome definitions. Although the PHQ-9 measures depressive symptom severity [3], the presence of a field named depression_phq9_score does not establish that a questionnaire was administered to patients. Similarly, a PEM field does not establish a clinical ME/CFS diagnosis. Without documentation of label construction, classification may reflect imposed relationships among recorded variables rather than clinically validated differences.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 1 Introduction — paragraph 10

Before:
The present study examines three questions using instructor-provided synthetic data: how logistic regression, decision tree, and random forest compare on aggregate classification metrics; whether their relative performance differs for the Both label; and which predictors receive the largest random forest importance scores. The analysis concerns the recorded ME/CFS, Depression, and Both labels within this dataset.

After:
The present study examines three questions using an instructor-provided dataset: how logistic regression, decision tree, and random forest compare on aggregate classification metrics; whether their relative performance differs for the Both label; and which predictors contribute most to random forest performance under permutation. The analysis concerns the recorded labels ME/CFS, Depression, and Both. The dataset is considered potentially synthetic, with its provenance unresolved.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 1 Introduction — paragraph 11

Before:
The contribution is an exploratory comparison of established classifiers that examines aggregate performance together with class-specific errors. The original outputs illustrate a difference in model ranking between overall accuracy and Both recall, but this observation remains provisional because of preprocessing leakage. The study introduces no new algorithm and provides no clinical validation. Its value depends on transparent reporting of the synthetic-data setting, the analysis workflow, and the limitations of the available results.

After:
The contribution is an exploratory comparison of established classifiers under a common, explicitly documented internal evaluation procedure. Aggregate metrics are considered alongside class-specific errors and validation-based feature importance. The analysis illustrates how a model with higher overall accuracy can have lower recall for one label. It introduces no new algorithm and does not validate a clinical diagnostic tool.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 2 Related Work — paragraph 14

Before:
Hawk et al. [9] examined chronic fatigue syndrome, major depressive disorder, and controls, whereas the present study uses synthetic records labeled ME/CFS, Depression, and Both. The present analysis also compares logistic regression, decision tree, and random forest rather than discriminant function analysis. Its scope is an exploratory comparison of classification methods and class-specific error patterns within a supplied synthetic dataset. Differences in data origin, variable definitions, label construction, and evaluation design prevent direct comparison of accuracy with the clinical study. The inclusion of Both changes the classification task but does not establish methodological novelty or clinical superiority.

After:
Hawk et al. [9] examined clinically defined chronic fatigue syndrome, major depressive disorder, and control groups, whereas the present analysis concerns recorded ME/CFS, Depression, and Both labels in a dataset of unverified provenance. It compares logistic regression, decision tree, and random forest using nested internal cross-validation. Differences in data origin, class composition, variable definitions, and evaluation design prevent direct comparison of accuracy across studies. The inclusion of Both changes the classification task but does not establish methodological novelty or clinical superiority.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 2 Related Work — paragraph 16

Before:
TRIPOD and TRIPOD+AI emphasize transparent reporting of prediction-model development and evaluation [8, 10]. Relevant reporting principles include documenting data provenance, outcome definitions, preprocessing, model selection, and performance estimation. Here, they guide description of the analysis; adherence to reporting principles would not establish the clinical validity of models evaluated on synthetic data.

After:
TRIPOD and TRIPOD+AI emphasize transparent reporting of prediction-model development and evaluation [8, 10]. Relevant reporting principles include documenting data provenance, outcome definitions, preprocessing, model selection, and performance estimation. These principles guide the present description, while the lack of a verified clinical reference standard limits interpretation to recorded-label prediction.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 3.1 Study design and data source — paragraph 19

Before:
This exploratory study conducted a secondary analysis of a synthetic dataset provided by an instructor, as reported by the author. No participants were recruited and no new clinical examinations or questionnaires were conducted for this study. The records are analyzed as synthetic observations with assigned labels, rather than verified patient records. [需要作者补充：填写原数据提供者的适当署名、获得数据的时间，以及合成性质的来源说明；不得将指导教师同意表述写成原提供者已经确认具体生成过程。]

After:
This study conducted an exploratory secondary analysis of a dataset that the author reports receiving from a former course instructor associated with a Coursera course. The provider identity, date of receipt, and original generation or collection procedure could not be confirmed. The author believes the data may have been artificially generated, but has not obtained confirmation from the original provider. Accordingly, the dataset is described as potentially synthetic and is not presented as verified patient data or an official Coursera dataset. No participants were recruited and no new clinical examinations or questionnaires were conducted for this analysis.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 3.1 Study design and data source — paragraph 20

Before:
The analysis used two supplied files: the raw file Data.csv and the completed file multiple_imputed.csv. Each file contains 1,620 records and 16 columns, including 15 predictor variables and one outcome field, diagnosis. The two files have the same column order and recorded outcome labels. A row-wise comparison identified no changes to originally observed values, and neither file contains exact duplicate rows. These checks establish correspondence between the supplied files, but they do not establish that the records represent statistically independent synthetic observations or that the variables reproduce clinical measurements.

After:
The revised analysis used Data.csv, containing 1,620 rows and 16 columns: 15 predictors and the outcome field diagnosis. The previously completed file multiple_imputed.csv was retained for historical documentation but was not used to train or evaluate the revised models. Both files have the same column order and outcome labels; comparison found no changes to originally observed values. No exact duplicate rows or duplicate predictor rows were identified in the raw file. These checks do not establish independence of the underlying records.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 3.1 Study design and data source — paragraph 21

Before:
The cleaning and evaluation notebooks use the names group_30.csv and group_30_multiple_imputed.csv. Their reported record and missing-value counts agree with the supplied files. This supports, but does not prove, the presumed correspondence between each notebook filename and its supplied CSV counterpart. The cleaning notebook computes imputed values but does not visibly export them before loading the completed CSV; therefore, the generation history of multiple_imputed.csv cannot be established from the saved notebook alone. [需要作者补充：确认两组文件名的对应关系，以及完成CSV的实际导出步骤。]

After:
The author confirmed that Data.csv and multiple_imputed.csv correspond to the notebook filenames group_30.csv and group_30_multiple_imputed.csv, respectively, and that the completed file was generated by executing code. The original execution environment was Jupyter Notebook. The present reanalysis bypassed that completed file and directly fitted all preprocessing from the raw missing-value data within the relevant training partitions.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 3.1 Study design and data source — paragraph 22

Before:
The supplied materials do not identify a formal dataset title, DOI, or accompanying dataset publication. The files available for analysis contain 1,620 records; documentation establishing the originally generated record count or any earlier exclusions was not supplied. The generation procedure and label-assignment rules remain unavailable in the materials reviewed. These limitations concern the documentation available for this analysis, not proof that such documentation does not exist.

After:
No accompanying dataset publication, formal dataset title, data dictionary, or documented sampling frame was available for this analysis. The supplied file contains 1,620 records, all of which were retained. Earlier exclusions, repeated observations, geographic coverage, and any relationship to real patient data remain unknown. Neither the label-assignment rules nor a data-generation script was available.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 3.1 Study design and data source — paragraph 23

Before:
The three assigned labels are ME/CFS, Depression, and Both. They are retained as supplied and treated as classification targets. In particular, Both is not evidence of independently confirmed clinical comorbidity. [需要作者补充：如可获得，请提供标签生成规则，尤其说明标签是否由输入症状字段或预设阈值决定；若未获得规则，应在局限性中保留这一事实。]

After:
The labels ME/CFS, Depression, and Both were retained as supplied. Both was treated as one distinct multiclass outcome, not as evidence of independently confirmed comorbidity. Unknown label-generation rules are a substantive limitation: the labels could have been assigned using the same symptom-related fields that serve as predictors.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 3.1 Study design and data source — paragraph 24

Before:
The author reports archiving the analysis materials at https://github.com/SHIKACO0325/mecfs-depression-analysis. This repository is an archive of the study materials, not the original source of the dataset.

After:
The original analysis materials are publicly archived at https://github.com/SHIKACO0325/mecfs-depression-analysis. The repository is a study-material archive and does not establish the original source or nature of the data. The downloaded raw CSV and the locally supplied CSV were identical in parsed values, despite differing file bytes. The revised analysis package records the SHA-256 of the exact local input used.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 3.1 Study design and data source — paragraph 25

Before:
The reported archive includes the two CSV files, original notebooks, three saved models, and six historical figures. [需要作者补充：确认最终仓库访问状态、分享许可及论文对应的完整commit或release编号。归档历史材料不等于已提供修正后的可复现分析。]

After:
The revised package contains the executable analysis script, an optional Jupyter entry notebook, frozen package versions, the analysis specification, per-fold search results and selected parameters, out-of-fold predictions and probabilities, and regenerated figures. [需要作者补充：将本次修订代码和结果上传到仓库后填写对应的完整commit或release编号；当前公开仓库链接不代表本次修订包已经发布。]

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 3.2 Outcome labels and predictor definitions — paragraph 27

Before:
The outcome field contains ME/CFS, Depression, and Both. For model fitting, LabelEncoder was fitted on the training labels, with Both = 0, Depression = 1, and ME/CFS = 2. Both is treated as a distinct output class, not as two simultaneous binary predictions.

After:
The outcome labels were passed directly to the scikit-learn classifiers as strings. The reporting order was Both, Depression, and ME/CFS. Each record received one predicted class, determined by the fitted classifier’s predict method, and probabilities for all three labels. No manual class-specific threshold tuning was performed.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 3.2 Outcome labels and predictor definitions — paragraph 28

Before:
The nine numerical predictors were age, sleep_quality_index, brain_fog_level, physical_pain_score, stress_level, depression_phq9_score, fatigue_severity_scale_score, pem_duration_hours, and hours_of_sleep_per_night. The six categorical predictors were gender, pem_present, work_status, social_activity_level, exercise_frequency, and meditation_or_mindfulness. All 15 predictors were retained; no automated feature-selection step appears in the supplied modeling code.

After:
The nine numerical predictors were age, sleep_quality_index, brain_fog_level, physical_pain_score, stress_level, depression_phq9_score, fatigue_severity_scale_score, pem_duration_hours, and hours_of_sleep_per_night. The six categorical predictors were gender, pem_present, work_status, social_activity_level, exercise_frequency, and meditation_or_mindfulness. All 15 predictors were retained; no automated feature-selection step was applied in the revised analysis.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 3.2 Outcome labels and predictor definitions — paragraph 29

Before:
Observed values in Data.csv ranged from 18 to 70 for age, 2 to 26 for depression_phq9_score, 2 to 10 for fatigue_severity_scale_score, 0 to 50 for pem_duration_hours, and 0 to 10 for hours_of_sleep_per_night. The sleep-quality, brain-fog, pain, and stress fields ranged from 1 to 10. These are observed data ranges, not verified instrument ranges. Four records report zero hours of sleep. Among records with observed PEM fields, 602 have pem_present = 0 with a positive duration, and 16 have pem_present = 1 with zero duration. These combinations require clarification of the synthetic coding conventions and generation rules, not automatic recoding. 

After:
Observed values in Data.csv ranged from 18 to 70 for age, 2 to 26 for depression_phq9_score, 2 to 10 for fatigue_severity_scale_score, 0 to 50 for pem_duration_hours, and 0 to 10 for hours_of_sleep_per_night. The sleep-quality, brain-fog, pain, and stress fields ranged from 1 to 10. These are observed data ranges, not verified instrument ranges. Four records report zero hours of sleep. Among records with observed PEM fields, 602 have pem_present = 0 with a positive duration, and 16 have pem_present = 1 with zero duration. These combinations require clarification of the coding conventions and generation or collection rules, not automatic recoding. 

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 3.3 Data preparation and feature handling — paragraph 31

Before:
Data.csv contains 333 missing cells across 13 predictors, affecting 302 of 1,620 records (18.6%). Missing counts ranged from 23 to 28 per affected predictor (1.42%–1.73%); age, gender, and diagnosis had no missing values. The completed CSV contains no missing values. The cleaning notebook includes a duplicate-removal command and visual distribution checks, but no reproducible outlier threshold or explicit outlier-removal rule.

After:
The raw file contains 333 missing cells across 13 predictors, affecting 302 of 1,620 records (18.6%). Missing counts ranged from 23 to 28 per affected predictor; age, gender, and diagnosis had no missing values. All 1,620 records and all 15 predictors were retained. No outlier removal, resampling, or undocumented value recoding was applied.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 3.3 Data preparation and feature handling — paragraph 32

Before:
The supplied cleaning code used IterativeImputer with a RandomForestRegressor (100 trees, maximum depth 10, random_state = 42), maximum 20 iterations, tolerance 0.01, and median initialization. The imputation matrix contained nine numerical predictors, encoded gender, and an encoded diagnosis variable. The imputer was fitted to all 1,620 records before the modeling notebook created the train–test split. The saved iteration log reached 20 iterations; its final change (1.6369) exceeded the displayed stopping threshold (0.7), so convergence was not demonstrated. No posterior sampling or pooling across multiple completed datasets was implemented. Accordingly, this was a single iterative-imputation workflow, despite the filename multiple_imputed.csv [7].

After:
Numerical predictors were imputed using training-partition medians and standardized using training-partition means and standard deviations. Categorical predictors, including pem_present, were imputed using training-partition modes and one-hot encoded with handle_unknown="ignore" and all observed training categories retained. ColumnTransformer combined the numerical and categorical transformations, and Pipeline joined preprocessing to the classifier. No outcome field was included in the preprocessing inputs.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 3.3 Data preparation and feature handling — paragraph 33

Before:
Categorical gaps were filled with full-sample modes: pem_present = 1.0, work_status = Not working, social_activity_level = Very High, exercise_frequency = Sometimes, and meditation_or_mindfulness = Yes. In the evaluation notebook, a ColumnTransformer fitted six categorical predictors with OneHotEncoder on the training subset and passed numerical predictors through. This produced 28 columns. StandardScaler was then fitted on those training columns and applied to the test subset for all three models. Encoding retained all categories; the code did not specify handling for unseen categories.

After:
Simple median and mode imputation was chosen for the revised analysis to provide a transparent, reproducible treatment of the modest missingness without adding an imputation-model search. This replaces the historical outcome-assisted iterative imputation and is not multiple imputation [7]. It does not propagate missing-value uncertainty, and alternative imputation methods were not compared. Preprocessing was refitted separately within every inner-training split and then on each full outer-training partition before evaluation on its held-out fold.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 3.3 Data preparation and feature handling — paragraph 34

Before:
The supplied cleaning code included diagnosis when imputing predictor values and fitted the imputer before data splitting. If the completed CSV used for evaluation was generated by this procedure, outcome information entered inputs for records later allocated to the test subset. This constitutes target-information leakage and compromises train–test separation. The exact CSV export chain remains to be confirmed (Section 3.1); the documented workflow nevertheless cannot establish a leakage-controlled evaluation. Encoding and scaling were fitted on the training subset once before the hyperparameter searches, rather than separately within each cross-validation fold. [需要作者补充：从Data.csv重新分析，移除预测输入插补中的diagnosis，并将插补、编码和标准化置于各训练折内拟合；提供实际运行记录和新结果。]

After:
The historical workflow used diagnosis-assisted imputation before data splitting and performed encoding and scaling outside the tuning folds. Those operations could transmit held-out information into model development. The revised pipelines correct these identified operations. However, they cannot reverse earlier inspection of the dataset or resolve unknown dependencies between records. The revised results therefore constitute retrospective internal re-evaluation, not validation on a newly collected independent sample.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 3.4 Models and class weighting — paragraph 36

Before:
The supplied evaluation notebook compared LogisticRegression, DecisionTreeClassifier, and RandomForestClassifier with random_state = 42. Training class counts were 324 Both, 454 Depression, and 518 ME/CFS. The balanced-weight calculation produced weights of approximately 1.3333, 0.9515, and 0.8340 in that order. Logistic regression and decision tree used class_weight = balanced; the selected random forest used balanced_subsample. No over-sampling or under-sampling step is present.

After:
The models were LogisticRegression, DecisionTreeClassifier, and RandomForestClassifier [4, 5], with random_state=42 and class_weight="balanced" for each classifier. Class weights were recomputed from the labels passed to each fitting operation; no full-dataset class weights were supplied. A most-frequent-class DummyClassifier was evaluated on the same outer folds as a reference baseline. There was no over-sampling or under-sampling.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 3.4 Models and class weighting — paragraph 37

Before:
The saved logistic-regression selection was C = 0.1, L2 regularization, solver = lbfgs, max_iter = 500, and tol = 0.001. The selected decision tree used entropy, max_depth = 5, min_samples_split = 5, and min_samples_leaf = 8. The selected random forest used 200 trees, max_depth = 8, min_samples_split = 5, min_samples_leaf = 2, max_features = 0.7, bootstrap = True, and class_weight = balanced_subsample. Class weighting does not itself establish adequate performance in every class.

After:
Logistic regression used the lbfgs solver, L2 regularization, max_iter=5000, and the default tolerance of 0.0001. Decision tree used the Gini criterion and default min_samples_split=2. Random forest used 200 trees, bootstrap=True, the Gini criterion, min_samples_split=2, and one worker per fitted forest. Parameters not included in the search retained the scikit-learn 1.8.0 defaults. There was no single global best parameter set for the reported evaluation: hyperparameters were selected independently in each outer fold and are supplied in selected_parameters.json.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 3.5 Hyperparameter search and evaluation design — paragraph 39

Before:
The supplied completed data were split using train_test_split with test_size = 0.2, random_state = 42, and stratification by diagnosis. The 1,296-record training subset comprised 324 Both, 454 Depression, and 518 ME/CFS records; the 324-record test subset comprised 81, 113, and 130 records, respectively. The same split was used for all three models. This is a nominal holdout split, not a leakage-free evaluation, because imputation preceded it.

After:
The revised specification was fixed before executing the new evaluation, after inspection of the historical results; it was not prospectively registered. StratifiedKFold with five outer folds, shuffle=True, and random_state=42 created five common evaluation partitions for all models. Each outer iteration used 1,296 training records and 324 held-out records. Across the five iterations, each of the 1,620 records received exactly one out-of-fold prediction per model. Row-level partition assignments are supplied with the predictions. No grouping or temporal splitting was possible because such identifiers were unavailable.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 3.5 Hyperparameter search and evaluation design — paragraph 40

Before:
Hyperparameter search used StratifiedKFold with 10 folds, shuffle = True, and random_state = 42 on the preprocessed training subset. Logistic regression used grid search over C = {0.01, 0.1, 0.5, 1, 2, 5}, solver = {lbfgs, saga}, max_iter = {500, 1000}, and tol = {0.0001, 0.001, 0.01}, with L2 and balanced weights fixed: 72 combinations. Decision tree used 30 randomized candidates from max_depth = {3, 5, 7, 10, 15, 20, None}, min_samples_split = {2, 5, 10, 20}, min_samples_leaf = {1, 2, 4, 8}, and criterion = {gini, entropy}. Both searches optimized weighted F1.

After:
Within each outer-training partition, three-fold stratified GridSearchCV with shuffle=True and random_state=43 selected hyperparameters using macro F1 for all three models. Logistic regression evaluated C in {0.01, 0.1, 1, 10}, giving four candidates. Decision tree evaluated max_depth in {3, 5, 8, None} and min_samples_leaf in {2, 5, 10}, giving 12 candidates. Random forest evaluated max_depth in {5, 8, None}, min_samples_leaf in {2, 5}, and max_features in {sqrt, 0.7}, giving 12 candidates.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 3.5 Hyperparameter search and evaluation design — paragraph 41

Before:
Random forest used 50 randomized candidates from n_estimators = {100, 150, 200}, max_depth = {5, 8, 10, 12, 15}, min_samples_split = {5, 10, 15}, min_samples_leaf = {2, 4, 6}, max_features = {sqrt, 0.5, 0.7}, and class_weight = {balanced, balanced_subsample}, with bootstrap = True. Unlike the other searches, it optimized weighted one-versus-rest ROC AUC. This difference must be considered when comparing the selected models; the searches did not optimize one common criterion.

After:
Each search refitted the selected pipeline on the complete outer-training partition before generating held-out predictions. The candidate grids and scoring criterion were not changed after examining the revised results. Nested evaluation separates parameter selection from outer-fold scoring [6]; it does not establish independence from the earlier research process or from unknown dependencies in the source data. The limited grids are a documented modeling choice rather than an exhaustive search for each model’s maximum attainable performance.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 3.5 Hyperparameter search and evaluation design — paragraph 42

Before:
After selection, cross_val_score reused the same ten-fold configuration to calculate weighted F1 for the selected estimators. These are non-nested, post-selection scores, not independent estimates from an outer cross-validation loop. Final test predictions were generated after fitting the selected estimators on the full training subset. The notebook also inspected test performance before and after tuning, so the test subset was viewed more than once; whether this influenced subsequent decisions requires author confirmation. [需要作者补充：确认测试集结果是否影响后续模型选择；提供完整环境版本。重分析前应确定共同调参指标与评估方案，并披露旧测试集已被查看。]

After:
The new analysis ran using Python 3.12.14, scikit-learn 1.8.0, NumPy 2.3.5, pandas 2.2.3, SciPy 1.17.0, joblib 1.5.3, and Matplotlib 3.10.8. The supplied script and requirements.txt specify the runnable environment; the optional notebook invokes the same script. The run completed without warnings recorded by the analysis process. No original serialized model was loaded to generate the new results.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 3.6 Performance measures and descriptive analyses — paragraph 44

Before:
Figure 4 and Table 1 report accuracy, macro F1-score, and macro recall calculated from the selected models’ predictions on the 324-record test subset, rather than cross-validation means. Accuracy is the number of correct predictions divided by 324. For each class, precision is TP/(TP + FP), recall is TP/(TP + FN), and F1 is the harmonic mean of precision and recall. Macro F1 and macro recall average the corresponding class metrics equally across all three labels; weighted F1 uses class support as weights. Figure 5 presents random forest prediction counts with recorded labels in rows and predicted labels in columns. Its class recalls are diagonal counts divided by row totals.

After:
The primary metric was macro F1. Accuracy, macro recall, and Both recall were also reported. For each class, precision equals TP/(TP+FP), recall equals TP/(TP+FN), and F1 is their harmonic mean. Macro metrics assign equal weight to each of the three classes. Table 1 and Figure 4 show the arithmetic mean and sample standard deviation of the five outer-fold metrics. These standard deviations describe fold-to-fold variation and are not confidence intervals or tests of superiority.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 3.6 Performance measures and descriptive analyses — paragraph 45

Before:
Two stored metric names require correction. The fields cv_mean_accuracy and cv_std_accuracy contain the mean and standard deviation of cross-validation weighted F1, not accuracy. The field test_recall_minority contains the minimum recall over all classes, not necessarily recall for Both, the smallest class. Test ROC AUC was calculated as the unweighted mean of class-specific one-versus-rest AUCs, whereas the random forest search optimized a support-weighted version.

After:
Class-specific reports and Figure 5 pool the 1,620 out-of-fold predictions for each model. Confusion-matrix percentages divide each cell by its recorded-class row total. Pooled macro F1 can differ from the mean of fold-wise macro F1 because F1 is nonlinear; these summaries are reported separately. No statistical significance test, equivalence test, or calibration analysis was performed. Training macro F1 was summarized separately to describe the training-to-validation gap.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 3.6 Performance measures and descriptive analyses — paragraph 46

Before:
Class counts, symptom boxplots, and the manuscript Spearman heatmap were generated from the completed full dataset. Earlier exploratory heatmaps in the cleaning notebook used the default Pearson correlation; the code specifically used for Figure 3 calls method = spearman. No formal group-comparison tests or inferential model-superiority tests are reported. [需要作者补充：重分析后提供三模型的逐条预测、概率、完整分类报告及与评估设计匹配的不确定性估计；确认全样本探索性分析是否参与了特征或模型选择。]

After:
Figures 1–3 were regenerated from the raw file for descriptive purposes. Boxplots exclude missing values separately for each variable, and Spearman correlations use pairwise observed values. They are not based on the legacy completed dataset and were not used to select features in the revised run. Previous exploratory inspection is acknowledged. No formal between-group hypothesis tests are reported.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 3.7 Feature importance and research transparency — paragraph 48

Before:
Figure 6 was generated by fitting the selected random forest on the preprocessed training subset and extracting feature_importances_. These are impurity-based importance scores, not permutation importance or SHAP values. All 28 encoded predictors were included in model fitting; displaying only the ten largest importance values was not a feature-selection step. The two PEM indicators represent one original categorical variable. Importance does not establish causal effects or independent diagnostic value, particularly when target-assisted imputation has affected predictor values. No completed cross-fold importance-stability or external-validation analysis was supplied.

After:
Random forest feature contributions were assessed by permutation on each held-out outer fold. Each of the 15 original predictors was permuted ten times using random_state=100+fold_number, and the decrease in macro F1 was recorded. Permutation occurred before the fitted preprocessing pipeline, so all encoded categories of a source variable were assessed together. Repeats were averaged within a fold, then the five fold means were summarized by their mean and sample standard deviation. Figure 6 displays the ten largest means; all 15 predictors remained in fitting and full results are supplied. These are permutation contributions, not impurity-based scores or SHAP values.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 3.7 Feature importance and research transparency — paragraph 49

Before:
The saved model bundles contain the classifier, scaler, categorical transformer, label encoder, and feature names, but omit the numerical imputer used upstream. They therefore do not specify a complete procedure for predicting from raw records with missing inputs. Repository access and version information are addressed in Section 3.1. [需要作者补充：确认合成数据是否由真实个人数据衍生、数据和代码的使用及分享条件，以及本研究实际适用的伦理要求；不能自动声称已获审批或豁免。]

After:
Predictions and class probabilities, fold metrics, search tables, warnings, input checksums, and environment versions were saved. The package supports recomputation of this internal analysis and does not contain a validated deployment model. [需要作者补充：确认原数据和代码的使用及再分发条件，以及本研究实际适用的伦理要求；当前不能自行宣称已获得伦理批准或豁免。]

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 4.1 Class distribution and symptom profiles — paragraph 54

Before:
Figure 1. Assigned-label distribution in the supplied synthetic dataset: ME/CFS (648), Depression (567), and Both (405). Counts agree with both supplied CSV files and do not estimate disease prevalence in a clinical population.

After:
Figure 1. Recorded-label counts in the raw dataset: Both 405, Depression 567, and ME/CFS 648. These proportions do not estimate disease prevalence.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 4.1 Class distribution and symptom profiles — paragraph 55

Before:
Figure 2 shows higher fatigue-field values for records labeled ME/CFS than for those labeled Depression, and higher PHQ-9-field values for Depression. Both records show elevated values on both fields, while sleep-quality and brain-fog distributions overlap. These patterns describe the completed synthetic dataset and may reflect generation and imputation rules; they do not establish differences between clinical populations. No formal between-group tests are reported.

After:
Figure 2 describes observed fatigue, PHQ-9, sleep-quality, and brain-fog fields by recorded label. Fatigue values are higher for ME/CFS and Both records than for Depression records, whereas PHQ-9 values are higher for Depression and Both records. Sleep-quality and brain-fog distributions overlap. These patterns may reflect construction of the dataset and do not establish differences between clinically verified populations.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 4.1 Class distribution and symptom profiles — paragraph 57

Before:
Figure 2. Historical distributions of symptom-related fields in the completed synthetic dataset. “Comorbid” in the original image refers to the assigned Both label, not clinically confirmed comorbidity. The upstream imputation and export-history limitations in Sections 3.1 and 3.3 apply.

After:
Figure 2. Boxplots of observed raw values by recorded label. Missing values are omitted separately for each field. Both is a dataset label and does not establish confirmed comorbidity.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 4.1 Class distribution and symptom profiles — paragraph 58

Before:
Most displayed Spearman correlations between numerical features are close to zero (Figure 3). For example, the PHQ-9–age correlation is approximately 0.06 and the fatigue–PHQ-9 correlation is approximately -0.09. These coefficients describe pairwise monotonic associations among predictors. They do not establish the predictive value of any individual feature for the outcome, exclude nonlinear relationships, or prove that multivariable modeling is superior.

After:
Figure 3 reports pairwise Spearman correlations among the nine numerical predictors using available raw observations. These are descriptive associations between inputs. Small pairwise correlations do not exclude nonlinear relationships or determine the value of multivariable classification.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 4.1 Class distribution and symptom profiles — paragraph 60

Before:
Figure 3. Historical Spearman correlations among numerical predictors in the completed synthetic dataset. The figure-specific code uses Spearman correlation. These are not measures of outcome discrimination; imputation limitations apply.

After:
Figure 3. Spearman correlations computed from pairwise observed raw values. Each pair can have a different number of available records because of missingness.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 4.2 Overall model comparison — paragraph 62

Before:
At the two-decimal precision of Figure 4 and Table 1, both decision tree and random forest have accuracy 0.82, macro F1 0.81, and macro recall 0.81. Logistic regression has 0.80 for each metric. The saved notebook dashboard displays accuracies of 0.802, 0.821, and 0.824 for logistic regression, decision tree, and random forest, respectively. Random forest has the numerically highest displayed accuracy, but its advantage over decision tree is only approximately 0.3 percentage points at that precision. Thus, Figure 4 supports a description of close aggregate performance for the tree models; it does not support describing decision tree as the weakest model or random forest as clearly superior.

After:
Outer-fold mean accuracy was 0.778 ± 0.022 for logistic regression, 0.802 ± 0.024 for decision tree, and 0.811 ± 0.020 for random forest (mean ± SD). Mean macro F1 was 0.773 ± 0.021, 0.785 ± 0.025, and 0.799 ± 0.017, respectively. The majority baseline had mean accuracy 0.400 and macro F1 0.190.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 4.2 Overall model comparison — paragraph 63

Before:
Post-selection cross-validation weighted F1 means (standard deviations) were 0.7928 (0.0405) for logistic regression, 0.8132 (0.0340) for decision tree, and 0.8225 (0.0342) for random forest in the saved text output. These are separate from the test-set metrics in Figure 4. They are neither cross-validation accuracies nor independent outer-validation estimates, and the standard deviations are not confidence intervals for the test scores. No inferential comparison establishes superiority or equivalence of the models.

After:
Random forest had the highest mean aggregate metrics in this run. Its mean accuracy exceeded decision tree by approximately 0.93 percentage points and its mean macro F1 by 1.34 percentage points. Decision tree exceeded logistic regression in accuracy and macro F1, but its mean macro recall was slightly lower. Consequently, the evidence supports metric-specific numerical comparisons rather than describing decision tree as uniformly poor. No formal analysis establishes statistical superiority or equivalence.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 4.2 Overall model comparison — paragraph 64

Before:
The retained scores document the original completed-data analysis and are provisional because its preprocessing and file-provenance limitations prevent establishing test-set independence. A previous fixed-parameter audit reconstruction reproduced the displayed logistic-regression and decision-tree summaries but yielded 265 correct random forest predictions rather than the original 267. That reconstruction did not correct leakage or repeat hyperparameter selection, and its results have not replaced the original values. A corrected analysis with a documented data-processing chain is required before finalizing the comparison.

After:
The scores in this section replace the historical 80:20 split results. Differences from those results cannot be attributed solely to removal of leakage: imputation, evaluation partitions, tuning objectives, and candidate grids also changed. Training mean macro F1 was 0.790 for logistic regression, 0.796 for decision tree, and 0.910 for random forest, compared with outer-validation means of 0.773, 0.785, and 0.799. The larger random forest gap indicates remaining overfitting concerns despite nested evaluation.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 4.2 Overall model comparison — paragraph 65

Before:
Table 1. Historical synthetic test-set scores reproduced from Figure 4 at two-decimal precision. Close point estimates do not establish superiority or equivalence; corrected evaluation is required.

After:
Table 1. Revised outer-fold performance, reported as mean ± sample SD over five folds. SD is descriptive fold variation, not a confidence interval.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 4.2 Overall model comparison — paragraph 67

Before:
Figure 4. Historical accuracy, macro F1, and macro recall for the three models on 324 synthetic test records. Both tree models have the same displayed values at two-decimal precision. The plot contains no uncertainty intervals or significance tests; preprocessing limitations prevent interpreting these as leakage-controlled generalization estimates.

After:
Figure 4. Revised five-fold outer-validation mean accuracy, macro F1, and macro recall; error bars show one sample SD across folds. Values are not from the historical test split. Error-bar overlap or separation is not a significance test.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 4.3 Class-specific performance and random forest errors — paragraph 68

Before:
4.3 Class-specific performance and random forest errors

After:
4.3 Class-specific performance and error patterns

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 4.3 Class-specific performance and random forest errors — paragraph 69

Before:
The saved class-recall output reports Both recall of 0.790 for logistic regression, 0.728 for decision tree, and 0.667 for random forest on the 324-record test subset. The ranking for Both recall therefore differs from the ranking for displayed accuracy. This provides a descriptive example of why aggregate and class-specific metrics should be considered together. Because the original preprocessing compromises evaluation, the ranking is provisional and does not justify selecting a model for clinical use.

After:
Pooled Both recall was 0.743 (301/405) for logistic regression, 0.578 (234/405) for decision tree, and 0.659 (267/405) for random forest. Corresponding Both precision values were 0.667, 0.867, and 0.769, and F1 values were 0.703, 0.693, and 0.710. Logistic regression identified more Both records but also produced more false-positive Both predictions. The choice of metric therefore changes the apparent ranking.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 4.3 Class-specific performance and random forest errors — paragraph 70

Before:
For logistic regression, the lowest class recall was 0.754 for ME/CFS, not the Both recall of 0.790. Consequently, the notebook's plot labeled Minority Class Recall misidentifies the underlying statistic for that model. The random forest confusion matrix retained as Figure 5 contains 81 Both, 113 Depression, and 130 ME/CFS records and remains consistent with the original class-recall heatmap.

After:
Figure 5 shows pooled out-of-fold confusion matrices for all three models, each covering the same 1,620 records. Each prediction was generated by a pipeline fitted without that record’s outer fold. These are combined predictions from five fitted pipelines per model, not the predictions of one model fitted on all records.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 4.3 Class-specific performance and random forest errors — paragraph 72

Before:
Figure 5. Historical random forest confusion matrix for 324 synthetic test records. Rows denote recorded labels; columns denote predictions; percentages use row totals. Counts are unchanged from the original run. The preprocessing and provenance limitations prevent establishing test-set independence; this is not a clinical reference-standard validation.

After:
Figure 5. Pooled out-of-fold confusion matrices for logistic regression (LR), decision tree (DT), and random forest (RF). Rows are recorded labels; columns are predictions. Counts and row percentages cover 405 Both, 567 Depression, and 648 ME/CFS records per model.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 4.3 Class-specific performance and random forest errors — paragraph 73

Before:
Of 113 depression-labeled records, 104 were correctly classified, giving a recall of 92.0%. Of 130 ME/CFS-labeled records, 109 were correctly classified, giving a recall of 83.8%. Of 81 Both-labeled records, 54 were correctly classified, giving a recall of 66.7%. Thus, Both had the lowest recall within this random forest evaluation.

After:
Random forest correctly classified 267 of 405 Both records (65.9%), 510 of 567 Depression records (89.9%), and 537 of 648 ME/CFS records (82.9%). Its pooled accuracy was 1,314/1,620 (81.1%). Both had its lowest class recall.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 4.3 Class-specific performance and random forest errors — paragraph 74

Before:
Among Both records, 23 were predicted as ME/CFS (28.4%) and four as depression (4.9%). Among ME/CFS records, 12 were predicted as depression and nine as Both. These counts identify the direction of errors in this evaluation subset. They do not establish the biological cause of the errors or demonstrate clinical harm. They motivate reporting class-specific metrics for all three models.

After:
Of the 138 Both records misclassified by random forest, 106 were predicted as ME/CFS and 32 as Depression. Decision tree classified 137 Both records as ME/CFS, compared with 75 for logistic regression. These counts describe errors relative to the supplied labels; they do not establish missed diagnoses or clinical harm.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 4.4 Random forest feature importance — paragraph 76

Before:
The PHQ-9 feature has the largest historical importance value in Figure 6 (0.371), followed by pem_present_1.0 (0.162), fatigue_severity_scale_score (0.151), and pem_present_0.0 (0.149). The remaining displayed values are 0.023 or less at the reported precision. These values are retained from the original run, not from the audit reconstruction.

After:
The largest mean decreases in held-out random forest macro F1 after permutation were 0.231 ± 0.023 for depression_phq9_score, 0.155 ± 0.006 for pem_present, and 0.141 ± 0.016 for fatigue_severity_scale_score (mean ± SD across five fold means). All remaining mean decreases were below 0.007. These values differ in definition and scale from the historical impurity-based importance scores and should not be compared numerically with them.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 4.4 Random forest feature importance — paragraph 77

Before:
The two PEM columns represent categories of one predictor. Their impurity-based importance scores describe how the fitted model partitions this synthetic dataset, not independent clinical effects. Unknown label-generation rules and the imputation limitations may influence the apparent importance of symptom-related fields. No importance-stability analysis was supplied; consequently, these values cannot establish causal effects or clinically reliable discriminators.

After:
The ranking indicates dependence of this fitted procedure on the PHQ-9, PEM-presence, and fatigue fields under marginal permutation. It does not establish causation, independent diagnostic value, or valid clinical measurement. Correlated or structurally related predictors can complicate marginal permutation interpretation, and unknown label-construction rules may account for apparent predictive importance.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 4.4 Random forest feature importance — paragraph 79

Before:
Figure 6. Historical impurity-based importance from the selected random forest fitted on the 1,296-record preprocessed synthetic training subset. The top ten of 28 encoded predictors are shown. The two PEM columns represent one source variable. Values retain the original run and inherit its imputation limitations.

After:
Figure 6. Ten largest random forest permutation contributions, measured as the decrease in held-out macro F1. Bars average ten permutations within each outer fold and then the five fold means. Error bars show SD across fold means, not clinical-effect uncertainty. All 15 original fields were retained.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 5.1 Interpretation and contribution — paragraph 82

Before:
The original results show close aggregate scores for decision tree and random forest, while logistic regression has the highest recorded Both recall. Thus, the available outputs do not support an unqualified claim that random forest is the best model overall or that decision tree performs poorly. They illustrate a difference between accuracy-based ranking and sensitivity to one assigned label. The small displayed accuracy difference, different tuning objectives, and preprocessing leakage limit interpretation of this comparison.

After:
The revised analysis gives random forest the highest average aggregate scores, with a small numerical advantage over decision tree. Logistic regression has the highest Both recall, whereas random forest has the highest Both F1 and decision tree the highest Both precision. These results support joint consideration of aggregate and class-specific performance. They do not support a universal ranking of the models across all objectives.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 5.1 Interpretation and contribution — paragraph 83

Before:
The study contributes an applied comparison of three established methods for three synthetic labels, including Both. Its potential insight is the need to examine class-specific errors alongside aggregate performance: similar overall scores can coexist with different recall for a selected label. This is a dataset-specific observation requiring confirmation after corrected evaluation, not evidence of a new algorithm or clinical advance. Relative to Hawk et al. [9], the data type, class composition, and model comparison differ; no direct cross-study performance claim is warranted.

After:
Relative to previous symptom-based discrimination research [9], the present analysis addresses a different recorded-label composition, compares three established classifiers, and reports a common nested evaluation together with out-of-fold error patterns. Its dataset-specific insight is the trade-off between detecting Both records and avoiding false-positive Both predictions. This is an applied comparison, not an algorithmic innovation or evidence of clinical superiority. The observed patterns require evaluation in independently characterized data before broader interpretation.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 5.2 Scope of interpretation — paragraph 85

Before:
Misclassifying a Both record is an error relative to a supplied synthetic label. This analysis does not establish that such an error corresponds to a missed diagnosis in a patient, or that it carries greater clinical cost than other classification errors. Clinical consequences cannot be inferred from the confusion matrix alone.

After:
Misclassification in this study is disagreement with a supplied label. Because no independent clinical reference standard is documented, an error cannot be equated with a missed diagnosis in a patient. In particular, the Both category cannot establish confirmed comorbidity or its clinical consequences.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 5.2 Scope of interpretation — paragraph 86

Before:
Predicting recorded labels, discriminating conditions against an independent clinical reference standard, and demonstrating effectiveness in clinical practice are separate evidential questions. The original analysis attempted the first, but its evaluation is compromised by preprocessing leakage. It does not demonstrate earlier diagnosis, fewer missed diagnoses, screening benefit, or improved patient outcomes.

After:
Recorded-label prediction, discrimination against a clinical reference standard, and effectiveness in clinical practice are distinct evidentiary questions. The present analysis addresses the first using internal resampling. It does not demonstrate earlier diagnosis, screening benefit, treatment selection, or improved patient outcomes.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 5.3 Limitations and validation needs — paragraph 88

Before:
First, the study uses a single instructor-provided dataset described as synthetic. Detailed generation procedures, label-assignment rules, and statistical independence of records are not established by the supplied documentation. If labels were constructed using the same symptom fields used as predictors, performance could reflect recovery of imposed rules. The dataset therefore cannot establish discrimination between independently diagnosed clinical groups.

After:
First, data provenance remains unresolved. Provider details, generation or collection procedures, label-assignment rules, and statistical independence of records could not be verified. If labels were constructed from the same fields used as predictors, performance could reflect recovery of imposed rules. The results cannot establish discrimination between independently diagnosed clinical groups, whether or not the data are synthetic.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 5.3 Limitations and validation needs — paragraph 89

Before:
Second, the supplied cleaning workflow used target-assisted imputation before splitting, while the completed CSV export history is not fully documented. Encoding and scaling were fitted outside the cross-validation folds, and selected estimators were evaluated using non-nested post-selection cross-validation. The available materials consequently do not establish leakage-controlled performance. Reanalysis from the raw missing-value data is necessary, and the direction or magnitude of changes in model scores cannot be determined from the historical outputs.

After:
Second, the dataset and historical test results were inspected before the revised evaluation was designed. Nested cross-validation corrects the identified preprocessing and inner-selection operations but does not make the full research process prospective. There is no fresh external test set. Row-wise splitting also assumes that records can be separated meaningfully; unknown repeated, grouped, or generated dependencies may violate this assumption.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 5.3 Limitations and validation needs — paragraph 90

Before:
Third, the imputer did not meet its displayed stopping criterion, while the notebook suppressed warnings. The single completed dataset does not propagate multiple-imputation uncertainty. Four zero-sleep values and the discordant PEM status/duration combinations require a data dictionary before any correction. The learning-curve dashboard cell terminates with a plotting TypeError; its partial output is not evidence of a fully completed stability or overfitting assessment.

After:
Third, median and mode imputation do not model missingness mechanisms or propagate multiple-imputation uncertainty. Alternative imputers and sensitivity to anomalous field combinations were not examined. Four records have zero sleep hours; 602 observed PEM-negative records have positive PEM duration, while 16 PEM-positive records have zero duration. These values were retained because coding rules were unavailable. They limit substantive interpretation.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 5.3 Limitations and validation needs — paragraph 91

Before:
Fourth, model searches optimized different metrics, the test subset was inspected repeatedly, and no suitable uncertainty estimates or inferential comparison were supplied. A fixed-parameter reconstruction in a different environment did not exactly reproduce the original random forest outputs. Version strings found in the three model files indicate scikit-learn 1.5.1, whereas the audit used 1.8.0; this difference is a reproducibility lead, not a proven explanation. The original full environment and predictions remain necessary.

After:
Fourth, the study uses one five-fold partition configuration and limited candidate grids. Fold standard deviations are descriptive, and no inferential comparison demonstrates model superiority. The random forest training-to-validation gap indicates remaining overfitting. The results are conditional on the stated preprocessing and search choices; changes relative to the historical workflow cannot isolate any one methodological correction.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 5.3 Limitations and validation needs — paragraph 92

Before:
Finally, impurity-based importance has not been assessed for stability, and no independent external validation, calibration study, or prospective clinical-utility evaluation was supplied. Generalization and clinical use remain unestablished [8, 10].

After:
Finally, permutation importance is model- and metric-dependent and may be affected by correlated or structurally linked predictors. No calibration assessment, independent external validation, or prospective clinical-utility study was performed. The new environment is documented, but the full historical environment remains unconfirmed. Transparent reporting does not substitute for these additional forms of evidence [8, 10].

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 6 Conclusion — paragraph 94

Before:
This exploratory secondary analysis compared logistic regression, decision tree, and random forest for the ME/CFS, Depression, and Both labels in instructor-provided synthetic data. The original outputs showed close aggregate performance for the two tree models and higher Both recall for logistic regression. They support descriptive reporting of differing metric-based rankings, but not a conclusion of clear random forest superiority or poor decision tree performance. Preprocessing and provenance limitations prevent finalizing comparative performance estimates.

After:
This exploratory secondary analysis compared three established classifiers for recorded ME/CFS, Depression, and Both labels in an instructor-provided dataset of unverified provenance. With preprocessing fitted within training partitions and a common nested evaluation, random forest had the highest mean accuracy and macro F1, while logistic regression had the highest Both recall. The differences are descriptive and do not establish statistically significant superiority.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.

## 6 Conclusion — paragraph 95

Before:
The analysis must be repeated from the raw data with outcome information excluded from predictor imputation and preprocessing fitted within the relevant training partitions. Data-generation and label definitions also require documentation. Any conclusions from the corrected analysis should remain limited to the supplied synthetic-data setting; clinical diagnostic validity would require independent clinical evidence.

After:
The analysis illustrates the importance of reporting class-specific precision and recall alongside aggregate metrics. Uncertain data and label provenance, prior data inspection, and the absence of independent clinical validation restrict conclusions to the supplied dataset. These models should not be presented as clinically validated diagnostic tools.

Reason: Align manuscript with executed revised analysis and latest author provenance clarification.
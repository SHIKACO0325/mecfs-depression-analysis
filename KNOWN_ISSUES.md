# Known issues in the original analysis

These issues are disclosed for author review. This repository packages the original workflow; it does not claim they have been corrected.

1. **Target-assisted imputation:** cleaning notebook cell 7 (one-based numbering) adds `diagnosis_imputated` to the numerical imputation matrix. Held-out labels therefore inform predictor construction in the intended workflow.
2. **Full-sample imputation:** imputation is fitted on all 1,620 records before the 80:20 split. Categorical modes also come from the full sample.
3. **Preprocessing outside CV:** encoding and scaling are fitted on the outer training subset once, before inner cross-validation. They need to be fitted within each corresponding training fold.
4. **Post-selection CV:** selected models are scored using the same ten-fold configuration used in tuning; these are not independent nested-CV results. Test results are also inspected before and after tuning.
5. **Different tuning objectives:** logistic regression and decision tree optimize weighted F1; random forest optimizes weighted one-versus-rest AUC.
6. **Metric labels:** `cv_mean_accuracy` and `cv_std_accuracy` actually summarize weighted F1. `test_recall_minority` is the minimum class recall, not necessarily Both recall. Test AUC is macro OVR AUC, unlike the weighted RF tuning objective.
7. **Single imputation and convergence:** only one completed dataset is supplied. The recorded final iterative change exceeds the displayed stopping threshold after 20 iterations; warnings are suppressed.
8. **Partial/error outputs:** the advanced dashboard cell records a plotting `TypeError`. Some subsequent cells have no saved execution result. Do not claim a complete overfitting/stability assessment.
9. **Incomplete prediction bundle:** notebook exports contain the model, scaler, categorical transformer, label encoder, and feature names, but not the upstream numerical imputer. `.joblib` files are executable serialization formats; they have not been deserialized in this packaging step.
10. **Environment and reproduction:** static strings in model files indicate scikit-learn 1.5.1. The notebook metadata lists Python 3.14.6, but the full original environment is unconfirmed. A prior audit reconstruction using scikit-learn 1.8.0 and saved parameters yielded RF accuracy 265/324, compared with the original 267/324. This does not establish the cause or constitute corrected evaluation. Original artifacts remain unchanged.
11. **Data meaning:** real versus synthetic status, diagnosis-label creation, and several field meanings are unresolved. Label prediction is not evidence of clinical diagnostic validity.
12. **Interpretability:** `feature_importances_` is impurity-based importance, not SHAP. Showing ten features is not feature selection. Averaging LR coefficient magnitudes with tree importance scores, or comparing iteration counts and depth as a common complexity scale, is not justified.

## Required correction

Confirm the data provenance and dictionary. Start from raw missing data, exclude outcome information from predictor imputation, and fit all preprocessing within the appropriate training partitions. Prespecify the evaluation and tuning objective, account transparently for prior test-set inspection, save complete predictions and dependencies, and update the manuscript consistently. Independent clinical validation would require suitable independent clinical data.

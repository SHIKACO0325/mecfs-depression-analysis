# Revised ME/CFS and depression label classification

This package contains an executed retrospective internal reanalysis. The original dataset provenance and synthetic status remain unverified. Results concern recorded labels, not clinical diagnoses.

## Run

Use Python 3.12.14 and install the pinned packages with `python -m pip install -r requirements.txt`. Then run:

```bash
python run_analysis.py --data Data.csv
```

Alternatively, open `run_reanalysis.ipynb` in Jupyter with a kernel containing these packages and run its code cell. Jupyter is a launcher; all analysis logic is in the supplied script. Running regenerates the results directory and may replace existing results. Preserve a copy to compare runs.

## Evaluation fixed for this revision

Five outer stratified folds (seed 42), three inner stratified folds (seed 43). Training-fold median numeric imputation and most-frequent categorical imputation, numerical standardization, and one-hot encoding are inside the classifier pipeline. Diagnosis is excluded from predictors. All searches optimize macro F1. LR uses 4 C candidates; DT and RF each use 12 candidates. Grids and fixed model parameters are in run_analysis.py and results/protocol.json. All three classifiers use balanced class weights. A majority baseline uses the same folds.

The specification was fixed before this new run, after historical dataset inspection. This is not a prospective or externally independent validation. No final deployment model is exported. No claim of clinical utility or statistically significant model superiority is made.

Median/mode imputation replaces the historical iterative approach. The evaluation design and search grids also differ from the historical analysis, so score differences do not isolate leakage effects. No undocumented outlier recoding or sample exclusion is performed. Grouping and record independence cannot be verified. The supplied data and provider identity have not been independently authenticated.

## Outputs

- results/summary.json: pooled predictions and fold summary statistics. Pooled macro F1 is not the same as fold-mean macro F1.
- results/fold_metrics.csv: fold performance and apparent training macro F1; SD describes variation, not confidence intervals.
- results/oof_predictions.csv: 0-based raw row index, outer fold, model, recorded label, prediction, probabilities; each row receives one outer prediction per model.
- results/search_*.csv and selected_parameters.json: inner searches and fold-specific selections.
- results/permutation_importance.csv and importance_summary.csv: marginal permutation decreases in held-out macro F1. Ten repeats averaged within each fold; mean and SD then calculated across five folds.
- results/figure_01.png to figure_06.png: revised figures; Figures 1–3 use observed raw values, not a full-data imputation.
- results/data_audit.json, environment.json, warnings.json, protocol.json: input audit and execution settings.
- run.log: actual execution log.
- change_log.md and change_log.json: paragraph-level before and after text relative to the preceding review draft. Table 1 and all six figures are replaced by newly computed results.

## GitHub integration

Original archive: https://github.com/SHIKACO0325/mecfs-depression-analysis . Its public status was verified during this revision; older README references to private status are outdated. This revised package has NOT been uploaded to that repository. Keep original notebooks, model artifacts, figures, and completed CSV in legacy paths. Add the contents of this package under a separate revised_analysis/ directory and link that directory from the root README. Amend the root status to public author-review archive and retain the unverified-provenance disclosure. Cite the final commit or release after upload; do not invent a DOI. Record permissions for original data/code before claiming a license or unrestricted reuse.

Data.csv here is the exact supplied raw local input used for the run. Its values match the public repository raw CSV; file bytes differ. The public raw blob was 1095a87e17ef46d21309d3a579b73766dfb6fc6e at retrieval. The local SHA-256 is in protocol.json and SHA256SUMS.txt.

Implementation references: https://scikit-learn.org/stable/common_pitfalls.html and https://scikit-learn.org/stable/auto_examples/model_selection/plot_nested_cross_validation_iris.html . These document the pipeline and nested-evaluation approach, not this dataset’s validity.

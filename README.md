# ME/CFS and depression: exploratory classification materials

**Status: private author-review working archive. This is not a validated clinical diagnostic model.**

This project organizes the data, original notebooks, saved model artifacts, and historical figures associated with the manuscript *Machine Learning-Based Differential Diagnosis of ME/CFS and Depression Using Clinical and Symptom Features*. The manuscript is under revision.

## Data provenance

The manuscript author reports receiving the dataset from a former course instructor associated with a Coursera course. The author believes the dataset may have been artificially generated; this has not yet been confirmed by the provider. These files must not be described as verified patient records or an official Coursera dataset.

Using an existing dataset is secondary analysis. That description does not resolve whether the underlying data are empirical or synthetic. Provider attribution, generation/collection procedures, diagnosis-label rules, and permission to redistribute the materials remain to be established. See [data/README.md](data/README.md).

## Contents

| Folder/file | Contents |
| --- | --- |
| `data/raw/Data.csv` | Supplied data with missing values; unchanged |
| `data/legacy_processed/multiple_imputed.csv` | Supplied completed dataset; unchanged; affected by the documented legacy workflow |
| `notebooks/legacy/` | Two original notebooks, including saved outputs; unchanged |
| `models/legacy/` | Three original `.joblib` files; unchanged |
| `figures/legacy/` | Six original manuscript figures; historical results |
| `KNOWN_ISSUES.md` | Methodological and reproducibility limitations |
| `tools/stage_legacy.py` | Copies files into a separate working directory with filenames expected by the notebooks |
| `docs/ENVIRONMENT.md` | What is and is not known about dependencies |
| `docs/PAPER_CITATION.md` | Conditional manuscript wording and citation template |
| `CITATION.cff.example` | Draft citation metadata; finalize after repository URL and authorship confirmation |
| `SHA256SUMS.txt` | Checksums for the packaged files |

## Inspecting and running the archived notebooks

Read `KNOWN_ISSUES.md` first. Inspect saved outputs without rerunning if the goal is to review the original analysis. This archive does not provide a corrected analysis or promise that all cells execute successfully.

For a separate local working copy, run from the project root:

```bash
python tools/stage_legacy.py
cd work/legacy
jupyter lab
```

The staging script uses only Python's standard library. Jupyter and the scientific packages listed in `docs/ENVIRONMENT.md` are required to run the notebooks themselves; the original complete environment is not available.

The notebook filenames retain their original spelling. The script supplies `group_30.csv` and `group_30_multiple_imputed.csv`, which the notebooks expect, as copies of the supplied CSV files. This is a working filename mapping, not proof of their original export history. The cleaning notebook does not visibly export its in-memory imputation result before reading the completed CSV. Rerunning it therefore does not automatically replace the completed file used for evaluation.

Notebook execution can retrain models and overwrite outputs in the working directory. The plotting dashboard has a recorded error. The evaluation notebook's model-saving loop repeatedly overwrites `best_model.pkl`; that filename should not be interpreted as a validated model-selection result. The staged working directory is excluded from Git.

## Analysis status

The supplied data contain 1,620 records and 15 predictors plus the `diagnosis` field. Label counts are ME/CFS 648, Depression 567, and Both 405. The original evaluation used an 80:20 stratified split and three models: logistic regression, decision tree, and random forest.

The legacy cleaning code uses the diagnosis label to assist numerical imputation and fits imputation before the split. Encoding and scaling are also outside the inner cross-validation folds. Historical scores are consequently not leakage-controlled estimates. Corrected preprocessing, tuning, and evaluation remain outstanding. Uploading the files to GitHub does not fix these issues.

## Attribution, permissions, and citation

No open-source or open-data license is assigned by this packaging step. Rights, attribution, and redistribution permission for instructor-provided data/code require confirmation. Keep the repository private while resolving these questions. A private URL alone does not provide access to reviewers or readers.

After the materials are cleared for sharing and the analysis is finalized, complete the citation metadata and cite the exact release or commit used by the paper. Do not invent a DOI, publication date, repository address, or clinical data source. The repository citation documents access to these materials; it does not replace the original data-source statement.

# Environment status

The original notebooks import pandas, NumPy, scikit-learn, matplotlib, seaborn, and joblib, and require a Jupyter-compatible environment for interactive use. The full original dependency lockfile was not supplied. No fabricated `requirements.txt` is included.

Static version strings in the three saved model files indicate scikit-learn 1.5.1. Notebook metadata reports Python 3.14.6; these clues do not establish a single verified environment.

A separate audit used Python 3.12, scikit-learn 1.8.0, NumPy 2.3.5, and pandas 2.2.3. It was not an end-to-end reproduction and did not exactly reproduce the RF result. These audit versions must not be presented as the original requirements.

Request the original `requirements.txt`, `environment.yml`, or `pip freeze` output. Once a corrected workflow is run successfully, export and commit its verified environment along with that workflow. Do not resolve failures by silently changing code while retaining old output claims.

"""Stage a separate legacy working copy; do not retrain or correct the models."""
from pathlib import Path
import shutil


def main():
    root = Path(__file__).resolve().parents[1]
    destination = root / "work" / "legacy"
    if destination.exists():
        raise SystemExit("work/legacy already exists. Use another copy of the project to avoid overwriting your work.")
    files = {
        root / "data/raw/Data.csv": "group_30.csv",
        root / "data/legacy_processed/multiple_imputed.csv": "group_30_multiple_imputed.csv",
    }
    for name in ["data cleaning & visulazation -2.ipynb", "Evaluation-6.ipynb"]:
        files[root / "notebooks/legacy" / name] = name
    missing = [str(p) for p in files if not p.is_file()]
    if missing:
        raise SystemExit("Missing inputs: " + ", ".join(missing))
    destination.mkdir(parents=True)
    for source, name in files.items():
        shutil.copyfile(source, destination / name)
    print("Legacy working files staged in:", destination)
    print("Known leakage and plotting issues remain. No analysis was run.")


if __name__ == "__main__":
    main()

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

RAW_PATH = BASE_DIR / "data" / "raw" / "turismo_europa.csv"
OUT_PATH = BASE_DIR / "data" / "processed" / "clean_dataset.csv"

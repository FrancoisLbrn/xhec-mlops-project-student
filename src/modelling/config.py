from pathlib import Path

CATEGORICAL_COLS = []
NUMERICAL_COLS = []

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIRPATH = str(PROJECT_ROOT / "data")
MODEL_DIRPATH = str(PROJECT_ROOT / "src/web_service/local_objects")

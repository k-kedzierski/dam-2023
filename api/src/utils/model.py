from pathlib import Path
from typing import Any
import joblib
import pandas as pd


class Model:
    def __init__(self, model_path: str) -> None:
        self.model_path = model_path
        self.model = self._load_model()

    def _load_model(self) -> Any:
        return joblib.load(Path(self.model_path))
    
    def predict(self, X: pd.DataFrame):
        return self.model.predict(X)
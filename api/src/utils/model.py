from functools import cache
from pathlib import Path
from typing import Any
import joblib
import pandas as pd

from ..utils.logger import get_logger
from ..config import settings

log = get_logger()


@cache
def get_model():
    return Model(model_path=settings.MODEL_PATH)


class Model:
    def __init__(self, model_path: str) -> None:
        self.model_path = model_path
        self.model = self._load_model()

    def _load_model(self) -> Any:
        log.info(f"Loading model '{self.model_path}'")
        model = joblib.load(Path(self.model_path))
        log.info(f"Model loaded sucessfully: {model}")
        return model

    def predict(self, X: pd.DataFrame):
        return self.model.predict(X)

from fastapi import APIRouter
import pandas as pd
from scipy import stats

from ..utils.model import Model

from ..schemas import PredictionIntervalRequest, PredictRequest

router = APIRouter()

@router.post("/housing/predict")
async def predict(request: PredictRequest):
    model = Model(model_path="../models/best_model.pkl")
    X = pd.DataFrame([request.data.dict()])
    y_pred = model.predict(X).flat[0]
    return {"response": y_pred}

@router.post("/housing/prediction_interval")
async def prediction_interval(request: PredictionIntervalRequest):
    model = Model(model_path="../models/best_model.pkl")
    estimated_stdev = 50581.26

    X = pd.DataFrame([request.data.dict()])
    y_pred = model.predict(X).flat[0]

    interval = stats.norm.ppf((1 + (1 - request.alpha)) / 2) * estimated_stdev

    return {"response": (y_pred - interval, y_pred + interval)}

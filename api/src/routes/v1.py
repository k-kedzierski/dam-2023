from fastapi import APIRouter
import pandas as pd
import time
from scipy import stats

from ..utils.logger import get_logger
from ..utils.model import Model
from ..config import settings

from ..schemas import PredictionIntervalRequest, PredictRequest

log = get_logger()

router = APIRouter()


@router.post("/housing/predict")
async def predict(request: PredictRequest):
    log.info("Running prediction...")

    start_time = time.perf_counter()
    model = Model(model_path="../models/best_model.pkl")
    X = pd.DataFrame([request.data.dict()])
    y_pred = model.predict(X).flat[0]

    elapsed_time = round(time.perf_counter() - start_time, 3)

    log.info(f"Finished predicting: {y_pred=} in {elapsed_time} seconds.")
    return {"response": y_pred, "time": elapsed_time}

@router.post("/housing/prediction_interval")
async def prediction_interval(request: PredictionIntervalRequest):
    log.info("Calculating prediction intervals...")

    start_time = time.perf_counter()
    model = Model(model_path=settings.MODEL_PATH)
    X = pd.DataFrame([request.data.dict()])
    y_pred = model.predict(X).flat[0]

    interval = stats.norm.ppf((1 + (1 - request.alpha)) / 2) * settings.ESTIMATED_STDEV
    lower_bound = y_pred - interval
    upper_bound = y_pred + interval

    elapsed_time = round(time.perf_counter() - start_time, 3)

    log.info(f"Finished calculating prediction intervals: ({lower_bound} ,{upper_bound}) in {elapsed_time} seconds.")
    return {"response": (y_pred - interval, y_pred + interval), "time": elapsed_time}

from fastapi import APIRouter

from ..schemas import ConfidenceIntervalRequest, PredictRequest

router = APIRouter()

@router.post("/housing/predict")
async def predict(request: PredictRequest):
    return {"response": "foo"}

@router.post("/housing/confidence_interval")
async def confidence_interval(request: ConfidenceIntervalRequest):
    return {"response": "bar"}

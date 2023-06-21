from pydantic import BaseModel, validator
from typing import Optional

class FeaturesModel(BaseModel):
    longitude: Optional[float]
    latitude: Optional[float]
    housing_median_age: Optional[float]
    total_rooms: Optional[int]
    total_bedrooms: Optional[int]
    population: Optional[float]
    households: Optional[int]
    median_income: Optional[float]
    ocean_proximity: Optional[str]

class PredictRequest(BaseModel):
    data: FeaturesModel

class PredictionIntervalRequest(BaseModel):
    data: FeaturesModel
    alpha: float = 0.05

    @validator("alpha")
    def alpha_between_zero_one(cls, v):
        if not(0.0 < v < 1.0):
            raise ValueError("Alpha must be between 0.0 and 1.0!")

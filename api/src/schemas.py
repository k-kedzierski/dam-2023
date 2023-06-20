from pydantic import BaseModel, validator

class FeaturesModel(BaseModel):
    longitude: float
    latitude: float
    housing_median_age: float
    total_rooms: int
    total_bedrooms: int
    population: float
    households: int
    median_income: float
    ocean_proximity: str

class PredictRequest(BaseModel):
    data: FeaturesModel

class ConfidenceIntervalRequest(BaseModel):
    data: FeaturesModel
    alpha: float

    @validator("alpha")
    def alpha_between_zero_one(cls, v):
        if not(0.0 < v < 1.0):
            raise ValueError("Alpha must be between 0.0 and 1.0!")

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str


class PredictRequest(BaseModel):
    text: str = Field(..., min_length=1, description="News article text to classify")


class PredictResponse(BaseModel):
    prediction: str
    confidence: float

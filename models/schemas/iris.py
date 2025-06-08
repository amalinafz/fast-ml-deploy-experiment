from pydantic import BaseModel, conlist
from typing import List, Any


class Iris(BaseModel):
    data:  List[conlist(float, min_length=4, max_length=4)]


class IrisPredictionResponse(BaseModel):
    prediction: List[int]
    probability: List[Any]
    log_probability: List[Any]

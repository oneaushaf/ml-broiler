from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class RequestBody(BaseModel):
    age: int
    count: int
    image: str

class ResponseBody(BaseModel):
    average_weight: float
    time: int

@app.post("/predict/weight",response_model=ResponseBody)
def predict_weight(data: RequestBody):
    average_weight = data.age * 2
    time_taken = data.count * 5

    return {"average_weight":average_weight,"time":time_taken}
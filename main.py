from fastapi import FastAPI
from pydantic import BaseModel, Field
from backend import hugger as hug

class PredictionRequest(BaseModel):
  query_string: str Field(description="DealIds to target")

app = FastAPI()

@app.get("/health")
def health():
    return "Service is online"


@app.post("/sentiment")
def my_endpoint(request: PredictionRequest):
    sentiment = hug.get_sentiment(request.query_string)
    return sentiment

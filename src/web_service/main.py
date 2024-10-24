from app_config import APP_DESCRIPTION, APP_TITLE, APP_VERSION, MODEL_VERSION
from fastapi import FastAPI
from lib.models import InputData, PredictionOut

app = FastAPI(
    title=APP_TITLE, description=APP_DESCRIPTION, version=APP_VERSION
)


@app.get("/")
def home() -> dict:
    return {
        "health_check": "App up and running!",
        "model_version": MODEL_VERSION,
    }


@app.post("/predict", response_model=PredictionOut, status_code=201)
def predict(payload: InputData) -> dict:
    return {"health_check": "Prediction missing!"}

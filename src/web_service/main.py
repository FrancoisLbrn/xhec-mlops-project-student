from app_config import (
    APP_DESCRIPTION,
    APP_TITLE,
    APP_VERSION,
    MODEL_VERSION,
    PATH_TO_MODEL,
    PATH_TO_PREPROCESSOR,
)
from fastapi import FastAPI
from lib.inference import run_inference
from lib.models import InputData, PredictionOut
from lib.utils import load_pickle

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
def predict(value: InputData) -> dict:
    model = load_pickle(PATH_TO_MODEL)
    preprocessor = load_pickle(PATH_TO_PREPROCESSOR)
    y = run_inference([value], preprocessor, model)
    return {"abalone_age_prediction": y}

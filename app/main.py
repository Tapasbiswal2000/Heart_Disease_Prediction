from fastapi import FastAPI

from app.model import predict_heart_disease
from app.schemas import PatientData,PredictionResponse


app = FastAPI()


@app.get("/")
def home():
    return {"message": "Heart Disease Prediction API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/predict", response_model=PredictionResponse)
def predict(patient: PatientData):
    prediction, probability = predict_heart_disease(
        patient.model_dump()
    )

    return {
        "prediction": prediction,
        "probability": probability
    }
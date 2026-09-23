import pickle
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "best_model.pkl"


with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


def predict_heart_disease(patient_data):
    input_data = pd.DataFrame([patient_data])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    return int(prediction), float(probability)
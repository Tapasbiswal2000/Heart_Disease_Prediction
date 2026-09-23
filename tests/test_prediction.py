from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_prediction():
    patient_data = {
        "age": 45,
        "resting_blood_pressure": 128,
        "serum_cholesterol_mg_per_dl": 308,
        "oldpeak_eq_st_depression": 0.0,
        "max_heart_rate_achieved": 170,
        "sex": 1,
        "chest_pain_type": 2,
        "fasting_blood_sugar_gt_120_mg_per_dl": 0,
        "resting_ekg_results": 2,
        "num_major_vessels": 0,
        "slope_of_peak_exercise_st_segment": 1,
        "exercise_induced_angina": 0,
        "thal": "normal"
    }

    response = client.post("/predict", json=patient_data)

    assert response.status_code == 200

    result = response.json()

    assert result["prediction"] == 0
    assert result["probability"] == 0.20979084977778786

def test_prediction_invalid_age():
    patient_data = {
        "age": -10,
        "resting_blood_pressure": 128,
        "serum_cholesterol_mg_per_dl": 308,
        "oldpeak_eq_st_depression": 0.0,
        "max_heart_rate_achieved": 170,
        "sex": 1,
        "chest_pain_type": 2,
        "fasting_blood_sugar_gt_120_mg_per_dl": 0,
        "resting_ekg_results": 2,
        "num_major_vessels": 0,
        "slope_of_peak_exercise_st_segment": 1,
        "exercise_induced_angina": 0,
        "thal": "normal"
    }

    response = client.post("/predict", json=patient_data)

    assert response.status_code == 422

def test_prediction_missing_field():
    patient_data = {
        "resting_blood_pressure": 128,
        "serum_cholesterol_mg_per_dl": 308,
        "oldpeak_eq_st_depression": 0.0,
        "max_heart_rate_achieved": 170,
        "sex": 1,
        "chest_pain_type": 2,
        "fasting_blood_sugar_gt_120_mg_per_dl": 0,
        "resting_ekg_results": 2,
        "num_major_vessels": 0,
        "slope_of_peak_exercise_st_segment": 1,
        "exercise_induced_angina": 0,
        "thal": "normal"
    }

    response = client.post("/predict", json=patient_data)

    assert response.status_code == 422
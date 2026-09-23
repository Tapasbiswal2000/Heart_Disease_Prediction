from pydantic import BaseModel, Field


class PatientData(BaseModel):
    age: int = Field(..., ge=1, le=120)
    resting_blood_pressure: int = Field(..., ge=50, le=250)
    serum_cholesterol_mg_per_dl: int = Field(..., ge=50, le=700)
    oldpeak_eq_st_depression: float = Field(..., ge=-10, le=20)
    max_heart_rate_achieved: int = Field(..., ge=50, le=250)

    sex: int = Field(..., ge=0, le=1)
    chest_pain_type: int = Field(..., ge=0, le=4)
    fasting_blood_sugar_gt_120_mg_per_dl: int = Field(..., ge=0, le=1)
    resting_ekg_results: int = Field(..., ge=0, le=2)
    num_major_vessels: int = Field(..., ge=0, le=3)
    slope_of_peak_exercise_st_segment: int = Field(..., ge=0, le=2)
    exercise_induced_angina: int = Field(..., ge=0, le=1)

    thal: str


class PredictionResponse(BaseModel):
    prediction: int
    probability: float
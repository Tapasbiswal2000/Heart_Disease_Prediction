# Heart Disease Prediction

An end-to-end Machine Learning classification project that predicts the presence of heart disease from patient clinical features.

This project covers the complete workflow from data preprocessing and model training to API development, automated testing, Docker containerization, and cloud deployment.

> **Disclaimer:** This project is for educational and demonstration purposes only. It is not a medical diagnostic tool and should not be used to make healthcare decisions.

---

## 🚀 Live API

**Deployed API:**  
https://heart-disease-api-b29r.onrender.com
### API Documentation

```text
https://heart-disease-api-b29r.onrender.com/docs
```

The deployed API provides:

- `/` — API status
- `/health` — Health check
- `/docs` — Interactive Swagger/OpenAPI documentation
- `/predict` — Heart disease prediction

---

## 📌 Project Overview

This project is a **binary classification problem**.

The model predicts whether heart disease is present based on patient information such as:

- Age
- Resting blood pressure
- Serum cholesterol
- Chest pain type
- Maximum heart rate achieved
- Exercise-induced angina
- Resting ECG results
- Number of major vessels
- Thalassemia-related information
- Other clinical features

The final machine learning solution uses a Scikit-learn preprocessing pipeline combined with an **SVC classifier**.

The complete pipeline is saved as a Pickle file and loaded by the FastAPI application for prediction.

---

# 🧠 Machine Learning Pipeline

The overall workflow is:

```text
Dataset
   ↓
Data Understanding
   ↓
Exploratory Data Analysis
   ↓
Train-Test Split
   ↓
Data Preprocessing
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Best Model Selection
   ↓
Pipeline Serialization
   ↓
FastAPI
   ↓
Docker
   ↓
Render Deployment
```

## Preprocessing

The preprocessing pipeline uses a `ColumnTransformer`.

### Numerical Features

Numerical features are standardized using:

```text
StandardScaler
```

### Categorical Features

Categorical features are encoded using:

```text
OneHotEncoder(handle_unknown="ignore")
```

### Final Model

The final classification model is:

```text
SVC
```

The preprocessing and model are combined into a single Scikit-learn `Pipeline`.

The trained pipeline is saved as:

```text
models/best_model.pkl
```

This allows the API to use the same preprocessing and model during inference.

---

# 🏗️ Project Architecture

```text
                         Client
                           │
                           ▼
                    ┌─────────────┐
                    │   FastAPI   │
                    └──────┬──────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Pydantic Schema │
                  │ Input Validation│
                  └────────┬────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ ML Pipeline       │
                 │                   │
                 │ ColumnTransformer │
                 │ ├─ StandardScaler │
                 │ └─ OneHotEncoder  │
                 │                   │
                 │ SVC Classifier    │
                 └─────────┬─────────┘
                           │
                           ▼
                  Prediction Result
                           │
                           ▼
                  Class + Probability
```

### Deployment Architecture

```text
GitHub
   ↓
Render
   ↓
Docker Build
   ↓
Docker Container
   ↓
Uvicorn
   ↓
FastAPI
   ↓
ML Model
   ↓
Prediction
```

---

# 🌐 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Returns API status |
| GET | `/health` | Health check |
| GET | `/docs` | Swagger API documentation |
| POST | `/predict` | Predicts heart disease class |

---

## GET `/`

Example response:

```json
{
  "message": "Heart Disease Prediction API is running"
}
```

---

## GET `/health`

Example response:

```json
{
  "status": "healthy"
}
```

This endpoint is used to verify that the API is running correctly.

---

## GET `/docs`

FastAPI automatically provides interactive Swagger documentation.

Open:

```text
YOUR_RENDER_URL/docs
```

You can use Swagger UI to test the `/predict` endpoint directly from the browser.

---

# 🔮 POST `/predict`

The `/predict` endpoint accepts patient information and returns a predicted class and probability.

## Example Request

```json
{
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
```

## Example Response

```json
{
  "prediction": 0,
  "probability": 0.20979084977778786
}
```

The `prediction` represents the predicted class.

The `probability` represents the model probability for class `1`.

---

# 🛡️ Input Validation

The API uses **Pydantic** schemas to validate incoming data before sending it to the machine learning model.

For example, invalid values such as:

```json
{
  "age": -10
}
```

are rejected by the API validation layer.

This prevents invalid input from reaching the model.

---

# 🧪 Testing

The project uses:

```text
pytest
```

and FastAPI's:

```text
TestClient
```

The test suite checks:

- API health endpoint
- Prediction endpoint
- Valid prediction behavior
- Invalid input validation

Run the tests using:

```bash
pytest
```

Current test result:

```text
4 passed
```

---

# 🐳 Docker

The FastAPI application is containerized using Docker.

## Build Docker Image

From the project root:

```bash
docker build -t heart-disease-api .
```

## Run Docker Container

```bash
docker run -d -p 8000:8000 --name heart-disease-api-container heart-disease-api
```

## Check Running Container

```bash
docker ps
```

## View Container Logs

```bash
docker logs heart-disease-api-container
```

The container runs:

```text
Uvicorn
   ↓
FastAPI
```

on port:

```text
8000
```

---

# 💻 Local Setup

## 1. Clone the Repository

```bash
git clone https://github.com/Tapasbiswal2000/Heart_Disease_Prediction.git
```

## 2. Navigate to the Project

```bash
cd Heart_Disease_Prediction
```

## 3. Create Virtual Environment

Windows:

```bash
python -m venv venv
```

## 4. Activate Virtual Environment

```bash
venv\Scripts\activate
```

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

For development and testing dependencies:

```bash
pip install -r requirements-dev.txt
```

## 6. Run FastAPI

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

Health check:

```text
http://127.0.0.1:8000/health
```

---

# 📁 Project Structure

```text
Heart_Disease_Prediction/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── model.py
│   └── schemas.py
│
├── data/
│   └── processed/
│       └── heart_disease.csv
│
├── models/
│   └── best_model.pkl
│
├── notebooks/
│   ├── heart_disease_prediction.ipynb
│   └── predict.ipynb
│
├── tests/
│   ├── test_health.py
│   └── test_prediction.py
│
├── .dockerignore
├── .gitignore
├── Dockerfile
├── pytest.ini
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

---

# 📂 Important Files

| File | Purpose |
|---|---|
| `notebooks/heart_disease_prediction.ipynb` | EDA, preprocessing, model training and evaluation |
| `notebooks/predict.ipynb` | Model loading and prediction testing |
| `models/best_model.pkl` | Saved machine learning pipeline |
| `app/main.py` | FastAPI application and API endpoints |
| `app/model.py` | Model loading and prediction logic |
| `app/schemas.py` | Pydantic request validation |
| `tests/test_health.py` | Health endpoint tests |
| `tests/test_prediction.py` | Prediction and validation tests |
| `Dockerfile` | Docker image configuration |
| `requirements.txt` | Runtime dependencies |
| `requirements-dev.txt` | Development/testing dependencies |
| `pytest.ini` | Pytest configuration |

---

# 🛠️ Technologies Used

## Programming

- Python

## Data Science

- NumPy
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

## Machine Learning

- Scikit-learn
- StandardScaler
- OneHotEncoder
- ColumnTransformer
- Pipeline
- SVC

## API Development

- FastAPI
- Pydantic
- Uvicorn

## Testing

- Pytest
- HTTPX
- FastAPI TestClient

## Deployment

- Docker
- Git
- GitHub
- Render

---

# 🔄 Development Workflow

The project follows this workflow:

```text
Develop
   ↓
Test Locally
   ↓
Run Pytest
   ↓
Build Docker Image
   ↓
Run Docker Container
   ↓
Test API
   ↓
Push to GitHub
   ↓
Render Automatically Deploys
   ↓
Test Cloud API
```

---

# 📌 Key Engineering Practices

- Train-test split before data-dependent preprocessing
- Leakage-aware preprocessing
- Separate numerical and categorical preprocessing
- Reusable Scikit-learn Pipeline
- Model serialization using Pickle
- Pydantic input validation
- Automated API testing
- Docker containerization
- Git/GitHub version control
- Cloud deployment
- Health-check endpoint
- Swagger/OpenAPI documentation

---

# 💼 Resume / Portfolio Description

### Detailed Description

> Built and deployed an end-to-end Heart Disease Prediction system using Python and Scikit-learn. Developed a reusable machine learning pipeline with ColumnTransformer, StandardScaler, OneHotEncoder and SVC, then serialized the trained pipeline for inference. Exposed the model through a validated FastAPI REST API, added automated testing with Pytest, containerized the application using Docker, and deployed the API to Render for cloud-based inference.

### Short Resume Bullet

> Built and deployed a production-style heart disease classification API using Scikit-learn, FastAPI, Pytest, Docker and Render, implementing reusable preprocessing, model serialization, input validation and automated API testing.

---

# 👨‍💻 Author

**Tapas Ranjan Biswal**

GitHub:

https://github.com/Tapasbiswal2000

---

# ⚠️ Disclaimer

This project is intended for educational and software engineering demonstration purposes only.

The predictions generated by this application should not be considered medical advice, diagnosis, or treatment recommendations.

Real medical decisions should always be made by qualified healthcare professionals using appropriate clinical evaluation.

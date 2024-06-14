# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# from sklearn.preprocessing import StandardScaler
# from sklearn.pipeline import Pipeline
# from sklearn.compose import ColumnTransformer
# from sklearn.impute import SimpleImputer
# from sklearn.preprocessing import OneHotEncoder
# import pandas as pd
# import numpy as np
# import joblib

# app = FastAPI()



# # Modelo de machine learning
# class Model(BaseModel):
#     features: list
#     target: str

# # # Función para entrenar el modelo
# # def train_model(X_train, y_train):
# #     # Crear un pipeline para preprocesar los datos
# #     preprocessor = ColumnTransformer(
# #         transformers=[
# #             ("num", SimpleImputer(strategy="median"), ["feature1", "feature2"]),
# #             ("cat", OneHotEncoder(handle_unknown="ignore"), ["feature3", "feature4"]),
# #         ]
# #     )

# #     # Crear un pipeline para entrenar el modelo
# #     model = Pipeline(steps=[
# #         ("preprocessor", preprocessor),
# #         ("classifier", RandomForestClassifier(n_estimators=100)),
# #     ])

# #     # Entrenar el modelo
# #     model.fit(X_train, y_train)

# #     return model

# # Función para hacer predicciones con el modelo
# def make_prediction(model, X):
#     return model.predict(X)

# # # Función para evaluar el modelo
# # def evaluate_model(model, X_test, y_test):
# #     y_pred = model.predict(X_test)
# #     accuracy = accuracy_score(y_test, y_pred)
# #     return accuracy

# # Función para guardar el modelo
# def save_model(model, filename):
#     joblib.dump(model, filename)

# # Función para cargar el modelo
# def load_model(filename):
#     return joblib.load(filename)

# # # Ruta para entrenar el modelo
# # @app.post("/train")
# # async def train_model_endpoint(model: Model):
# #     # Cargar los datos de entrenamiento
# #     X_train = pd.read_csv("data/train.csv")
# #     y_train = pd.read_csv("data/train_labels.csv")

# #     # Entrenar el modelo
# #     model = train_model(X_train, y_train)

# #     # Guardar el modelo
# #     save_model(model, "model.joblib")

# #     return {"message": "Modelo entrenado y guardado"}

# # Ruta para hacer predicciones
# @app.post("/predict")
# async def predict_endpoint(model: Model):
#     # Cargar el modelo entrenado
#     model = load_model("inference_pipeline.joblib")

#     # Cargar los datos de entrada
#     X = pd.DataFrame(model.features)

#     # Hacer predicciones
#     y_pred = make_prediction(model, X)

#     return {"predictions": y_pred}

# # # Ruta para evaluar el modelo
# # @app.post("/evaluate")
# # async def evaluate_endpoint(model: Model):
# #     # Cargar el modelo entrenado
# #     model = load_model("model.joblib")

# #     # Cargar los datos de evaluación
# #     X_test = pd.read_csv("data/test.csv")
# #     y_test = pd.read_csv("data/test_labels.csv")

# #     # Evaluar el modelo
# #     accuracy = evaluate_model(model, X_test, y_test)

# #     return {"accuracy": accuracy}

from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from joblib import load
import pandas as pd
import uvicorn

app = FastAPI()

class InputData(BaseModel):
    hotel: str
    lead_time: int
    arrival_date_year: int
    arrival_date_month: str
    arrival_date_week_number: int
    arrival_date_day_of_month: int
    stays_in_weekend_nights: int
    stays_in_week_nights: int
    adults: int
    children: int
    babies: int
    meal: str
    country: str
    market_segment: str
    distribution_channel: str
    is_repeated_guest: int
    previous_cancellations: int
    previous_bookings_not_canceled: int
    reserved_room_type: str
    assigned_room_type: str
    booking_changes: int
    deposit_type: str
    agent: str
    days_in_waiting_list: int
    customer_type: str
    adr: float
    required_car_parking_spaces: int
    total_of_special_requests: int
    

@app.get('/')
def index():
    return "home page"

@app.post("/predict")
async def predict(input_data: InputData):
    preprocesor_pipeline = load("../artifacts/preprocessor_pipeline.joblib")
    best_model_load = load("../artifacts/inference_pipeline.joblib")

    input_data_df = pd.DataFrame([input_data.model_dump()])
    
    # transform
    transformed_input = preprocesor_pipeline.transform(input_data_df)

    # predict
    try:
        prediction = best_model_load.predict(transformed_input)
        result = "no cancelled"
        if prediction[0] == 1:
            result = "is calcelled"
        
        return JSONResponse(content={"prediction": result})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
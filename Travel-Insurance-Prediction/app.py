import os
import pickle
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
import uvicorn
from pydantic import BaseModel

# Create an instance of the FastAPI class
app = FastAPI()

# Define the path to the main folder and the model file
MAIN_FOLDER = os.path.dirname(__file__)
MODEL_PATH = os.path.join(MAIN_FOLDER, "artifacts/model/model.pkl")

# Load the model from the specified directory with exception handling
try:
    with open(MODEL_PATH, "rb") as file:
        model = pickle.load(file)
except Exception as e:
    raise HTTPException(status_code=500, detail=f"Error loading the model: {e}")

# Define a Pydantic model to validate the input data
class AnswerDataInput(BaseModel):
    Age: int
    Employment_Type: int
    GraduateOrNot: int
    AnnualIncome: int
    FamilyMembers: int
    ChronicDiseases: int
    FrequentFlyer: int
    EverTravelledAbroad: int

# Define a root endpoint that returns a welcome message
@app.get("/")
async def root():
    return {"message": "Travel Insurance Prediction API"}

# Define an endpoint for making predictions
@app.post("/prediction")
def predict_satisfaction_flight(answer: AnswerDataInput):
    # Convert the input data to a JSON-compatible format
    answer_dict = jsonable_encoder(answer)

    # Convert the input data to a DataFrame
    single_instance = pd.DataFrame([answer_dict])

    # Make a prediction using the loaded model
    prediction = model.predict(single_instance)

    # Convert the prediction to an integer
    score = int(prediction[0])
    # Return the prediction as a JSON response
    return {"score": score}

# Run the API using Uvicorn if the script is executed directly
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)



# CORREGIR NO COINIDEN LOS NOMBRES DE LOS INPUTS
# ValueError: The feature names should match those that were passed during fit.
# Feature names unseen at fit time:
# - ChronicDisease
# - EmploymentType
# Feature names seen at fit time, yet now missing:
# - ChronicDiseases
# - Employment_Type

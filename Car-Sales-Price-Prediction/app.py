import gradio as gr
import pandas as pd
import pickle

# ----------------------------------------------------------
# Columns
COL_PATH = "./artifacts/categories_ohe.pkl"
try:
    with open(COL_PATH, "rb") as file:
        loaded_cat_ohe = pickle.load(file)
except Exception as e:
    print(f"Error loading columns: {e}")

# ----------------------------------------------------------
# Load the model
MODEL_PATH = "./artifacts/model.pkl"
try:
    with open(MODEL_PATH, "rb") as file:
        model = pickle.load(file)
except Exception as e:
    print(f"Error loading the model: {e}")

# ----------------------------------------------------------
# Define the params names
PARAMS_NAME = ["year", "fuel","seats","transmission","Region"]


# ----------------------------------------------------------
# Method to predict
def predict(*args):
    # Create a dictionary to hold the input features
    features_dict = {}

    # Populate the dictionary with feature names and corresponding values
    for index, feature_name in enumerate(PARAMS_NAME):
        features_dict[feature_name] = [args[index]]

    # Convert the dictionary to a DataFrame
    single_instance_df = pd.DataFrame.from_dict(features_dict)

    # One-hot encode the categorical features and align with training data
    single_instance_encoded = pd.get_dummies(single_instance_df).reindex(columns=loaded_cat_ohe).fillna(0)

    # Make a prediction using the preloaded model
    prediction_result = model.predict(single_instance_encoded)

    # Convert the prediction to an integer
    predicted_value = int(prediction_result[0])

    return predicted_value



# ----------------------------------------------------------
# UI APP
with gr.Blocks() as Gradio_App:
    gr.Markdown(
        """
        <div style="text-align: center">

        # <h1><font color="#004FBF" size=7>SALES PRICE OF USED CARS</font></h1>
        
        """
    )

    with gr.Row():
        with gr.Column():
            gr.Markdown(
                """
                ## Price Prediction
                """
                )

            fuel = gr.Radio(
                label="Fuel Type",
                choices=["Gasoline", "Diesel","LPG","Petrol"],
                value="Diesel"
                )

            year = gr.Slider(
                label="Year",
                minimum=1995,
                maximum=2020,
                step=5,
                randomize=True
                )
            
            seats = gr.Slider(
                label="Seats",
                minimum=2,
                maximum=8,
                step=1,
                randomize=True
                )
            
            transmision = gr.Radio(
                label="Transmision",
                choices=["Manual", "Automatic"],
                value="Manual"
                )

            Region = gr.Dropdown(
                label="Region",
                choices=["Central", "East","South","West"],
                multiselect=False,
                value="Central"
                )

        with gr.Column():
            gr.Markdown(
                """
                ## Prediction
                """
                )
            
            label = gr.Label(label="Price in Rupias")
            predict_btn = gr.Button(value="Predict")
            predict_btn.click(
                                predict,
                                inputs=[fuel,year, seats, transmision, Region],
                                outputs=[label]
                            )
            
    gr.Markdown(
        """
        <p style='text-align: center'>
            <a href='https://github.com/Ael-Dev/End-to-end-projects' target='_blank'>
                Github Projects
            </a>
        </p>
        """
    )

Gradio_App.launch()


# comand to deploy
# python app.py
# localhost
# http://localhost:7860


import streamlit as st
import requests
import json

# Set the API endpoint
API_ENDPOINT = "http://127.0.0.1:8000/predict"

# Create a Streamlit app
st.title("Hotel Reservation Prediction App")

# Create a sidebar
st.sidebar.title("Input Fields")

# Create input fields for the user
hotel = st.sidebar.text_input("Hotel")
lead_time = st.sidebar.number_input("Lead Time", value=0)
arrival_date_year = st.sidebar.number_input("Arrival Date Year", value=0)
arrival_date_month = st.sidebar.selectbox("Arrival Date Month", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
arrival_date_week_number = st.sidebar.number_input("Arrival Date Week Number", value=0)
arrival_date_day_of_month = st.sidebar.number_input("Arrival Date Day of Month", value=0)
stays_in_weekend_nights = st.sidebar.number_input("Stays in Weekend Nights", value=0)
stays_in_week_nights = st.sidebar.number_input("Stays in Week Nights", value=0)
adults = st.sidebar.number_input("Adults", value=0)
children = st.sidebar.number_input("Children", value=0)
babies = st.sidebar.number_input("Babies", value=0)
meal = st.sidebar.selectbox("Meal", ["BB", "HB", "FB"])
country = st.sidebar.selectbox("Country", ["PRT", "USA", "CAN"])
market_segment = st.sidebar.selectbox("Market Segment", ["Direct", "Indirect"])
distribution_channel = st.sidebar.selectbox("Distribution Channel", ["Direct", "Indirect"])
is_repeated_guest = st.sidebar.number_input("Is Repeated Guest", value=0)
previous_cancellations = st.sidebar.number_input("Previous Cancellations", value=0)
previous_bookings_not_canceled = st.sidebar.number_input("Previous Bookings Not Canceled", value=0)
reserved_room_type = st.sidebar.selectbox("Reserved Room Type", ["C", "A", "B"])
assigned_room_type = st.sidebar.selectbox("Assigned Room Type", ["C", "A", "B"])
booking_changes = st.sidebar.number_input("Booking Changes", value=0)
deposit_type = st.sidebar.selectbox("Deposit Type", ["No Deposit", "Deposit"])
agent = st.sidebar.text_input("Agent")
days_in_waiting_list = st.sidebar.number_input("Days in Waiting List", value=0)
customer_type = st.sidebar.selectbox("Customer Type", ["Transient", "Contract"])
adr = st.sidebar.number_input("ADR", value=0.0)
required_car_parking_spaces = st.sidebar.number_input("Required Car Parking Spaces", value=0)
total_of_special_requests = st.sidebar.number_input("Total of Special Requests", value=0)

# Create a button to submit the input
if st.sidebar.button("Predict"):
    # Create a dictionary to hold the input data
    input_data = {
        "hotel": hotel,
        "lead_time": lead_time,
        "arrival_date_year": arrival_date_year,
        "arrival_date_month": arrival_date_month,
        "arrival_date_week_number": arrival_date_week_number,
        "arrival_date_day_of_month": arrival_date_day_of_month,
        "stays_in_weekend_nights": stays_in_weekend_nights,
        "stays_in_week_nights": stays_in_week_nights,
        "adults": adults,
        "children": children,
        "babies": babies,
        "meal": meal,
        "country": country,
        "market_segment": market_segment,
        "distribution_channel": distribution_channel,
        "is_repeated_guest": is_repeated_guest,
        "previous_cancellations": previous_cancellations,
        "previous_bookings_not_canceled": previous_bookings_not_canceled,
        "reserved_room_type": reserved_room_type,
        "assigned_room_type": assigned_room_type,
        "booking_changes": booking_changes,
        "deposit_type": deposit_type,
        "agent": agent,
        "days_in_waiting_list": days_in_waiting_list,
        "customer_type": customer_type,
        "adr": adr,
        "required_car_parking_spaces": required_car_parking_spaces,
        "total_of_special_requests": total_of_special_requests
    }

    # Convert the input data to JSON
    input_json = json.dumps(input_data)

    # Send a POST request to the API with the input data
    response = requests.post(API_ENDPOINT, data=input_json)

    # Display the prediction result
    if response.status_code == 200:
        prediction = response.json()["prediction"]
        st.write(f"Prediction: {prediction}")
    else:
        st.write("Error: Unable to get prediction.")
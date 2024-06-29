import streamlit as st
import pandas as pd
import joblib
import numpy as np
from datetime import datetime

# Define a SessionState class for managing state across Streamlit reruns
class SessionState:
    def __init__(self):
        self.all_data = pd.DataFrame(columns=['DATE', 'ALLSKY_KT', 'T2M', 'TS', 'PRECTOTCORR', 'PS', 'WS10M', 'Predictions'])
        self.csv_data = pd.DataFrame(columns=['DATE', 'ALLSKY_KT', 'T2M', 'TS', 'PRECTOTCORR', 'PS', 'WS10M'])
        self.selected_date_data = {}
        self.auto_fill_message_shown = False  # Add a flag to track if the message has been shown

# Initialize state
if 'session_state' not in st.session_state:
    st.session_state.session_state = SessionState()
state = st.session_state.session_state

# Function to load the machine learning model
def load_model(model_path):
    model = joblib.load(model_path)
    return model

# Function to perform prediction
def predict(model, input_features):
    predictions = model.predict(input_features)
    return predictions

# Function to display the prediction interface
def app():
    st.title("Upwelling Prediction")

    # Load the model
    model_path = 'Dashboard/data/model_fix.pkl'  # Replace with the correct path to your model
    model = load_model(model_path)

    # Load data from data.csv
    try:
        state.csv_data = pd.read_csv('Dashboard/data/data.csv')
        state.csv_data['DATE'] = pd.to_datetime(state.csv_data['DATE'], format='%d/%m/%Y')
        state.csv_data['DATE'] = state.csv_data['DATE'].dt.date  # Convert to date only (no time component)
        st.write("CSV Data Loaded Successfully")
    except Exception as e:
        st.error(f"Error loading data.csv: {e}")
        return

    # Sidebar inputs for selecting date range
    date_range = st.date_input('Select Date Range', [pd.to_datetime('today').date(), pd.to_datetime('today').date()])
    if len(date_range) != 2:
        st.error("Please select a valid date range.")
        return
    start_date, end_date = date_range
    selected_dates = pd.date_range(start=start_date, end=end_date).date

    results = []
    input_data = []

    for selected_date in selected_dates:
        selected_date_str = selected_date.strftime('%Y-%m-%d')

        # Check if data exists for selected date and auto-fill inputs
        if not state.csv_data.empty and selected_date in state.csv_data['DATE'].values:
            row_data = state.csv_data[state.csv_data['DATE'] == selected_date].iloc[0]
            allsky_kt = row_data['ALLSKY_KT']
            t2m = row_data['T2M']
            ts = row_data['TS']
            prectotcorr = row_data['PRECTOTCORR']
            ps = row_data['PS']
            ws10m = row_data['WS10M']
            if not state.auto_fill_message_shown:
                st.success("Data found, auto-filled the fields.")
                state.auto_fill_message_shown = True
        else:
            st.warning(f"Data not found for {selected_date_str}. Please input the values manually.")
            allsky_kt = st.number_input(f'ALLSKY_KT for {selected_date_str}', value=0.00)
            t2m = st.number_input(f'T2M for {selected_date_str}', value=0.00)
            ts = st.number_input(f'TS for {selected_date_str}', value=0.00)
            prectotcorr = st.number_input(f'PRECTOTCORR for {selected_date_str}', value=0.00)
            ps = st.number_input(f'PS for {selected_date_str}', value=0.00)
            ws10m = st.number_input(f'WS10M for {selected_date_str}', value=0.00)

        input_data.append({
            'DATE': selected_date_str,
            'ALLSKY_KT': float(allsky_kt),
            'T2M': float(t2m),
            'TS': float(ts),
            'PRECTOTCORR': float(prectotcorr),
            'PS': float(ps),
            'WS10M': float(ws10m)
        })

    # Display prediction result
    if st.button("Predict Upwelling"):
        # Clear previous predictions
        state.all_data = pd.DataFrame(columns=['DATE', 'ALLSKY_KT', 'T2M', 'TS', 'PRECTOTCORR', 'PS', 'WS10M', 'Predictions'])
        
        for data in input_data:
            try:
                input_features = [[data['ALLSKY_KT'], data['T2M'], data['TS'], data['WS10M'], data['PRECTOTCORR'], data['PS']]]
                input_array = np.array(input_features)
                hasil_prediksi = predict(model, input_array)

                # Store prediction result and input data in state or any storage mechanism
                new_data = {
                    'DATE': [data['DATE']],
                    'ALLSKY_KT': [data['ALLSKY_KT']],
                    'T2M': [data['T2M']],
                    'TS': [data['TS']],
                    'PRECTOTCORR': [data['PRECTOTCORR']],
                    'PS': [data['PS']],
                    'WS10M': [data['WS10M']],
                    'Predictions': [hasil_prediksi]
                }

                state.all_data = pd.concat([state.all_data, pd.DataFrame(new_data)], ignore_index=True)
                results.append(new_data)
            except ValueError:
                st.warning("Please enter valid numeric values.")

    if results:
        st.success("Predictions completed for the selected date range.")

    # Display all_data table
    state.all_data = state.all_data.sort_values(by=['DATE'], ascending=True)
    state.all_data = state.all_data.reset_index(drop=True)
    st.table(state.all_data)

    # Download button for CSV
    if not state.all_data.empty:
        csv_data = state.all_data.to_csv(index=False)
        st.download_button(label="Download CSV", data=csv_data, file_name='predicted_results.csv', key='download_button')

    st.text("This tool predicts upwelling potential based on various weather parameters. Use the input fields to enter the weather data, and click 'Predict Upwelling' to see the results.")

# Ensure the script can be run directly or imported as a module
if __name__ == "__main__":
    app()

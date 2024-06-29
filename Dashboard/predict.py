import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Define a SessionState class for managing state across Streamlit reruns
class SessionState:
    def __init__(self):
        self.all_data = pd.DataFrame(columns=['DATE', 'ALLSKY_KT', 'T2M', 'TS', 'PRECTOTCORR', 'PS', 'WS10M', 'Predictions'])
        self.csv_data = pd.DataFrame(columns=['DATE', 'ALLSKY_KT', 'T2M', 'TS', 'PRECTOTCORR', 'PS', 'WS10M'])
        self.selected_date_data = {}

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
        st.write("CSV Data Loaded Successfully")
    except Exception as e:
        st.error(f"Error loading data.csv: {e}")
        return

    # Sidebar inputs for selecting date
    selected_date = st.date_input('Select Date', pd.to_datetime('today').date())
    selected_date_str = selected_date.strftime('%Y-%m-%d')

    # Check if data exists for selected date and auto-fill inputs
    if not state.csv_data.empty and selected_date in state.csv_data['DATE'].dt.date.values:
        row_data = state.csv_data[state.csv_data['DATE'].dt.date == selected_date].iloc[0]
        allsky_kt = row_data['ALLSKY_KT']
        t2m = row_data['T2M']
        ts = row_data['TS']
        prectotcorr = row_data['PRECTOTCORR']
        ps = row_data['PS']
        ws10m = row_data['WS10M']
        st.success("Data found for the selected date and auto-filled the fields.")
    else:
        st.warning("Data not found for the selected date. Please input the values manually.")
        allsky_kt = st.number_input('ALLSKY_KT', value=0.00)
        t2m = st.number_input('T2M', value=0.00)
        ts = st.number_input('TS', value=0.00)
        prectotcorr = st.number_input('PRECTOTCORR', value=0.00)
        ps = st.number_input('PS', value=0.00)
        ws10m = st.number_input('WS10M', value=0.00)

    # Display prediction result
    hasil_prediksi = ""

    if st.button("Predict Upwelling"):
        try:
            input_features = [[float(allsky_kt), float(t2m), float(ts), float(ws10m), float(prectotcorr), float(ps)]]
            input_array = np.array(input_features)
            st.write(f"Input Array: {input_array}")  # Display input array for debugging
            hasil_prediksi = predict(model, input_array)
            st.write(f"Raw Prediction: {hasil_prediksi}")  # Display raw prediction for debugging

            # Store prediction result and input data in state or any storage mechanism
            new_data = {
                'DATE': [selected_date_str],
                'ALLSKY_KT': [float(allsky_kt)],
                'T2M': [float(t2m)],
                'TS': [float(ts)],
                'PRECTOTCORR': [float(prectotcorr)],
                'PS': [float(ps)],
                'WS10M': [float(ws10m)],
                'Predictions': [hasil_prediksi]
            }

            state.all_data = pd.concat([state.all_data, pd.DataFrame(new_data)], ignore_index=True)

        except ValueError:
            st.warning("Please enter valid numeric values.")
            hasil_prediksi = ""

    st.success(hasil_prediksi)

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

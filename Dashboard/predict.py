import streamlit as st
import pandas as pd
import joblib
import numpy as np
from datetime import datetime

# Function to apply custom HTML style to the entire row based on the Prediksi column
def render_styled_table(dataframe):
    def highlight_row(row):
        prediction = row['Prediksi']
        if prediction == "BERPOTENSI UPWELLING":
            return ['background-color: #FF7F7F; color: black'] * len(row)
        elif prediction == "TIDAK BERPOTENSI UPWELLING":
            return ['background-color: lightblue; color: black'] * len(row)
        return [''] * len(row)
    
    styled_table = dataframe.style.apply(highlight_row, axis=1)
    return styled_table

# Define a SessionState class for managing state across Streamlit reruns
class SessionState:
    def __init__(self):
        self.all_data = pd.DataFrame(columns=['DATE', 'Indeks Kejernihan Langit', 'Suhu Pada Ketinggian 2 Meter', 'Curah Hujan', 'Tekanan Permukaan', 'Kecepatan Angin', 'Prediksi'])
        self.csv_data = pd.DataFrame(columns=['DATE', 'Indeks Kejernihan Langit', 'Suhu Pada Ketinggian 2 Meter', 'Curah Hujan', 'Tekanan Permukaan', 'Kecepatan Angin'])
        self.auto_fill_message_shown = True  # Flag untuk menampilkan pesan auto-fill

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
    st.write("#### Pastikan Menekan Tombol Predict Upwelling Saat Memprediksi")

    # Load the model
    model_path = "Dashboard/data/model_klasifikasi.pkl"
    model = load_model(model_path)

    # Load data from data.csv
    try:
        state.csv_data = pd.read_csv('Dashboard/data/Data_Hasil_Forcast_2_Tahun_(2024-2025).csv')
        state.csv_data['DATE'] = pd.to_datetime(state.csv_data['DATE'], format='%d/%m/%Y')
        state.csv_data['DATE'] = state.csv_data['DATE'].dt.date  # Convert to date only (no time component)
    except Exception as e:
        st.error(f"Error loading data.csv: {e}")
        return

    # Rename columns in csv_data
    state.csv_data.rename(columns={
        'ALLSKY_KT': 'Indeks Kejernihan Langit',
        'T2M': 'Suhu Pada Ketinggian 2 Meter',
        'PRECTOTCORR': 'Curah Hujan',
        'PS': 'Tekanan Permukaan',
        'WS10M': 'Kecepatan Angin'
    }, inplace=True)

    # Sidebar inputs for selecting date range
    date_range = st.date_input('Select Date Range', [])
    if len(date_range) != 2:
        st.error("Please select date range.")
        return
    start_date, end_date = date_range
    selected_dates = pd.date_range(start=start_date, end=end_date).date

    results = []
    input_data = []

    for selected_date in selected_dates:
        selected_date_str = selected_date.strftime('%d/%m/%Y')  # Change the format to dd/mm/yyyy

        # Check if data exists for selected date and auto-fill inputs
        if not state.csv_data.empty and selected_date in state.csv_data['DATE'].values:
            row_data = state.csv_data[state.csv_data['DATE'] == selected_date].iloc[0]
            allsky_kt = row_data['Indeks Kejernihan Langit']
            t2m = row_data['Suhu Pada Ketinggian 2 Meter']
            prectotcorr = row_data['Curah Hujan']
            ps = row_data['Tekanan Permukaan']
            ws10m = row_data['Kecepatan Angin']
            if not state.auto_fill_message_shown:
                st.success("Data found, auto-filled the fields.")
                state.auto_fill_message_shown = True
        else:
            st.warning(f"Data not found for {selected_date_str}. Please input the values manually.")
            allsky_kt = st.number_input(f'Indeks Kejernihan Langit for {selected_date_str}', value=0.00)
            t2m = st.number_input(f'Suhu Pada Ketinggian 2 Meter for {selected_date_str}', value=0.00)
            prectotcorr = st.number_input(f'Curah Hujan for {selected_date_str}', value=0.00)
            ps = st.number_input(f'Tekanan Permukaan for {selected_date_str}', value=0.00)
            ws10m = st.number_input(f'Kecepatan Angin for {selected_date_str}', value=0.00)

        input_data.append({
            'DATE': selected_date_str,
            'Indeks Kejernihan Langit': float(allsky_kt),
            'Suhu Pada Ketinggian 2 Meter': float(t2m),
            'Curah Hujan': float(prectotcorr),
            'Tekanan Permukaan': float(ps),
            'Kecepatan Angin': float(ws10m)
        })

    # Display prediction result
    if st.button("Predict Upwelling"):
        # Clear previous predictions
        state.all_data = pd.DataFrame(columns=['DATE', 'Indeks Kejernihan Langit', 'Suhu Pada Ketinggian 2 Meter', 'Curah Hujan', 'Tekanan Permukaan', 'Kecepatan Angin', 'Prediksi'])
        
        for data in input_data:
            try:
                input_features = [[data['Indeks Kejernihan Langit'], data['Suhu Pada Ketinggian 2 Meter'], data['Kecepatan Angin'], data['Curah Hujan'], data['Tekanan Permukaan']]]
                input_array = np.array(input_features)
                hasil_prediksi = predict(model, input_array)

                # Store prediction result and input data in state or any storage mechanism
                new_data = {
                    'DATE': [data['DATE']],
                    'Indeks Kejernihan Langit': [data['Indeks Kejernihan Langit']],
                    'Suhu Pada Ketinggian 2 Meter': [data['Suhu Pada Ketinggian 2 Meter']],
                    'Curah Hujan': [data['Curah Hujan']],
                    'Tekanan Permukaan': [data['Tekanan Permukaan']],
                    'Kecepatan Angin': [data['Kecepatan Angin']],
                    'Prediksi': hasil_prediksi[0]  # Ambil prediksi sebagai string, bukan list
                }

                state.all_data = pd.concat([state.all_data, pd.DataFrame(new_data)], ignore_index=True)
                results.append(new_data)
            except ValueError:
                st.warning("Please enter valid numeric values.")

    if results:
        st.success("Predictions completed for the selected date range.")

    # Display all_data table
    # Convert DATE back to datetime for sorting
    state.all_data['DATE'] = pd.to_datetime(state.all_data['DATE'], format='%d/%m/%Y')

    # Sort by DATE in ascending order
    state.all_data = state.all_data.sort_values(by=['DATE'], ascending=True)

    # Convert back to string format after sorting
    state.all_data['DATE'] = state.all_data['DATE'].dt.strftime('%d/%m/%Y')

    # Format numeric columns to display float with two decimal places
    formatted_data = state.all_data.copy()
    numeric_columns = ['Indeks Kejernihan Langit', 'Suhu Pada Ketinggian 2 Meter', 'Curah Hujan', 'Tekanan Permukaan', 'Kecepatan Angin']

    for col in numeric_columns:
        formatted_data[col] = formatted_data[col].apply(lambda x: f"{x:.2f}")

    # Render the styled table using custom styling
    styled_table = render_styled_table(formatted_data)
    
    st.write(styled_table.to_html(), unsafe_allow_html=True)

    # Download button for CSV
    if not state.all_data.empty:
        csv_data = state.all_data.to_csv(index=False)
        st.download_button(label="Download CSV", data=csv_data, file_name='predicted_results.csv', key='download_button')

    st.text("This tool predicts upwelling potential based on various weather parameters. Use the input fields to enter the weather data, and click 'Predict Upwelling' to see the results.")

# Ensure the script can be run directly or imported as a module
if __name__ == "__main__":
    app()

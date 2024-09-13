import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os
from web_function import preprocess_dataframe, load_data  # Assuming these are your custom functions

# Descriptive names for the climate indicators in both languages
indicator_names_en = {
    'ALLSKY_KT': 'Sky Insolation Clarity Index',
    'T2M': 'Average Air Temperature at 2 Meters Height (°C)',
    'PRECTOTCORR': 'Rainfall (mm)',
    'PS': 'Average Surface Pressure at the Earth\'s Surface (kPa)',
    'WS10M': 'Average Wind Speed at 10 Meters Height (m/s)'
}

indicator_names_id = {
    'ALLSKY_KT': 'Indeks Kejernihan Langit',
    'T2M': 'Suhu Udara Rata-Rata pada Ketinggian 2 Meter (°C)',
    'PRECTOTCORR': 'Curah Hujan (mm)',
    'PS': 'Tekanan Permukaan Rata-Rata (kPa)',
    'WS10M': 'Kecepatan Angin Rata-Rata pada Ketinggian 10 Meter (m/s)'
}

def plot_climate_indicator(df, indicator, lang):
    # Ensure the index is set as date time, if not already done
    if not pd.api.types.is_datetime64_any_dtype(df.index):
        df.index = pd.to_datetime(df.index)
    
    # Ensure there are no missing values
    if df[indicator].isnull().all():
        st.error(f"No data available for {indicator}")
        return None

    indicator_names = indicator_names_en if lang == "English" else indicator_names_id

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df[indicator], mode='lines', name=indicator))
    fig.update_layout(title=indicator_names[indicator],
                      xaxis_title='Date' if lang == 'English' else 'Tanggal',
                      yaxis_title=indicator_names[indicator],
                      template='plotly_dark')
    return fig

def app():
    # Set default language as "Bahasa Indonesia"
    lang = st.selectbox("Pilih Bahasa / Select Language", ["Bahasa Indonesia", "English"])

    # Add logging for debugging purposes
    st.write(f"Selected language: {lang}")

    # Verify file existence and load the dataset
    file_path = "Dashboard/data/HASIL_CLUSTERING.csv"
    
    if not os.path.exists(file_path):
        st.error(f"Error: File '{file_path}' not found.")
        return

    try:
        # Load Dataset
        df = load_data(file_path)
        st.write("Data Loaded Successfully")
        st.write(df.head())  # Display first few rows to verify the data
    except Exception as e:
        st.error("Error loading data")
        st.write(e)
        return

    # Check the structure of the dataframe
    st.write("Dataframe Info:")
    st.write(df.info())

    # Create two separate dataframes for table and plotting
    df_table = df.copy()
    df_plot = df.copy()

    # Convert date to string for display in table
    df_table['DATE_STR'] = df_table['DATE'].dt.strftime('%d-%m-%Y')
    df_table.set_index('DATE_STR', inplace=True)

    # Filter based on date range
    min_date = pd.to_datetime("2017-01-01")
    max_date = pd.to_datetime("2023-12-31")
    
    try:
        date_range = st.date_input("Pilih Rentang Waktu" if lang == "Bahasa Indonesia" else "Select Date Range", 
                                   [min_date, max_date], 
                                   min_value=min_date, max_value=max_date, key="date_range")
    except Exception as e:
        st.error("Error processing date range")
        st.write(e)
        return
    
    # Extract start and end date
    start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
    df_table = df_table[(df_table['DATE'] >= start_date) & (df_table['DATE'] <= end_date)]
    df_plot = df_plot[(df_plot['DATE'] >= start_date) & (df_plot['DATE'] <= end_date)]

    # Display historical data
    try:
        st.write(df_table[['ALLSKY_KT', 'T2M', 'PRECTOTCORR', 'PS', 'WS10M', 'Status']])
    except KeyError as e:
        st.error(f"Error: One of the required columns is missing - {e}")
        return

    # Column descriptions
    column_header = 'Deskripsi Kolom dari Tabel' if lang == 'Bahasa Indonesia' else 'Column descriptions of the table'
    column_description = """
        1. DATE         : Tanggal indikator iklim
        2. ALLSKY_KT    : Indeks kejernihan insolasi langit
        3. T2M          : Suhu udara rata-rata pada ketinggian 2 meter (°C)
        4. PRECTOTCORR  : Curah hujan (mm)
        5. PS           : Tekanan permukaan rata-rata (kPa)
        6. WS10M        : Kecepatan angin rata-rata pada ketinggian 10 meter (m/s)
        7. Status       : Potensi Kejadian Upwelling
    """ if lang == "Bahasa Indonesia" else """
        1. DATE             : Date of the climate indicator
        2. ALLSKY_KT        : Sky insolation clarity index
        3. T2M              : Average air temperature at 2 meters height (°C)
        4. PRECTOTCORR      : Rainfall (mm)
        5. PS               : Average surface pressure (kPa)
        6. WS10M            : Average wind speed at 10 meters height (m/s)
        7. Status           : Potential Upwelling Event
    """

    st.header(column_header)
    st.text(column_description)

    # Plot Upwelling Events vs Non-Upwelling Events with markers and specific colors
    tampilan_header = 'Tampilan Data Historis' if lang == 'Bahasa Indonesia' else 'Historical Data Display'
    st.header(tampilan_header)
    fig = go.Figure()

    for status, color in zip(df_plot['Status'].unique(), ['red', 'green']):
        filtered_df = df_plot[df_plot['Status'] == status]
        fig.add_trace(go.Scatter(x=filtered_df['DATE'], y=filtered_df['PRECTOTCORR'],
                                 mode='markers', marker=dict(color=color), name=status))

    fig.update_layout(title='Potential Upwelling vs Non-Upwelling Events' if lang == "English" 
                      else 'Potensi Upwelling vs Tidak Berpotensi Upwelling',
                      xaxis_title='Date' if lang == "English" else 'Tanggal',
                      yaxis_title='Rainfall (PRECTOTCORR)' if lang == "English" else 'Curah Hujan (PRECTOTCORR)',
                      template='plotly_dark')
    st.plotly_chart(fig, use_container_width=True)

    # Climate Indicator Selection
    st.header("Select Climate Indicators" if lang == "English" else "Pilih Indikator Iklim")
    with st.expander("Choose Climate Indicators to Display:" if lang == "English" else "Pilih Indikator Iklim yang Ingin Ditampilkan:"):
        # Checkbox to select all indicators
        select_all = st.checkbox('Select All Indicators' if lang == "English" else 'Tampilkan Semua Indikator')
        
        # Set individual checkboxes depending on the "Select All" checkbox
        allsky_kt = st.checkbox('ALLSKY_KT' if lang == "English" else 'ALLSKY_KT - Indeks Kejernihan Langit', value=select_all)
        t2m = st.checkbox('T2M' if lang == "English" else 'T2M - Suhu Udara', value=select_all)
        prectotcorr = st.checkbox('PRECTOTCORR' if lang == "English" else 'PRECTOTCORR - Curah Hujan', value=select_all)
        ps = st.checkbox('PS' if lang == "English" else 'PS - Tekanan Permukaan', value=select_all)
        ws10m = st.checkbox('WS10M' if lang == "English" else 'WS10M - Kecepatan Angin', value=select_all)

    # Plot selected indicators
    if allsky_kt:
        fig_indicator = plot_climate_indicator(df_plot, 'ALLSKY_KT', lang)
        st.plotly_chart(fig_indicator, use_container_width=True)

    if t2m:
        fig_indicator = plot_climate_indicator(df_plot, 'T2M', lang)
        st.plotly_chart(fig_indicator, use_container_width=True)

    if prectotcorr:
        fig_indicator = plot_climate_indicator(df_plot, 'PRECTOTCORR', lang)
        st.plotly_chart(fig_indicator, use_container_width=True)

    if ps:
        fig_indicator = plot_climate_indicator(df_plot, 'PS', lang)
        st.plotly_chart(fig_indicator, use_container_width=True)

    if ws10m:
        fig_indicator = plot_climate_indicator(df_plot, 'WS10M', lang)
        st.plotly_chart(fig_indicator, use_container_width=True)

if __name__ == "__main__":
    app()

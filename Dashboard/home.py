import streamlit as st
import pandas as pd
import plotly.graph_objects as go
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
    # Select indicator name based on chosen language
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

    if lang == "Bahasa Indonesia":
        st.title("Dashboard Pemantauan dan Prediksi Upwelling Berbasis Indikator Iklim di Danau Laut Tawar")
        st.markdown("""
            Selamat datang di Dashboard Pemantauan dan Prediksi Upwelling berbasis indikator iklim Danau Laut Tawar!
            Dengan menggabungkan data dalam setahun, potensi produksi ikan di Danau Laut Tawar dapat mencapai 196 ton. 
            Namun, perubahan iklim yang tidak menentu mengganggu kestabilan produksi ikan di Danau Laut Tawar.
        """)
        column_header = 'Deskripsi Kolom dari Tabel'
        tampilan_header = 'Tampilan Data Historis'
        column_description = """
        1. DATE         : Tanggal indikator iklim
        2. ALLSKY_KT    : Indeks kejernihan insolasi langit
        3. T2M          : Suhu udara rata-rata pada ketinggian 2 meter (°C)
        4. PRECTOTCORR  : Curah hujan (mm)
        5. PS           : Tekanan permukaan rata-rata (kPa)
        6. WS10M        : Kecepatan angin rata-rata pada ketinggian 10 meter (m/s)
        7. Status       : Potensi Kejadian Upwelling
        """
    else:
        st.title("Climate Indicator-Based Upwelling Monitoring and Prediction Dashboard in Danau Laut Tawar")
        st.markdown("""
            Welcome to the Lake Laut Tawar climate indicator-based Upwelling Monitoring and Prediction Dashboard!
            By combining the data in a year, the potential fish production in Danau Laut Tawar can reach 196 tons.
            However, erratic climate change is destabilizing fish production in Danau Laut Tawar.
        """)
        column_header = 'Column descriptions of the table'
        tampilan_header = 'Historical Data Display'
        column_description = """
        1. DATE             : Date of the climate indicator
        2. ALLSKY_KT        : Sky insolation clarity index
        3. T2M              : Average air temperature at 2 meters height (°C)
        4. PRECTOTCORR      : Rainfall (mm)
        5. PS               : Average surface pressure (kPa)
        6. WS10M            : Average wind speed at 10 meters height (m/s)
        7. Status           : Potential Upwelling Event
        """

    # Load Dataset
    df = load_data("Dashboard/data/HASIL_CLUSTERING.csv")
    df['DATE'] = pd.to_datetime(df['DATE'])
    
    # Create two separate dataframes for table and plotting
    df_table = df.copy()
    df_plot = df.copy()

    # Convert date to string for display in table
    df_table['DATE_STR'] = df_table['DATE'].dt.strftime('%d-%m-%Y')
    df_table.set_index('DATE_STR', inplace=True)

    # Filter based on date range
    min_date = pd.to_datetime("2017-01-01")
    max_date = pd.to_datetime("2023-12-31")
    date_range = st.date_input("Pilih Rentang Waktu" if lang == "Bahasa Indonesia" else "Select Date Range", 
                               [min_date, max_date], 
                               min_value=min_date, max_value=max_date, key="date_range")
    
    start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
    df_table = df_table[(df_table['DATE'] >= start_date) & (df_table['DATE'] <= end_date)]
    df_plot = df_plot[(df_plot['DATE'] >= start_date) & (df_plot['DATE'] <= end_date)]

    # Display historical data
    st.write(df_table[['ALLSKY_KT', 'T2M', 'PRECTOTCORR', 'PS', 'WS10M', 'Status']])

    # Column descriptions
    st.header(column_header)
    st.text(column_description)

    # Plot Upwelling Events vs Non-Upwelling Events with markers and specific colors
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
        st.markdown('This graph displays the sky clarity index values from 2017 to 2024. This index measures how clear or bright the sky is, with values ranging from 0.1 (very cloudy) to 0.7 (very bright). Changes in this index show daily variations in sky clarity, which can be affected by factors such as clouds or pollution.' if lang == "English" else 'Grafik ini menampilkan nilai indeks kejernihan langit dari 2017 hingga 2024. Indeks ini mengukur seberapa jernih atau cerah langit, dengan nilai berkisar antara 0,1 (sangat keruh) hingga 0,7 (sangat cerah). Perubahan indeks ini menunjukkan variasi harian dalam kejernihan langit, yang bisa dipengaruhi oleh faktor-faktor seperti awan atau polusi.')

    if t2m:
        fig_indicator = plot_climate_indicator(df_plot, 'T2M', lang)
        st.plotly_chart(fig_indicator, use_container_width=True)
        st.markdown('This graph illustrates the change in average air temperature at 2 meters above ground level, over the period 2017 to 2024. Temperatures range from 17°C to 22°C. The graph shows a typical seasonal pattern, with regular increases and decreases in temperature over time.' if lang == "English" else 'Grafik ini menggambarkan perubahan suhu rata-rata udara di ketinggian 2 meter dari permukaan tanah, selama periode 2017 hingga 2024. Suhu berkisar antara 17°C hingga 22°C. Grafik ini menunjukkan pola musiman yang khas, dengan kenaikan dan penurunan suhu yang teratur seiring berjalannya waktu.')

    if prectotcorr:
        fig_indicator = plot_climate_indicator(df_plot, 'PRECTOTCORR', lang)
        st.plotly_chart(fig_indicator, use_container_width=True)
        st.markdown('This graph shows the changes in rainfall amounts from 2017 to 2024. Rainfall amounts are measured in millimeters (mm), with considerable variation each year. Some periods show high rainfall, particularly at the end of the data in 2024, which may signal heavy rainfall events or an intense rainy season.' if lang == "English" else 'Grafik ini menunjukkan perubahan jumlah curah hujan dari tahun 2017 hingga 2024. Jumlah curah hujan diukur dalam milimeter (mm), dengan variasi yang cukup besar setiap tahunnya. Beberapa periode menunjukkan curah hujan yang tinggi, khususnya pada akhir data di tahun 2024, yang mungkin menandakan kejadian hujan lebat atau musim hujan intens.')

    if ps:
        fig_indicator = plot_climate_indicator(df_plot, 'PS', lang)
        st.plotly_chart(fig_indicator, use_container_width=True)
        st.markdown('This graph shows the average surface atmospheric pressure measured in kilopascals (kPa), from 2017 to 2024. The atmospheric pressure ranges from 87.6 to 88.2 kPa. The changes seen indicate variations in atmospheric pressure, which can be influenced by changes in weather or air pressure systems.' if lang == "English" else 'Grafik ini menunjukkan tekanan atmosfer permukaan rata-rata yang diukur dalam kilopascal (kPa), dari tahun 2017 hingga 2024. Tekanan atmosfer berkisar antara 87,6 hingga 88,2 kPa. Perubahan yang terlihat menunjukkan adanya variasi tekanan atmosfer, yang dapat dipengaruhi oleh perubahan cuaca atau sistem tekanan udara.')

    if ws10m:
        fig_indicator = plot_climate_indicator(df_plot, 'WS10M', lang)
        st.plotly_chart(fig_indicator, use_container_width=True)
        st.markdown('This graph shows the change in average wind speed at a height of 10 meters from the ground, from 2017 to 2024. Wind speeds range from 0.5 meters per second to 2.5 meters per second. The fluctuations in this graph show variations in wind speed, with some periods recording higher wind speeds.' if lang == "English" else 'Grafik ini memperlihatkan perubahan kecepatan angin rata-rata pada ketinggian 10 meter dari permukaan tanah, dari 2017 hingga 2024. Kecepatan angin berkisar antara 0,5 meter per detik hingga 2,5 meter per detik. Fluktuasi dalam grafik ini menunjukkan variasi dalam kecepatan angin, dengan beberapa periode yang mencatat kecepatan angin yang lebih tinggi.', unsafe_allow_html=True)

if __name__ == "__main__":
    app()

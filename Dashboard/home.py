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

def plot_rainfall_line(df):
    fig = go.Figure()
    for event_type in df['Status'].unique():
        event_data = df[df['Status'] == event_type]
        fig.add_trace(go.Scatter(x=event_data.index, y=event_data['PRECTOTCORR'],
                                 mode='lines', name=event_type))
    fig.update_layout(title='Curah Hujan Rata-Rata dari Waktu ke Waktu',
                      xaxis_title='Tanggal',
                      yaxis_title='Curah Hujan (PRECTOTCORR)',
                      template='plotly_dark')
    return fig

def plot_climate_indicator(df, indicator, lang):
    # Pilih nama indikator berdasarkan bahasa yang dipilih
    indicator_names = indicator_names_en if lang == "English" else indicator_names_id

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df[indicator], mode='lines', name=indicator))
    fig.update_layout(title=indicator_names[indicator],
                      xaxis_title='Tanggal',
                      yaxis_title=indicator_names[indicator],
                      template='plotly_dark')
    return fig

def app():
    # Set Bahasa default sebagai "Bahasa Indonesia"
    lang = st.selectbox("Pilih Bahasa / Select Language", ["Bahasa Indonesia", "English"])

    if lang == "Bahasa Indonesia":
        # Konten dalam Bahasa Indonesia
        st.title("Dashboard Pemantauan dan Prediksi Upwelling Berbasis Indikator Iklim di Danau Laut Tawar")
        st.markdown("""
            Selamat datang di Dashboard Pemantauan dan Prediksi Upwelling berbasis indikator iklim Danau Laut Tawar! 
            Masyarakat setempat memanfaatkan danau ini sebagai salah satu sumber mata pencaharian utama. 
            Dengan menggabungkan data dalam setahun, potensi produksi ikan di Danau Laut Tawar dapat mencapai 196 ton. 
            Angka ini cukup fantastis dan menunjukkan betapa pentingnya peran Danau Laut Tawar dalam menyokong ekonomi lokal serta menyediakan pangan bagi masyarakat setempat. 
            Namun, perubahan iklim yang tidak menentu mengganggu kestabilan produksi ikan di Danau Laut Tawar. 
            Salah satu faktor penyebabnya adalah fenomena upwelling. Pada tahun 2017, fenomena ini pernah merugikan pembudidaya Keramba Jaring Apung (KJA) di Danau Laut Tawar, hingga mengakibatkan kerugian mencapai ratusan juta rupiah.
        """)

        column_header = 'Deskripsi Kolom dari Tabel'
        tampilan_header = 'Tampilan Data Historis'
        
        column_description = """
        1. DATE         : Kolom yang mencatat tanggal indikator iklim
        2. ALLSKY_KT    : Indeks kejernihan insolasi langit
        3. T2M          : Suhu udara rata-rata pada ketinggian 2 meter (°C)
        4. PRECTOTCORR  : Curah hujan (mm)
        5. PS           : Tekanan permukaan rata-rata di permukaan bumi (kPa)
        6. WS10M        : Kecepatan angin rata-rata pada ketinggian 10 meter (m/s)
        7. Status       : Potensi Kejadian Upwelling
        """

    else:
        # Konten dalam Bahasa Inggris
        st.title("Climate Indicator-Based Upwelling Monitoring and Prediction Dashboard in Danau Laut Tawar")
        st.markdown("""
            Welcome to the Lake Laut Tawar climate indicator-based Upwelling Monitoring and Prediction Dashboard! The local community utilizes this lake as one of the main sources of livelihood. By combining the data in a year, the potential fish production in Danau Laut Tawar can reach 196 tons. This figure is quite fantastic and shows how important the role of Danau Laut Tawar is in supporting the local economy and providing food for the local community. However, erratic climate change is destabilizing fish production in Danau Laut Tawar. One of the contributing factors is the upwelling phenomenon. In 2017, this phenomenon had harmed floating net cage (KJA) farmers in the freshwater lake, resulting in losses of hundreds of millions of rupiah.
        """)
        
        column_header = 'Column descriptions of the table'
        tampilan_header = 'Historical Data Display'
        
        column_description = """
        1. DATE             : Records the date of the climate indicator
        2. ALLSKY_KT        : Sky insolation clarity index
        3. T2M              : Average air temperature at 2 meters height (°C)
        4. PRECTOTCORR      : Rainfall (mm)
        5. PS               : Average surface pressure at the earth's surface (kPa)
        6. WS10M            : Average wind speed at 10 meters height (m/s)
        7. Status           : Potential Upwelling Event
        """

    # Memuat Dataset
    df = load_data("Dashboard/data/HASIL_CLUSTERING.csv")

    # Mengubah format tanggal
    df_class = df.copy()
    df_class['DATE'] = pd.to_datetime(df_class['DATE'])
    df_class.set_index('DATE', inplace=True)

    # Pemilihan Rentang Waktu
    min_date = pd.to_datetime("2017-01-01")
    max_date = pd.to_datetime("2023-12-31")

    date_range = st.date_input("Pilih Rentang Waktu" if lang == "Bahasa Indonesia" else "Select Date Range", 
                               [min_date, max_date], 
                               min_value=min_date, max_value=max_date, key="date_range")
    start_date, end_date = date_range
    filtered_df_class = df_class.loc[start_date:end_date]

    # Menampilkan Data Historis
    st.write(filtered_df_class)

    # Penjelasan Struktur Data
    st.header(column_header)
    st.text(column_description)

    # Menampilkan Plot Kejadian Upwelling dan Tidak Upwelling
    fig = go.Figure()
    for Status, color in zip(filtered_df_class['Status'].unique(), ['red', 'green']):
        filtered_df = filtered_df_class[filtered_df_class['Status'] == Status]
        fig.add_trace(go.Scatter(x=filtered_df.index, y=filtered_df['PRECTOTCORR'],
                             mode='markers', name=Status, line=dict(color=color)))
    fig.update_layout(title='Potensi Upwelling vs Tidak Berpotensi Upwelling Berdasarkan Indikator Iklim' if lang == "Bahasa Indonesia" 
                      else 'Potential Upwelling vs Non-Upwelling Events Based on Climate Indicators',
                  xaxis_title='Tanggal' if lang == "Bahasa Indonesia" else 'Date',
                  yaxis_title='Curah Hujan (PRECTOTCORR)' if lang == "Bahasa Indonesia" else 'Rainfall (PRECTOTCORR)',
                  template='plotly_dark')
    st.header(tampilan_header)
    st.plotly_chart(fig, use_container_width=True)

    # Pilihan Indikator Iklim untuk Ditampilkan
    st.header("Pilih Indikator Iklim yang Ingin Ditampilkan" if lang == "Bahasa Indonesia" else "Select Climate Indicators")

    with st.expander("Pilih Indikator Iklim yang Ingin Ditampilkan:" if lang == "Bahasa Indonesia" else "Choose Climate Indicators to Display:"):
        allsky_kt = st.checkbox('ALLSKY_KT - Indeks Kejernihan Langit' if lang == "Bahasa Indonesia" else 'ALLSKY_KT - Sky Insolation Clarity Index')
        t2m = st.checkbox('T2M - Suhu Udara Rata-Rata pada Ketinggian 2 Meter (°C)' if lang == "Bahasa Indonesia" else 'T2M - Average Air Temperature at 2 Meters Height (°C)')
        prectotcorr = st.checkbox('PRECTOTCORR - Curah Hujan (mm)' if lang == "Bahasa Indonesia" else 'PRECTOTCORR - Rainfall (mm)')
        ps = st.checkbox('PS - Tekanan Permukaan Rata-Rata (kPa)' if lang == "Bahasa Indonesia" else 'PS - Average Surface Pressure (kPa)')
        ws10m = st.checkbox('WS10M - Kecepatan Angin Rata-Rata pada Ketinggian 10 Meter (m/s)' if lang == "Bahasa Indonesia" else 'WS10M - Average Wind Speed at 10 Meters Height (m/s)')

    # Menampilkan Indikator Iklim yang Dipilih
    if allsky_kt:
        fig_indicator = plot_climate_indicator(filtered_df_class, 'ALLSKY_KT', lang)
        st.plotly_chart(fig_indicator, use_container_width=True)
    
    if t2m:
        fig_indicator = plot_climate_indicator(filtered_df_class, 'T2M', lang)
        st.plotly_chart(fig_indicator, use_container_width=True)
    
    if prectotcorr:
        fig_indicator = plot_climate_indicator(filtered_df_class, 'PRECTOTCORR', lang)
        st.plotly_chart(fig_indicator, use_container_width=True)
    
    if ps:
        fig_indicator = plot_climate_indicator(filtered_df_class, 'PS', lang)
        st.plotly_chart(fig_indicator, use_container_width=True)
    
    if ws10m:
        fig_indicator = plot_climate_indicator(filtered_df_class, 'WS10M', lang)
        st.plotly_chart(fig_indicator, use_container_width=True)

if __name__ == "__main__":
    app()

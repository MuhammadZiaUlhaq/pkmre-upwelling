import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from web_function import preprocess_dataframe, load_data  # Assuming these are your custom functions

def plot_rainfall_line(df):
    fig = go.Figure()
    for event_type in df['Status'].unique():
        event_data = df[df['Status'] == event_type]
        fig.add_trace(go.Scatter(x=event_data.index, y=event_data['PRECTOTCORR'],
                                 mode='lines', name=event_type))
    fig.update_layout(title='Average Rainfall Over Time',
                      xaxis_title='Date',
                      yaxis_title='PRECTOTCORR',
                      template='plotly_dark')
    return fig

def plot_climate_indicator(df, indicator):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df[indicator], mode='lines', name=indicator))
    fig.update_layout(title=['ALLSKY_KT', 'T2M', 'PRECTOTCORR', 'PS', 'WS10M'],
                      xaxis_title='Date',
                      yaxis_title=indicator,
                      template='plotly_dark')
    return fig

def app():
    # Language selection
    lang = st.selectbox("Select Language / Pilih Bahasa", ["English", "Bahasa Indonesia"])

    if lang == "English":
        # English content
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

    else:
        # Indonesian content
        st.title("Dashboard Pemantauan dan Prediksi Upwelling Berbasis Indikator Iklim di Danau Laut Tawar")
        st.markdown("""
            Selamat datang di Dashboard Pemantauan dan Prediksi Upwelling berbasis indikator iklim Danau Laut Tawar! Masyarakat setempat memanfaatkan danau ini sebagai salah satu sumber mata pencaharian utama. Dengan manggabungkan data Dalam setahun, potensi produksi ikan di Danau Laut Tawar dapat mencapai 196 ton. Angka ini cukup fantastis dan menunjukkan betapa pentingnya peran Danau Laut Tawar dalam menyokong ekonomi lokal serta menyediakan pangan bagi masyarakat setempat. Namun, perubahan iklim yang tidak menentu mengganggu kestabilan produksi ikan di Danau Laut Tawar. Salah satu faktor penyebabnya adalah fenomena upwelling. Pada tahun 2017, fenomena ini pernah merugikan pembudidaya Keramba Jaring Apung (KJA) di Danau Laut Tawar, higga mengakibatkan kerugian mencapai ratusan juta rupiah.
        """)
        
        column_header = 'Deskripsi kolom dari table tersebut'
        tampilan_header = 'Tampilan Data Historis'
        
        column_description = """
        1. DATE         : Merupakan kolom yang mencatat tanggal indikator iklim
        2. ALLSKY_KT    : Indeks kejernihan insolasi langit
        3. T2M          : Suhu udara rata-rata pada ketinggian 2 meter (°C)
        4. PRECTOTCORR  : Curah hujan (mm)
        5. PS           : Rata-rata tekanan permukaan di permukaan bumi (kPa)
        6. WS10M        : Kecepatan angin rata-rata pada ketinggian 10 meter (m/s)
        7. Status       : Potensi Kejadian Upwelling
        """

    # Load Dataset
    df = load_data("Dashboard/data/HASIL_CLUSTERING.csv")

    # Data Historis Banjir
    df_class = df.copy()
    df_class['DATE'] = pd.to_datetime(df_class['DATE'])
    df_class.set_index('DATE', inplace=True)

    # Define the date range for selection
    min_date = pd.to_datetime("2017-01-01")
    max_date = pd.to_datetime("2023-12-31")

    # Pemfilteran Data Berdasarkan Range Waktu
    date_range = st.date_input("Pilih Rentang Waktu", [min_date, max_date], min_value=min_date, max_value=max_date, key="date_range")
    start_date, end_date = date_range
    filtered_df_class = df_class.loc[start_date:end_date]

    # Menampilkan Data Historis Banjir
    st.write(filtered_df_class)

    # Menampilkan penjelasan dari struktur data
    st.header(column_header)
    st.text(column_description)
    
    
    
    # Menampilkan Plot Kejadian "Banjir" dan "Tidak Banjir" 
    fig = go.Figure()
    for Status, color in zip(filtered_df_class['Status'].unique(), ['red', 'green']):  # Choose your preferred colors
        filtered_df = filtered_df_class[filtered_df_class['Status'] == Status]
        fig.add_trace(go.Scatter(x=filtered_df.index, y=filtered_df['PRECTOTCORR'],
                             mode='markers', name=Status, line=dict(color=color)))
    fig.update_layout(title='Potensi Upwelling vs Tidak Berpotensi Upwelling berdasarkan Indikator Iklim',
                  xaxis_title='Date',
                  yaxis_title='PRECTOTCORR',
                  template='plotly_dark')
    st.header(tampilan_header)
    st.plotly_chart(fig, use_container_width=True)

    # Menampilkan Line Chart dari indikator iklim lainnya satu per satu
    climate_indicators = ['ALLSKY_KT', 'T2M', 'PRECTOTCORR', 'PS', 'WS10M']
    for indicator in climate_indicators:
        fig_indicator = plot_climate_indicator(filtered_df_class, indicator)
        st.plotly_chart(fig_indicator, use_container_width=True)

if __name__ == "__main__":
    app()

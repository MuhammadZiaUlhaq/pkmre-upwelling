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

def app():
    # Language selection
    lang = st.selectbox("Select Language / Pilih Bahasa", ["English", "Bahasa Indonesia"])

    if lang == "English":
        # English content
        st.title("Climate Indicator-Based Upwelling Monitoring and Prediction Dashboard in Danau Laut Tawar")
        st.markdown("""
            Welcome to the Lake Laut Tawar climate indicator-based Upwelling Monitoring and Prediction Dashboard! The local community utilizes this lake as one of the main sources of livelihood. By combining the data in a year, the potential fish production in Danau Laut Tawar can reach 196 tons. This figure is quite fantastic and shows how important the role of Danau Laut Tawar is in supporting the local economy and providing food for the local community. However, erratic climate change is destabilizing fish production in Danau Laut Tawar. One of the contributing factors is the upwelling phenomenon. In 2017, this phenomenon had harmed floating net cage (KJA) farmers in the freshwater lake, resulting in losses of hundreds of millions of rupiah.
        """)

        column_description = """
        1. DATE         : Records the date of the climate indicator
        2. ALLSKY_KT    : Sky insolation clarity index
        3. T2M          : Average air temperature at 2 meters height (°C)
        4. TS           : Average temperature at the earth's surface (°C)
        5. PRECTOTCORR  : Rainfall (mm)
        6. PS           : Average surface pressure at the earth's surface (kPa)
        7. WS10M        : Average wind speed at 10 meters height (m/s)
        8. Status       : Potential Upwelling Event
        """

    else:
        # Indonesian content
        st.title("Dashboard Pemantauan dan Prediksi Upwelling Berbasis Indikator Iklim di Danau Laut Tawar")
        st.markdown("""
            Selamat datang di Dashboard Pemantauan dan Prediksi Upwelling berbasis indikator iklim Danau Laut Tawar! Masyarakat setempat memanfaatkan danau ini sebagai salah satu sumber mata pencaharian utama. Dengan manggabungkan data Dalam setahun, potensi produksi ikan di Danau Laut Tawar dapat mencapai 196 ton. Angka ini cukup fantastis dan menunjukkan betapa pentingnya peran Danau Laut Tawar dalam menyokong ekonomi lokal serta menyediakan pangan bagi masyarakat setempat. Namun, perubahan iklim yang tidak menentu mengganggu kestabilan produksi ikan di Danau Laut Tawar. Salah satu faktor penyebabnya adalah fenomena upwelling. Pada tahun 2017, fenomena ini pernah merugikan pembudidaya Keramba Jaring Apung (KJA) di Danau Laut Tawar, higga mengakibatkan kerugian mencapai ratusan juta rupiah.
        """)

        column_description = """
        1. DATE         : Merupakan kolom yang mencatat tanggal indikator iklim
        2. ALLSKY_KT    : Indeks kejernihan insolasi langit
        3. T2M          : Suhu udara rata-rata pada ketinggian 2 meter (°C)
        4. TS           : Suhu rata-rata di permukaan bumi (°C)
        5. PRECTOTCORR  : Curah hujan (mm)
        6. PS           : Rata-rata tekanan permukaan di permukaan bumi (kPa)
        7. WS10M        : Kecepatan angin rata-rata pada ketinggian 10 meter (m/s)
        8. Status       : Potensi Kejadian Upwelling
        """

    # Load Dataset
    df = load_data("Dashboard/data/HASIL_CLUSTERING.csv")

    # Data Historis Banjir
    df_class = df.copy()
    df_class['DATE'] = pd.to_datetime(df_class['DATE'])
    df_class.set_index('DATE', inplace=True)

    # Pemfilteran Data Berdasarkan Range Waktu
    date_range = st.date_input("Pilih Rentang Waktu", [df_class.index.min(), df_class.index.max()], key="date_range")
    start_date, end_date = date_range
    filtered_df_class = df_class.loc[start_date:end_date]

    # Menampilkan Data Historis Banjir
    st.header("Deskripsi kolom dari table tersebut")
    st.write(filtered_df_class)

    # Menampilkan penjelasan dari struktur data
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
    st.plotly_chart(fig, use_container_width=True)

# Entry point of the app
if __name__ == '__main__':
    app()


'''
    # Data Historis Curah Hujan
    st.header("Data Historis Curah Hujan")
    df_time = df.drop(columns=['Kejadian','min_hujan', 'max_hujan', 'avg_hujan'])
    
    # Memberikan Opsi Resampling Frekuensi
    freq_options = {'Raw': '','Hourly': 'H', 'Daily': 'D' , 'Weekly': 'W', 'Monthly': 'M'}
    freq = st.radio("Pilih Frekuensi Resampling:", list(freq_options.keys()))

    # Menampilkan Data Historis Curah Hujan Berdasarkan Frekuensi
    df_time = preprocess_dataframe(df_time, freq_options[freq])  # Resample based on the selected frequency
    filtered_df_time = df_time.loc[start_date:end_date]

    col1, col2 = st.columns([1, 3])
    with col1:
        st.write(filtered_df_time)

    with col2:
        st.text("Dengan menghitung rata-rata dari frekuensi data yang diresample, kita dapat mendapatkan  \
            \nnilai rata-rata curah hujan untuk setiap interval waktu yang dipilih (misalnya, harian, \
            \nmingguan, atau bulanan). Perhitungan ini memberikan gambaran umum tentang kecenderungan  \
            \ncurah hujan selama interval waktu tersebut. Misalnya, rata-rata harian dapat memberikan \
            \ninformasi tentang curah hujan rata-rata setiap hari dalam satu bulan. Proses ini tidak  \
            \nhanya membantu dalam menyederhanakan data, tetapi juga memungkinkan penggunaan metrik \
            \nyang lebih mudah diinterpretasi dalam analisis. \
            \n\nDengan menggunakan nilai rata-rata ini, pengguna dapat mengidentifikasi pola, tren,  \
            \natau fluktuasi dalam curah hujan dengan lebih baik. Informasi ini kemudian dapat \
            \ndigunakan sebagai dasar untuk proses forecasting lebih lanjut atau untuk  \
            \nmengembangkan model prediksi terkait potensi banjir. Rata-rata frekuensi data \
            \nyang diresample memberikan ringkasan yang lebih mudah dipahami, yang dapat  \
            \ndigunakan sebagai dasar untuk pengambilan keputusan terkait manajemen risiko banjir."
    )    

    # Menampilkan Plot Curah Hujan
    fig = px.line(filtered_df_time, x=filtered_df_time.index, y=filtered_df_time.columns, title=f'Curah Hujan - Resampled {freq}')
    fig.update_traces(mode='lines+markers', hovertemplate='<b>Waktu</b>: %{x|%Y-%m-%d %H:%M:%S}<br><b>Curah Hujan</b>: %{y:.2f} mm')
    fig.update_layout(
        xaxis=dict(
            title_text='Waktu',
            rangeslider=dict(
                visible=True
            ),
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1h", step="hour", stepmode="backward"),
                    dict(count=1, label="1d", step="day", stepmode="backward"),
                    dict(count=7, label="1w", step="day", stepmode="backward"),
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=3, label="3m", step="month", stepmode="backward"),
                    dict(step="all")
                ]),
                bgcolor='#32B166',
                font=dict(color='black'),
                activecolor='gray',
                y=1
            ),
        ),
        yaxis=dict(title_text='Curah Hujan (mm)'),
        xaxis_rangeslider_visible=True,
    )
    st.plotly_chart(fig, use_container_width=True)




'''

            

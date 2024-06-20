import streamlit as st
import pandas as pd
from web_function import preprocess_dataframe, load_data
import plotly.express as px
import plotly.graph_objects as go

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
    # Language Selection
    language = st.sidebar.selectbox("Select Language / Pilih Bahasa", ["English", "Indonesian"])

    if language == "English":
        st.title("Monitoring and Prediction Dashboard for Climate Indicator-Based Upwelling in Lake Tawar")
        st.write("Welcome to the Monitoring and Prediction Dashboard for climate indicator-based upwelling in Lake Tawar! The local community relies on this lake as a primary livelihood source.")
        st.write("Within a year, potential fish production in Lake Tawar can reach 196 tons. This figure is quite significant and underscores the lake's importance in supporting the local economy and providing food for the community.")
        st.write("However, unpredictable climate changes disrupt fish production stability in Lake Tawar. One contributing factor is the phenomenon of upwelling. In 2017, this phenomenon adversely affected floating cage aquaculture (KJA) in Lake Tawar, resulting in losses amounting to hundreds of millions of rupiah.")

    elif language == "Indonesian":
        st.title("Dashboard Pemantauan dan Prediksi Upwelling Berbasis Indikator Iklim di Danau Laut Tawar")
        st.write("Selamat datang di Dashboard Pemantauan dan Prediksi Upwelling berbasis indikator iklim Danau Laut Tawar! Masyarakat setempat memanfaatkan danau ini sebagai salah satu sumber mata pencaharian utama.")
        st.write("Dalam setahun, potensi produksi ikan di Danau Laut Tawar dapat mencapai 196 ton. Angka ini cukup fantastis dan menunjukkan betapa pentingnya peran Danau Laut Tawar dalam menyokong ekonomi lokal serta menyediakan pangan bagi masyarakat setempat.")
        st.write("Namun, perubahan iklim yang tidak menentu mengganggu kestabilan produksi ikan di Danau Laut Tawar. Salah satu faktor penyebabnya adalah fenomena upwelling. Pada tahun 2017, fenomena ini pernah merugikan pembudidaya Keramba Jaring Apung (KJA) di Danau Laut Tawar, hingga mengakibatkan kerugian mencapai ratusan juta rupiah.")

    # Load Dataset
    df = load_data("Dashboard\data\HASIL_CLUSTERING.csv")

    # Data Historis Banjir
    df_class = df.copy()
    df_class['DATE'] = pd.to_datetime(df_class['DATE'])
    df_class.set_index('DATE', inplace=True)

    # Pemfilteran Data Berdasarkan Range Waktu
    date_range = st.date_input("Select Date Range / Pilih Rentang Waktu", [df_class.index.min(), df_class.index.max()], key="date_range")
    start_date, end_date = date_range
    filtered_df_class = df_class.loc[start_date:end_date]

    # Menampilkan Data Historis Banjir
    st.header("Description of the columns from the table")
    st.write(filtered_df_class)

    # Menampilkan penjelasan dari struktur data
    st.markdown("Description of the columns from the table:")
    kolomdesc = '\n1.  DATE\t: Records the date climate indicators were recorded\
                \n2.  ALLSKY_KT\t: Insolation clarity index of the sky\
                \n3.  T2M\t: Average air temperature at a height of 2 meters (degC)\
                \n4.  TS\t: Average temperature at the Earth\'s surface (degC)\
                \n5.  PRECTOTCORR\t: Precipitation (mm)\
                \n6.  PS\t: Average surface pressure at the Earth\'s surface (kPA)\
                \n7.  WS10M\t: Average wind speed at a height of 10 meters (m/s)\
                \n8.  Status\t: Indicates rainfall (mm) at 15:00\
                \n9.  hujan_2100\t: Potential Upwelling Event\
                \n10. min_hujan\t: Potential Upwelling Event'
    st.text(kolomdesc)


    # Menampilkan Plot Kejadian "Banjir" dan "Tidak Banjir" 
    fig = go.Figure()
    for Status, color in zip(filtered_df_class['Status'].unique(), ['green', 'red']):  # Choose your preferred colors
        filtered_df = filtered_df_class[filtered_df_class['Status'] == Status]
        fig.add_trace(go.Scatter(x=filtered_df.index, y=filtered_df['PRECTOTCORR'],
                             mode='lines+markers', name=Status, line=dict(color=color)))
    fig.update_layout(title='Potential Upwelling vs Non-Upwelling based on Climate Indicators',
                  xaxis_title='Date',
                  yaxis_title='PRECTOTCORR',
                  template='plotly_dark')
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
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

            

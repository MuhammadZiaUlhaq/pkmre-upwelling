import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    # Judul Halaman
    st.title("Data Display")

    # Load the CSV file
    csv_path = 'Dashboard/data/data.csv'
    df = pd.read_csv(csv_path)

    # Convert the DATE column to datetime format with the correct format
    df['DATE'] = pd.to_datetime(df['DATE'], format='%d/%m/%Y').dt.date  # Mengubah ke format tanggal saja
    df.set_index('DATE', inplace=True)

    # Define the date range for selection
    min_date = pd.to_datetime("1/1/2024", format="%d/%m/%Y").date()  # Mengubah ke format tanggal saja
    max_date = pd.to_datetime("31/12/2025", format="%d/%m/%Y").date()  # Mengubah ke format tanggal saja

    # Pemfilteran Data Berdasarkan Range Waktu
    date_range = st.date_input("Pilih Rentang Waktu", [], min_value=min_date, max_value=max_date)
    if len(date_range) != 2:
        st.error("Please select date range.")
        return
    start_date, end_date = date_range
    filtered_df = df.loc[start_date:end_date]

    st.write(f"Menampilkan data dari {start_date} hingga {end_date}")

    # Display the data and plot for each column
    st.subheader("CSV Data and Corresponding Plots")
    for column in filtered_df.columns:
        col1, col2 = st.columns(2)
        
        # Display the table
        with col1:
            st.write(f"**{column}**")
            st.write(filtered_df[[column]])
        
        # Display the plot
        with col2:
            st.write(f"**Plot for {column}**")
            fig = px.line(filtered_df, x=filtered_df.index, y=column, title=f'Plot of {column}')
            st.plotly_chart(fig)
    #tampilan setelah tanggal
    st.write(filtered_df)
    # Provide a download button for the data
    csv_data = filtered_df.to_csv(index=True)
    st.download_button(label="Download CSV", data=csv_data, file_name='filtered_data.csv', key='download_button')

app()

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
    df['DATE'] = pd.to_datetime(df['DATE'], format='%d/%m/%Y')
    df.set_index('DATE', inplace=True)

    # Define the date range for selection
    min_date = pd.to_datetime("1/1/2024", format="%d/%m/%Y")
    max_date = pd.to_datetime("31/12/2025", format="%d/%m/%Y")

    # Pemfilteran Data Berdasarkan Range Waktu
    date_range = st.date_input("Pilih Rentang Waktu", [min_date, max_date], min_value=min_date, max_value=max_date, key="date_range")
    start_date, end_date = date_range
    filtered_df = df.loc[start_date:end_date]

    st.write(f"Menampilkan data dari {start_date} hingga {end_date}")

    # Display the data and plot for each column
    st.subheader("CSV Data and Corresponding Plots")
    for column in filtered_df.columns:
        col1, col2 = st.columns((1, 1))  # Adjust column widths to center the table and plot
        
        # Display the table
        with col1:
            st.write(f"**{column}**")
            st.write(filtered_df[[column]])
        
        # Display the plot
        with col2:
            st.write(f"**Plot for {column}**")
            fig = px.line(filtered_df, x=filtered_df.index, y=column, title=f'Plot of {column}')
            st.plotly_chart(fig, use_container_width=True)  # Use container width to center the plot
            
    # Display preview of the data to be downloaded
    st.subheader("Preview of Data to be Downloaded")
    st.write(filtered_df)

    # Provide a download button for the data
    csv_data = filtered_df.to_csv(index=True)
    st.download_button(label="Download CSV", data=csv_data, file_name='filtered_data.csv', key='download_button')

app()
import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    # Judul Halaman
    st.title("Data Display")

    # Load the CSV file
    csv_path = 'Dashboard/data/2.csv'
    df = pd.read_csv(csv_path, delimiter=';')

    # Convert the DATE column to datetime format
    df['DATE'] = pd.to_datetime(df['DATE'], format='%d/%m/%Y')  # Mengubah ke format datetime
    df.set_index('DATE', inplace=True)

    # Define the date range for selection
    min_date = pd.to_datetime("1/1/2024", format="%d/%m/%Y").date()
    max_date = pd.to_datetime("31/12/2025", format="%d/%m/%Y").date()

    # Pemfilteran Data Berdasarkan Range Waktu
    date_range = st.date_input("Pilih Rentang Waktu", [], min_value=min_date, max_value=max_date)
    if len(date_range) != 2:
        st.error("Please select date range.")
        return
    start_date, end_date = date_range
    filtered_df = df.loc[start_date:end_date]

    st.write(f"Menampilkan data hasil forecast dari {start_date} hingga {end_date}")

    # Convert the date to the desired format (dd/mm/yyyy) for display
    filtered_df_display = filtered_df.copy()
    filtered_df_display.index = filtered_df_display.index.strftime('%d/%m/%Y')  # Format index DATE

    # Display the data and plot for each column
    st.subheader("CSV Data and Corresponding Plots")
    for column in filtered_df.columns:
        col1, col2 = st.columns(2)
        
        # Display the table
        with col1:
            st.write(f"**{column}**")
            st.write(filtered_df_display[[column]])  # Display with formatted DATE
        
        # Display the plot
        with col2:
            st.write(f"**Plot for {column}**")
            fig = px.line(filtered_df, x=filtered_df.index, y=column, title=f'Plot of {column}')
            st.plotly_chart(fig)
    
    # Display the filtered dataframe after formatting date
    st.write(filtered_df_display)

    # Provide a download button for the data
    csv_data = filtered_df.to_csv(index=True)
    st.download_button(label="Download CSV", data=csv_data, file_name='filtered_data.csv', key='download_button')

    st.write("Setelah melakukan forecasting curah hujan, nilai-nilai hasil forscast tersebut dapat dijadikan sebagai input untuk model prediksi yang lebih lanjut. Data forecasting ini mencakup estimasi (nama nama variable) di masa depan, yang diperoleh melalui metode analysis time series SVARMA dan VAR.")

if __name__ == "__main__":
    app()

import streamlit as st
from st_social_media_links import SocialMediaIcons


def app():

    # Language selection
    lang = st.selectbox("Select Language / Pilih Bahasa", ["English", "Bahasa Indonesia"])

    if lang == "English":
        # English content
        st.title("About Us")
        st.header("Project Description")
        st.markdown("""
            This dashboard is part of the output from the Program Kreatifitas Mahasiswa – Riset Eksakta (PKM - RE) conducted by students of Syiah Kuala University. This project is designed to help Floating Net Cage farmers in Danau Laut Tawar make decisions in fish farming.
        """)

        col_1, col_2, col_3 = st.columns(3)
        with col_1:
            st.header("Vision")
            st.markdown("""
            To be an innovative solution provider in mitigating upwelling risks and providing accurate information for decision-making by Danau Laut Tawar KJA farmers.
            """)
        with col_2:
            st.header("Mission")
            st.markdown("""
            1. Accurately collect and analyze upwelling events and climate indicators.
            2. Develop reliable upwelling prediction models based on historical data.
            3. Provide an interactive dashboard to monitor and forecast upwelling risks.
            4. Effectively disseminate information on upwelling risks to KJA farmers.
            """)
        with col_3:
            st.header("Goals")
            st.markdown("""
            1. Provide a reliable source of information related to upwelling risks in Danau Laut Tawar.
            2. Increase awareness and preparedness of Danau Laut Tawar KJA farmers against potential upwelling risks.
            3. Support mitigation and countermeasures against upwelling risks in Danau Laut Tawar.
            """)

        st.header("Datasets Used")
        st.markdown("""
            We use several datasets in this project. Here are some of them:
            1. Upwelling events data in Danau Laut Tawar.
            2. Danau Laut Tawar climate data - [NASA Prediction Of Worldwide Energy Resources](https://power.larc.nasa.gov/)
        """)

        st.header("Models Used")
        st.markdown("""
            #### Forecasting Models (SVARMA and Seasonal Autoregressive):
            We use two models, SVARMA and Seasonal Autoregressive, to forecast climate indicators at various time intervals:
            - All sky insolation clearness index: MSE = 0,0526, RMSE = 0,2295, MAE = 0,1815
            - Temperature: MSE = 0,0341, RMSE = 0,1847, MAE = 0,1514
            - Precipitation: MSE = 0,0738, RMSE = 0,2721, MAE = 0,2191
            - Surface pressure: MSE = 0,0399, RMSE = 0,1998, MAE = 0,1602
            - Wind speed: MSE = 0,0287, RMSE = 0,1697, MAE = 0,1347

            #### Prediction Model:
            We use the SVM model to predict upwelling:
            - SVM model with F1-Score = 0,985
        """)

        st.header("Technologies / Tools Used")
        st.markdown("""
            - **Streamlit:** For building the user interface.
            - **Pandas & R:** For data manipulation and analysis.
            - **Joblib:** For saving and loading machine learning models.
            - **Plotly Express and Plotly Graph Objects:** Libraries for creating interactive data visualizations.
        """)

        st.header("Social Media")
        st.markdown("""
            <a href="https://www.instagram.com/pkmre_upwelling?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram" style="width:30px;height:30px;">
            @pkmre_upwelling
            </a>
            """, unsafe_allow_html=True)
        st.markdown("""
            <a href="https://www.tiktok.com/@pkmre_upwelling?_t=8n8OhzhoUsr&_r=1">
            <img src="https://upload.wikimedia.org/wikipedia/en/a/a9/TikTok_logo.svg" alt="TikTok" style="width:30px;height:30px;background-color:white;">
            @pkmre_upwelling
            </a>
            """, unsafe_allow_html=True)

        st.header("Contact")
        st.markdown("""
            If you have any questions or feedback, please contact us:
        """)
        col_4, col_5 = st.columns(2)
        with col_4:
            st.markdown("""
                - **Muhammad Zia Ulhaq**
                    - Email: [ziaswatfbicia@gmail.com](mailto:ziaswatfbicia@gmail.com) 
                    - LinkedIn: [Muhammad Zia Ulhaq](https://www.linkedin.com/in/muhammad-zia-ulhaq-8373112b9/) 

                - **Zahra Ifma Aziza**
                    - Email: [zahraifmaa@gmail.com](mailto:zahraifmaa@gmail.com) 
                    - LinkedIn: [Zahra Ifma Aziza](https://www.linkedin.com/in/zahra-ifma-aziza) 

                - **Muhammad Farid**
                    - Email: [mhdfaridz93@gmail.com](mailto:mhdfaridz93@gmail.com) 
                    - LinkedIn: [Muhammad Farid](https://www.linkedin.com/in/MHD-FARID)  
            """)
        with col_5:
            st.markdown("""
                - **Fakhrus Syakir**
                    - Email: [fakhroosyakir@gmail.com](mailto:fakhroosyakir@gmail.com) 
                    - LinkedIn: [Fakhrus Syakir](https://www.linkedin.com/in/fakhrus-syakir-65bb72205/) 

                - **Teuku Muhammad Faiz Nuzullah**
                    - Email: [faiznuzullah@gmail.com](mailto:faiznuzullah@gmail.com) 
                    - LinkedIn: [Teuku Muhammad Faiz Nuzullah](https://www.linkedin.com/in/teuku-muhammad-f-4a906a239) 

                - **Novi Reandy Sasmita, S.Si., M.Sc.**
                    - Email: [novireandys@usk.ac.id](mailto:novireandys@usk.ac.id) 
                    - LinkedIn: [Novi Reandy Sasmita, S.Si., M.Sc.](https://www.linkedin.com/in/novi-reandy-sasmita-93371a72/) 
            """)

    else:
        # Indonesian content
        st.title("Tentang Kami")
        st.header("Deskripsi Projek")
        st.markdown("""
            Pembuatan dashboard ini merupakan salah satu luaran dari Pogram Kreativitas Mahasiswa  –Riset Eksakta (PKM - RE) yang dikerjakan oleh Mahasiswa Universitas Syiah Kuala. Projek ini disusun untuk tujuan membantu Pembudidaya Keramba Jaring Apung (KJA) Danau Laut Tawar untuk mengambil Keputusan dalam membudidayakan ikan.
        """)

        col_1, col_2, col_3 = st.columns(3)
        with col_1:
            st.header("Visi")
            st.markdown("""
            Menjadi penyedia solusi inovatif dalam mengatasi risiko upwelling dan memberikan indormasi yang akurat untuk pengambilan keputusan oleh Pembudidaya KJA Danau Laut Tawar
            """)
        with col_2:
            st.header("Misi")
            st.markdown("""
            1. Mengumpulkan dan menganalisis data kejadian upwelling dan indikator iklim dengan akurat.
            2. Mengembangkan model prediksi upwelling yang handal berdasarkan data historis.
            3. Menyediakan dashboard interaktif untuk memantau dan meramalkan risiko upwelling.
            4. Menyebarkan informasi mengenai risiko upwelling kepada Pembudidaya KJA secara efektif.
            """)
        with col_3:
            st.header("Tujuan")
            st.markdown("""
            1.	Menyediakan sumber infomrasi yang terpercaya terkait risiko upwelling di danau laut tawar.
            2.	Meningkatkan kewaspadaan dan kesiapsiagaan pembudaya KJA Danau Laut Tawar terhadap potensi risiko upwelling.
            3.	Mendukung upaya mitigasi dan penanggulangan risiko upwelling di danau laut tawar.
            """)

        st.header("Dataset yang Digunakan")
        st.markdown("""
            Kami menggunakan beberapa dataset dalam projek ini. Berikut adalah beberapa di antaranya:
            1.	Data Kejadian upwelling di Danau Laut Tawar
            2.	data iklim danau laut tawar - [NASA Prediction Of Worldwide Energy Resources](https://power.larc.nasa.gov/)

        """)

        st.header("Model yang Digunakan")
        st.markdown("""
            #### Model Model Forecast (SVARMA dan Seasonal Autoregresive):
            Kami menggunakan dua model SVARMA dan Seaonal Autoregresive untuk meramalkan indicator iklim pada berbagai interval waktu:            
            - All sky insilation cleaness index : MSE = 0,0526, RMSE = 0,2295, MAE = 0,1815
            - Temperature: MSE = 0,0341, RMSE = 0,1847, MAE = 0,1514
            - Precipitation: MSE = 0,0738, RMSE = 0,2721, MAE = 0,2191
            - Surface pressure: MSE = 0,0399, RMSE = 0,1998, MAE = 0,1602
            - Wind speed: MSE = 0,0287, RMSE = 0,1697, MAE = 0,1347


            #### Model 	prediksi:
            Kami menggunakan model SVM  untuk memprediksi upwelling:

            - Model svm dengan nilai F1-Score = 0,985
            """)

        st.header("Teknologi / Tools yang Digunakan")
        st.markdown("""
            - **Streamlit:** Untuk pembuatan antarmuka pengguna.
            - **Pandas & R:** Untuk manipulasi dan analisis data.
            - **Joblib:** Untuk menyimpan dan memuat model pembelajaran mesin.
            - **Plotly Express dan Plotly Graph Objects:** Library untuk membuat visualisasi data interaktif.

        """)
        st.header("Sosial Media")
        st.markdown("""
            <a href="https://www.instagram.com/pkmre_upwelling?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram" style="width:30px;height:30px;">
            @pkmre_upwelling
            </a>
            """, unsafe_allow_html=True)
        st.markdown("""
            <a href="https://www.tiktok.com/@pkmre_upwelling?_t=8n8OhzhoUsr&_r=1">
            <img src="https://upload.wikimedia.org/wikipedia/en/a/a9/TikTok_logo.svg" alt="TikTok" style="width:30px;height:10px;background-color:white;">
            @pkmre_upwelling
            </a>
            """, unsafe_allow_html=True)

        st.header("Kontak")
        st.markdown("""
            Jika Anda memiliki pertanyaan atau umpan balik, silakan hubungi kami:
        """)
        col_4, col_5 = st.columns(2)
        with col_4:
            st.markdown("""
                - **Muhammad Zia Ulhaq**
                    - Email: [ziaswatfbicia@gmail.com](mailto:ziaswatfbicia@gmail.com) 
                    - LinkedIn: [Muhammad Zia Ulhaq](https://www.linkedin.com/in/muhammad-zia-ulhaq-8373112b9/) 

                - **Zahra Ifma Aziza**
                    - Email: [zahraifmaa@gmail.com](mailto:zahraifmaa@gmail.com) 
                    - LinkedIn: [Zahra Ifma Azia](https://www.linkedin.com/in/zahra-ifma-aziza) 

                - **Muhammad Farid**
                    - Email: [mhdfaridz93@gmail.com](mailto:mhdfaridz93@gmail.com) 
                    - LinkedIn: [Muhammad Farid](https://www.linkedin.com/in/MHD-FARID)  
            """)
        with col_5:
            st.markdown("""
                - **Fakhrus Syakir**
                    - Email: [fakhroosyakir@gmail.com](mailto:fakhroosyakir@gmail.com) 
                    - LinkedIn: [Fakhrus Syakir](https://www.linkedin.com/in/fakhrus-syakir-65bb72205/) 

                - **Teuku Muhammad Faiz Nuzullah**
                    - Email: [faiznuzullah@gmail.com](mailto:faiznuzullah@gmail.com) 
                    - LinkedIn: [Teuku Muhammad Faiz Nuzullah](https://www.linkedin.com/in/teuku-muhammad-f-4a906a239) 

                - **Novi Reandy Sasmita, S.Si., M.Sc.**
                    - Email: [novireandys@usk.ac.id](mailto:novireandys@usk.ac.id) 
                    - LinkedIn: [Novi Reandy Sasmita, S.Si., M.Sc.](https://www.linkedin.com/in/novi-reandy-sasmita-93371a72/) 
            """)


import streamlit as st
from st_social_media_links import SocialMediaIcons

def app():

    # Language selection
    lang = st.selectbox("Select Language / Pilih Bahasa", ["Bahasa Indonesia", "English"])

    if lang == "Bahasa Indonesia":
        # Indonesian content
        st.title("Tentang Kami")
        st.header("Deskripsi Projek")
        st.markdown("""
            Pembuatan dashboard ini merupakan salah satu luaran dari Pogram Kreativitas Mahasiswa – Riset Eksakta (PKM - RE) yang dikerjakan oleh Mahasiswa Universitas Syiah Kuala. Projek ini disusun untuk tujuan membantu Pembudidaya Keramba Jaring Apung (KJA) Danau Laut Tawar untuk mengambil Keputusan dalam membudidayakan ikan.
        """)
        st.image('Artboard 1.png', use_column_width=True)

        # Visi, Misi, and Tujuan (Vision, Mission, and Goals)
        col_1, col_2, col_3 = st.columns(3)
        with col_1:
            st.header("Visi")
            st.markdown("""
            Menjadi penyedia solusi inovatif dalam mengatasi risiko upwelling dan memberikan informasi yang akurat untuk pengambilan keputusan oleh Pembudidaya KJA Danau Laut Tawar
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
            1. Menyediakan sumber informasi yang terpercaya terkait risiko upwelling di danau laut tawar.
            2. Meningkatkan kewaspadaan dan kesiapsiagaan pembudidaya KJA Danau Laut Tawar terhadap potensi risiko upwelling.
            3. Mendukung upaya mitigasi dan penanggulangan risiko upwelling di danau laut tawar.
            """)

        # Dataset Section
        st.header("Dataset yang Digunakan")
        st.markdown("""
            Kami menggunakan beberapa dataset dalam projek ini. Berikut adalah beberapa di antaranya:
            1. Data Kejadian upwelling di Danau Laut Tawar
            2. Data iklim Danau Laut Tawar   : [NASA Prediction Of Worldwide Energy Resources](https://power.larc.nasa.gov/)
        """)

        # Model Section
        st.header("Model yang Digunakan")
        st.markdown("""
            ### Model Forecast (Seasonal VARMA dan Vector Autoregresive)
            Kami menggunakan dua model Seasonal VARMA dan Vector Autoregresive untuk meramalkan indikator iklim pada berbagai interval waktu
        """)
        """st.write('#### Seasonal VARMA')
        st.latex(r'\Phi(B^s)\phi(B)Y_t = \Theta(B^S)\theta(B)\alpha_t')

        st.markdown(""" 
        """###### Keterangan:
        - 𝑌𝑡        : vektor deret waktu pada periode ke-t,
        - B          : operator pembeda,
        - 𝛼𝑡        : vektor residual white-noise,
        - 𝜙𝑝(𝐵)     : matriks polinomial AR,
        - 𝑞(𝐵)      : matriks polinomial MA,
        - Φ𝑃(𝐵)𝑠    : matriks polinomial AR musiman dan 
        - Θ𝑄(𝐵)𝑠    : matriks polinomial MA musiman
        """"""

        st.write('#### Vector Autoregressive (VAR)')
        st.latex(r'\Phi(B^s)\phi(B)Y_t = \Theta(B^S)\theta(B)\alpha_t')

        st.markdown("""
        """###### Keterangan:
        - 𝑌𝑡      : vektor dari variabel endogen pada waktu t
        - 𝐴𝑖      : matriks koefisien untuk lag i
        - 𝑝       : orde dari model VAR
        - 𝛼𝑡      : vektor residual white-noise
        """
        
        """st.markdown("""
            ### Model Klasifikasi Support Vector Machine (SVM)
            #Kami menggunakan model Klasifikasi Support Vector Machine (SVM) untuk mengklasifikasikan pottensi Upwelling
        """)
        
        st.write('#### Kernel Linear')
        # Linear kernel formula
        st.latex(r'''
                    K(x_i, x) = x_i^T x
                    ''')
        
        st.markdown(""" 
        """###### Keterangan:
        - 𝑥𝑖 = Vektor data training
        - 𝑥 = Vektor data testing
        """
        
        """st.write('#### Kernel RBF')
        # Linear kernel formula
        st.latex(r'''
                    K(x_i, x) = \exp\left(- \gamma \left| x_i^T x \right|^2 \right)
                    ''')
        
        st.markdown(""" 
        """###### Keterangan:
        - 𝑥𝑖 = Vektor data training
        - 𝑥 = Vektor data testing
        - 𝛾= gamma
        """
        
        """st.write('#### Kernel Polynomial')
        # Linear kernel formula
        st.latex(r'''
                    K(x_i, x) = (\gamma \cdot x_i^T x + r)^p
                    ''')
        
        st.markdown(""" 
        """###### Keterangan:
        - 𝑥𝑖 = Vektor data training
        - 𝑥 = Vektor data testing
        - 𝛾= gamma
        - 𝑟= coef ()
        - 𝑝 = degree
        """


        # Evaluation Metrics
        st.write('### Metrik Evaluasi')
        st.markdown("""
            - Indeks Kejernihan Langit   : MSE = 0,0526, RMSE = 0,2295, MAE = 0,1815
            - Suhu Pada Ketinggian 2 M   : MSE = 0,0341, RMSE = 0,1847, MAE = 0,1514
            - Curah Hujan                : MSE = 0,0738, RMSE = 0,2721, MAE = 0,2191
            - Tekanan Permukaan          : MSE = 0,0399, RMSE = 0,1998, MAE = 0,1602
            - Kecepatan Angin            : MSE = 0,0287, RMSE = 0,1697, MAE = 0,1347
        """)

        # Tools and Technologies
        st.header("Teknologi / Tools yang Digunakan")
        st.markdown("""
            - **Streamlit**              : Untuk pembuatan antarmuka pengguna.
            - **Pandas & R**             : Untuk manipulasi dan analisis data.
            - **Joblib**                 : Untuk menyimpan dan memuat model pembelajaran mesin.
            - **Plotly Express**         : Library untuk membuat visualisasi data interaktif.
        """)

        # Social Media
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

        # Contact
        st.header("Kontak")
        st.markdown("""
            Jika Anda memiliki pertanyaan atau umpan balik, silakan hubungi kami:
        """)
        col_4, col_5 = st.columns(2)
        with col_4:
            st.markdown("""
                - ##### Muhammad Zia Ulhaq
                                """)
            st.image('zz.png')
            st.markdown("""
                    - Email   : [ziaswatfbicia@gmail.com](mailto:ziaswatfbicia@gmail.com) 
                    - LinkedIn: [Muhammad Zia Ulhaq](https://www.linkedin.com/in/muhammad-zia-ulhaq-8373112b9/) 
                                    """)
            st.markdown("""
                - ##### Zahra Ifma Aziza
                                """)
            st.image('z.png')
            st.markdown("""
                    - Email   : [zahraifmaa@gmail.com](mailto:zahraifmaa@gmail.com) 
                    - LinkedIn: [Zahra Ifma Aziza](https://www.linkedin.com/in/zahra-ifma-aziza/) 
                    """)
            st.markdown("""
                - ##### Muhammad Farid
                                """)
            st.image('f.png')
            st.markdown("""
                    - Email   : [mhdfaridz93@gmail.com](mailto:mhdfaridz93@gmail.com) 
                    - LinkedIn: [Muhammad Farid](https://www.linkedin.com/in/mhd-farid/)
            """)
        with col_5:
            st.markdown("""
                - ##### Fakhrus Syakir
                """)
            st.image('s.png')
            st.markdown("""
                    - Email   : [fakhroosyakir@gmail.com](mailto:fakhroosyakir@gmail.com) 
                    - LinkedIn: [Fakhrus Syakir](https://www.linkedin.com/in/fakhrus-syakir-65bb72205/) 
                    """)
                    
            st.markdown("""
                - ##### Teuku Muhammad Faiz Nuzullah
                """)
            st.image('p.png')
            st.markdown("""
                    - Email   : [faiznuzullah@gmail.com](mailto:faiznuzullah@gmail.com) 
                    - LinkedIn: [Teuku Muhammad Faiz Nuzullah](https://www.linkedin.com/in/teuku-muhammad-f-4a906a239) 
                    """)
            st.markdown("""
                - #####  Novi Reandy Sasmita, S.Si., M.Sc.
                """)
            st.image('g.png', use_column_width=True)
            st.markdown("""
                    - Email   : [novireandys@usk.ac.id](mailto:novireandys@usk.ac.id) 
                    - LinkedIn: [Novi Reandy Sasmita](https://www.linkedin.com/in/novi-reandy-sasmita-93371a72/)
                    - Website : [Novi Reandy Sasmita's Website](https://www.reandy.info)
            """)


    else:
        # English content
        st.title("About Us")
        st.header("Project Description")
        st.markdown("""
            This dashboard is part of the output from the Program Kreatifitas Mahasiswa – Riset Eksakta (PKM - RE) conducted by students of Syiah Kuala University. This project is designed to help Floating Net Cage farmers in Danau Laut Tawar make decisions in fish farming.
        """)
        st.image('Artboard 1.png', use_column_width=True)

        # Vision, Mission, and Goals
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

        # Dataset Section
        st.header("Datasets Used")
        st.markdown("""
            We use several datasets in this project. Here are some of them:
            1. Upwelling events data in Danau Laut Tawar.
            2. Danau Laut Tawar climate data   : [NASA Prediction Of Worldwide Energy Resources](https://power.larc.nasa.gov/)
        """)

        # Model Section
        st.header("Models Used")
        st.markdown("""
            #### Forecasting Models (Seasonal VARMA and Vector Autoregressive)
            We use two models, Seasonal VARMA and Vector Autoregressive, to forecast climate indicators at various time intervals:
        """)
        """st.write('#### Seasonal VARMA')
        st.latex(r'\Phi(B^s)\phi(B)Y_t = \Theta(B^S)\theta(B)\alpha_t')

        st.markdown(""" 
        """###### Explanation:
        - 𝑌𝑡        : vector of time series at time t,
        - B          : difference operator,
        - 𝛼𝑡        : vector of white-noise residuals,
        - 𝜙𝑝(𝐵)     : AR polynomial matrix,
        - 𝑞(𝐵)      : MA polynomial matrix,
        - Φ𝑃(𝐵)𝑠    : seasonal AR polynomial matrix
        - Θ𝑄(𝐵)𝑠    : seasonal MA polynomial matrix
        """

        """st.write('#### Vector Autoregressive (VAR)')
        st.latex(r'\Phi(B^s)\phi(B)Y_t = \Theta(B^S)\theta(B)\alpha_t')

        st.markdown("""
        """###### Explanation:
        - 𝑌𝑡      : vector of endogenous variables at time t
        - 𝐴𝑖      : coefficient matrix for lag i
        - 𝑝       : order of the VAR model
        - 𝛼𝑡      : vector of white-noise residuals
        """
        
        """st.markdown("""
            ### Model Klasifikasi Support Vector Machine (SVM)
            #We use Classification model Support Vector Machine (SVM) for classified Upwelling potensial
        """)
        
        st.write('#### Kernel Linear')
        # Linear kernel formula
        st.latex(r'''
                    K(x_i, x) = x_i^T x
                    ''')
        
        st.markdown(""" 
        """###### Keterangan:
        - 𝑥𝑖 = Vektor data training
        - 𝑥 = Vektor data testing
        """
        
        """st.write('#### Kernel RBF')
        # Linear kernel formula
        st.latex(r'''
                    K(x_i, x) = \exp\left(- \gamma \left| x_i^T x \right|^2 \right)
                    ''')
        
        st.markdown(""" 
        """###### Keterangan:
        - 𝑥𝑖 = Vektor data training
        - 𝑥 = Vektor data testing
        - 𝛾= gamma
        """
        
        """st.write('#### Kernel Polynomial')
        # Linear kernel formula
        st.latex(r'''
                    K(x_i, x) = (\gamma \cdot x_i^T x + r)^p
                    ''')
        
        st.markdown(""" 
        """###### Keterangan:
        - 𝑥𝑖 = Vektor data training
        - 𝑥 = Vektor data testing
        - 𝛾= gamma
        - 𝑟= coef ()
        - 𝑝 = degree
        """

        # Evaluation Metrics
        st.write('### Evaluation Metrics')
        st.markdown("""
            - All Sky Insolation Clearness Index: MSE = 0,0526, RMSE = 0,2295, MAE = 0,1815
            - Temperature at 2 M                 : MSE = 0,0341, RMSE = 0,1847, MAE = 0,1514
            - Precipitation                      : MSE = 0,0738, RMSE = 0,2721, MAE = 0,2191
            - Surface Pressure                   : MSE = 0,0399, RMSE = 0,1998, MAE = 0,1602
            - Wind Speed                         : MSE = 0,0287, RMSE = 0,1697, MAE = 0,1347
        """)

        # Tools and Technologies
        st.header("Technologies / Tools Used")
        st.markdown("""
            - **Streamlit**              : For building the user interface.
            - **Pandas & R**             : For data manipulation and analysis.
            - **Joblib**                 : For saving and loading machine learning models.
            - **Plotly Express**         : Libraries for creating interactive data visualizations.
        """)

        # Social Media
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

        # Contact
        st.header("Kontak")
        st.markdown("""
            If you have any questions or feedback, please contact us:
        """)
        col_4, col_5 = st.columns(2)
        with col_4:
            st.markdown("""
                - ##### Muhammad Zia Ulhaq
                                """)
            st.image('zz.png')
            st.markdown("""
                    - Email   : [ziaswatfbicia@gmail.com](mailto:ziaswatfbicia@gmail.com) 
                    - LinkedIn: [Muhammad Zia Ulhaq](https://www.linkedin.com/in/muhammad-zia-ulhaq-8373112b9/) 
                                    """)
            st.markdown("""
                - ##### Zahra Ifma Aziza
                                """)
            st.image('z.png')
            st.markdown("""
                    - Email   : [zahraifmaa@gmail.com](mailto:zahraifmaa@gmail.com) 
                    - LinkedIn: [Zahra Ifma Aziza](https://www.linkedin.com/in/zahra-ifma-aziza/) 
                    """)
            st.markdown("""
                - ##### Muhammad Farid
                                """)
            st.image('f.png')
            st.markdown("""
                    - Email   : [mhdfaridz93@gmail.com](mailto:mhdfaridz93@gmail.com) 
                    - LinkedIn: [Muhammad Farid](https://www.linkedin.com/in/mhd-farid/)
            """)
        with col_5:
            st.markdown("""
                - ##### Fakhrus Syakir
                """)
            st.image('s.png')
            st.markdown("""
                    - Email   : [fakhroosyakir@gmail.com](mailto:fakhroosyakir@gmail.com) 
                    - LinkedIn: [Fakhrus Syakir](https://www.linkedin.com/in/fakhrus-syakir-65bb72205/) 
                    """)
                    
            st.markdown("""
                - ##### Teuku Muhammad Faiz Nuzullah
                """)
            st.image('p.png')
            st.markdown("""
                    - Email   : [faiznuzullah@gmail.com](mailto:faiznuzullah@gmail.com) 
                    - LinkedIn: [Teuku Muhammad Faiz Nuzullah](https://www.linkedin.com/in/teuku-muhammad-f-4a906a239) 
                    """)
            st.markdown("""
                - #####  Novi Reandy Sasmita, S.Si., M.Sc.
                """)
            st.image('g.png', use_column_width=True)
            st.markdown("""
                    - Email   : [novireandys@usk.ac.id](mailto:novireandys@usk.ac.id) 
                    - LinkedIn: [Novi Reandy Sasmita](https://www.linkedin.com/in/novi-reandy-sasmita-93371a72/)
                    - Website : [Novi Reandy Sasmita's Website](https://www.reandy.info)
            """)

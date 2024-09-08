import streamlit as st
from streamlit_option_menu import option_menu
from web_function import preprocess_dataframe, load_data
import home
import forecast
import predict
import about

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        # Sidebar
        with st.sidebar:
            # Inject CSS to center images vertically and horizontally
            st.markdown("""
                <style>
                .logo-container {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 150px;  /* Adjust height as needed */
                }
                .sidebar .css-1v3fvcr {
                    background-color: #0f1117 !important;
                }
                </style>
            """, unsafe_allow_html=True)

            # Use columns to display logos side by side, inside a div for centering
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.markdown('<div class="logo-container"><img src="LOGO-USK-MASTER-1-300x166.png" width="80%"></div>', unsafe_allow_html=True)
            with col2:
                st.markdown('<div class="logo-container"><img src="pkmre-upwelling.png" width="80%"></div>', unsafe_allow_html=True)
            with col3:
                st.markdown('<div class="logo-container"><img src="Logo-PKM-Warna.png" width="80%"></div>', unsafe_allow_html=True)
            with col4:
                st.markdown('<div class="logo-container"><img src="83790f2b43f00be.png" width="80%"></div>', unsafe_allow_html=True)

            # Option menu
            app = option_menu(
                menu_title='Dashboard',
                options=['Home', 'Forecast', 'Prediction', 'About'],
                icons=['house-fill', 'cloud-lightning-rain-fill', 'bi-water', 'info-circle-fill'],
                menu_icon='bi-cast',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": '#0f1117'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        # Main content
        if app == "Home":
            home.app()
        elif app == "Forecast":
            forecast.app()
        elif app == "Prediction":
            predict.app()
        elif app == 'About':
            about.app()

# Create an instance of MultiApp and run it
multi_app = MultiApp()
multi_app.run()

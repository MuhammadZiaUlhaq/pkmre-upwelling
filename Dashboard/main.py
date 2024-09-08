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
            # Add logo at the top of the sidebar
            st.image('/Users/fakhrussyakir/Desktop/GIT/pkmre-upwelling/pkmre-upwelling.png', use_column_width=True)

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

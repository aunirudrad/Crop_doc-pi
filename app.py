# app.py
import streamlit as st
from pages.home import home_page
from pages.camera import camera_page
from pages.detection import detection_page
from utils.styles import set_styles

# Set up page configuration
st.set_page_config(
    page_title="Hawkeye-Eagle",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom styles
st.markdown(set_styles(), unsafe_allow_html=True)

# Initialize session state for page navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = "home"

def navigate(page_name):
    st.session_state.current_page = page_name

# Navigation logic
if st.session_state.current_page == "home":
    home_page(navigate)
elif st.session_state.current_page == "camera":
    camera_page(navigate)
elif st.session_state.current_page == "detection":
    detection_page(navigate)

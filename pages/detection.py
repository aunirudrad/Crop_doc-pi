# pages/detection.py
import streamlit as st
from utils.detection_utils import run_detection

def detection_page(navigate):
    crop = st.session_state.get("crop")
    if crop:
        if "uploaded_image" in st.session_state:
            run_detection(crop, st.session_state["uploaded_image"])
        elif "captured_image" in st.session_state:
            run_detection(crop, st.session_state["captured_image"])
        else:
            st.write("No image available for detection.")
    else:
        st.write("No model available for the selected crop.")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Back (পিছনে ফিরে যান)"):
            navigate("camera")
    with col2:
        if st.button("Home (হোমে ফিরে যান)"):
            navigate("home")

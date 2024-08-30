import streamlit as st

def intro_page(navigate):
    st.title("Welcome to Hawkeye-Eagle")

    st.image("images\logo.png", width=400)
    
    # Add Start button
    if st.button("Start"):
        navigate("home")

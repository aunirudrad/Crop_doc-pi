import streamlit as st

def intro_page(navigate):
    st.title("Welcome to Hawkeye-Eagle")
    def display_image():
        st.title("Image Display Example")
        
        # Display image with specific width
        st.image("E:\Budget_ashle_fatai_dibo\hawkeye-agriculture\images\logo-removebg-preview.png", width=400)
    
    # Add Start button
    if st.button("Start"):
        navigate("home")

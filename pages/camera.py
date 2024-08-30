# pages/camera.py
import streamlit as st
from PIL import Image

def camera_page(navigate):
    st.write(f"<div class='title'>{st.session_state.get('crop', 'Camera')}</div>", unsafe_allow_html=True)
    st.write("<div class='sub-title'>Capture or Upload Image</div>", unsafe_allow_html=True)
    st.write("<div class='sub-title'>(ছবি তুলুন বা একটি ছবি আপলোড করুন)</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <div style='text-align: center; font-weight: bold; font-size: 20px;'>Capture Image (ছবি তুলুন)</div>
            <div style='text-align: center;'>Click the button below to capture an image with the camera.</div>
            <div style='text-align: center;'>ক্যামেরা চালু করতে "Open Camera" বাটনে ক্লিক করুন</div>
        """, unsafe_allow_html=True)
        if st.button("Open Camera", key="capture"):
            captured_image = Image.new('RGB', (300, 300), color='gray')
            st.session_state["captured_image"] = captured_image
            st.image(captured_image, caption="Open Image")
            st.write("Image captured!")  
        if st.button("Back (পিছনে ফিরে যান)"):
            navigate("home")

    with col2:
        st.markdown("""
            <div style='text-align: center; font-weight: bold; font-size: 20px;'>Upload Image (ছবি আপলোড করুন)</div>
            <div style='text-align: center;'>Upload an image file from your device to display below.</div>
        """, unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])
        if uploaded_file is not None:
            uploaded_image = Image.open(uploaded_file)
            st.image(uploaded_image, caption="Uploaded Image")
            st.session_state["uploaded_image"] = uploaded_image
        if st.button("Detect (সনাক্ত করুন)"):
            if "captured_image" in st.session_state or "uploaded_image" in st.session_state:
                navigate("detection")
            else:
                st.write("No image captured or uploaded to process!")

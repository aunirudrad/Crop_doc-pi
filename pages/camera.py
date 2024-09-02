# pages/camera.py
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import numpy as np
import cv2
from PIL import Image
from time import sleep
from picamera2 import Picamera2, Preview


class VideoTransformer(VideoTransformerBase):
    def __init__(self):
        self.frame = None

    def transform(self, frame):
        self.frame = frame.to_ndarray(format="bgr24")
        return self.frame

    def get_image(self):
        if self.frame is not None:
            return Image.fromarray(self.frame)
        return None

def camera_page(navigate):
    st.write(f"<div class='title'>{st.session_state.get('crop', 'Camera')}</div>", unsafe_allow_html=True)
    st.write("<div class='sub-title'>Capture or Upload Image</div>", unsafe_allow_html=True)
    st.write("<div class='sub-title'>(ছবি তুলুন বা একটি ছবি আপলোড করুন)</div>", unsafe_allow_html=True)

    picam2 = Picamera2()

    col1, col2 = st.columns(2)
    

    with col1:
        st.markdown("""
            <div style='text-align: center; font-weight: bold; font-size: 20px;'>Capture Image (ছবি তুলুন)</div>
            <div style='text-align: center;'>Click the button below to open the camera and capture an image.</div>
            <div style='text-align: center;'>ক্যামেরা চালু করতে "Open Camera" বাটনে ক্লিক করুন এবং ছবি তুলতে "Capture Image" বাটনে ক্লিক করুন</div>
        """, unsafe_allow_html=True)
        
        # Initialize variables to control camera and image capture
        if "camera_open" not in st.session_state:
            st.session_state.camera_open = False
        
        if "captured_image" not in st.session_state:
            st.session_state.captured_image = None
        
        # Button to open/close the camera
        if st.button("Open Camera", key="open_camera"):
            picam2.start_preview(Preview.QTGL)
            sleep(100)
            
            # Button to capture the image
            if st.button("Capture Image", key="capture_image"):

                capture_image = picam2.capture_image()
                st.image(capture_image, caption="Image captured")
                picam2.stop_preview()
                picam2.close()
                
    
    
    
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

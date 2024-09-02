# pages/camera.py
import streamlit as st
from PIL import Image
from time import sleep
from picamera2 import Picamera2

def initialize_camera():
    # Initialize the Picamera2 object and configure it for still capture
    picam2 = Picamera2()
    still_config = picam2.create_still_configuration()  # Create a configuration for still capture
    picam2.configure(still_config)  # Apply the still configuration
    picam2.start()  # Start the camera
    sleep(100)  # Allow time for the camera to warm up
    return picam2

def camera_page(navigate):
    st.title("Camera Page")

    # Initialize session states if not already done
    if "camera_open" not in st.session_state:
        st.session_state.camera_open = False
    if "picam2" not in st.session_state:
        st.session_state.picam2 = None
    if "captured_image" not in st.session_state:
        st.session_state.captured_image = None

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <div style='text-align: center; font-weight: bold; font-size: 20px;'>Capture Image (ছবি তুলুন)</div>
            <div style='text-align: center;'>Click the button below to open the camera and capture an image.</div>
            <div style='text-align: center;'>ক্যামেরা চালু করতে "Open Camera" বাটনে ক্লিক করুন এবং ছবি তুলতে "Capture Image" বাটনে ক্লিক করুন</div>
        """, unsafe_allow_html=True)

        # Button to open the camera
        if st.button("Open Camera", key="open_camera"):
            if not st.session_state.camera_open:
                st.session_state.picam2 = initialize_camera()  # Initialize and start the camera
                st.session_state.camera_open = True

        # If the camera is open, display a capture button
        if st.session_state.camera_open:
            if st.button("Capture Image", key="capture_image"):
                if st.session_state.picam2:
                    # Capture the image
                    image_array = st.session_state.picam2.capture_array()
                    captured_image = Image.fromarray(image_array)
                    st.session_state.captured_image = captured_image
                    # Display the captured image
                    st.image(captured_image, caption="Image captured", use_column_width=True)
                    # Stop the camera
                    st.session_state.picam2.stop()
                    st.session_state.picam2.close()
                    st.session_state.camera_open = False

    with col2:
        st.markdown("""
            <div style='text-align: center; font-weight: bold; font-size: 20px;'>Upload Image (ছবি আপলোড করুন)</div>
            <div style='text-align: center;'>Upload an image file from your device to display below.</div>
        """, unsafe_allow_html=True)

        uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])
        if uploaded_file is not None:
            uploaded_image = Image.open(uploaded_file)
            st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
            st.session_state["uploaded_image"] = uploaded_image

        if st.button("Detect (সনাক্ত করুন)"):
            if "captured_image" in st.session_state or "uploaded_image" in st.session_state:
                navigate("detection")
            else:
                st.write("No image captured or uploaded to process!")

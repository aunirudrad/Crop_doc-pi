import streamlit as st
from PIL import Image
from time import sleep
# from picamera2 import Picamera2, Preview


def test_camera():

    # try:
    #     picam2 = Picamera2()
    #     picam2.start_preview()
    #     sleep(2)  # Allow some time for the camera to initialize
    #     picam2.capture_file("/home/pi/Desktop/new_image.jpg")
    #     st.image("/home/pi/Desktop/new_image.jpg", caption="Captured Image", use_column_width=True)
    #     picam2.close()
    # except RuntimeError as e:
    #     st.error(f"Error initializing camera: {e}")
    # except Exception as e:
    #     st.error(f"Unexpected error: {e}")
    pass

def camera_page(navigate):
    st.title("Camera Page")

    # Initialize session state variables
    if "camera_open" not in st.session_state:
        st.session_state.camera_open = False
    if "captured_image" not in st.session_state:
        st.session_state.captured_image = None

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Capture Image")
        st.markdown("Click 'Open Camera' to initialize the camera, then click 'Capture Image' to take a picture.")

        # Button to open/initialize the camera
        if st.button("Open Camera"):
            test_camera()

    with col2:
        st.markdown("### Upload Image")
        st.markdown("Upload an image file from your device to display below.")

        uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])
        if uploaded_file is not None:
            uploaded_image = Image.open(uploaded_file)
            st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
            st.session_state["uploaded_image"] = uploaded_image

        if st.button("Detect"):
            if "captured_image" in st.session_state or "uploaded_image" in st.session_state:
                navigate("detection")
            else:
                st.write("No image captured or uploaded to process!")

# Example of calling the camera_page function
# camera_page(navigate=lambda x: st.write(f"Navigation placeholder: {x}"))

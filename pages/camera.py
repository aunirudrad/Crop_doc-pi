import streamlit as st
from PIL import Image
from time import sleep
from picamera2 import Picamera2

def initialize_camera():
    """Initialize and configure the camera."""
    try:
        picam2 = Picamera2()
        still_config = picam2.create_still_configuration()  # Configure for still images
        picam2.configure(still_config)
        return picam2
    except RuntimeError as e:
        st.error(f"Failed to initialize the camera: {e}")
        return None

def start_camera(picam2):
    """Start the camera preview."""
    try:
        picam2.start()  # Start the camera
        sleep(2)  # Give some time for the camera to initialize
        return True
    except Exception as e:
        st.error(f"Error starting the camera: {e}")
        return False

def capture_image(picam2):
    """Capture an image from the camera."""
    try:
        image_array = picam2.capture_array()  # Capture the image as an array
        captured_image = Image.fromarray(image_array)
        return captured_image
    except Exception as e:
        st.error(f"Error capturing image: {e}")
        return None

def stop_camera(picam2):
    """Stop the camera and release resources."""
    try:
        picam2.stop()
        picam2.close()
    except Exception as e:
        st.error(f"Error stopping the camera: {e}")

def camera_page(navigate):
    st.title("Camera Page")

    # Initialize session state variables
    if "camera_open" not in st.session_state:
        st.session_state.camera_open = False
    if "picam2" not in st.session_state:
        st.session_state.picam2 = None
    if "captured_image" not in st.session_state:
        st.session_state.captured_image = None

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Capture Image")
        st.markdown("Click 'Open Camera' to initialize the camera, then click 'Capture Image' to take a picture.")

        # Button to open/initialize the camera
        if st.button("Open Camera"):
            if not st.session_state.camera_open:
                st.session_state.picam2 = initialize_camera()
                if st.session_state.picam2 is not None:
                    camera_started = start_camera(st.session_state.picam2)
                    if camera_started:
                        st.session_state.camera_open = True

        # Button to capture the image
        if st.session_state.camera_open:
            if st.button("Capture Image"):
                if st.session_state.picam2:
                    captured_image = capture_image(st.session_state.picam2)
                    if captured_image:
                        st.session_state.captured_image = captured_image
                        st.image(captured_image, caption="Captured Image", use_column_width=True)

        # Button to close the camera
        if st.session_state.camera_open:
            if st.button("Close Camera"):
                stop_camera(st.session_state.picam2)
                st.session_state.camera_open = False

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
camera_page(navigate=lambda x: st.write(f"Navigation placeholder: {x}"))

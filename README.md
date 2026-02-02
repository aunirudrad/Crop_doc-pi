# Crop_doc-pi 🌾

## Overview
Crop_doc-pi (also known as Hawkeye-Eagle) is an AI-powered crop disease detection system designed to help farmers identify plant diseases early and accurately in real-time. The application leverages deep learning models to analyze crop images and provide instant diagnosis with detailed information about detected diseases, their symptoms, causes, and recommended treatments. With support for multiple crops including Mango, Soybean, and Potato, and a bilingual interface (English and Bengali), this tool makes advanced agricultural diagnostics accessible to farmers.

## Features
- 🎯 **Real-time Disease Detection**: Upload or capture images of crops to instantly detect diseases using AI-powered TensorFlow Lite models
- 🌱 **Multi-Crop Support**: Supports disease detection for multiple crops including:
  - Mango (আম) - Anthracnose, Dag Disease, Galls, Red Rust
  - Soybean (সয়াবিন) - Bacterial Blight, Cercospora Leaf Blight, Downey Mildew, Frogeye, Potassium Deficiency, Soybean Rust
  - Potato (আলু) - Early Blight, Late Blight, Leaf Diseases, Healthy detection
- 📸 **Flexible Image Input**: Capture images using camera or upload existing photos for analysis
- 🌐 **Bilingual Interface**: User-friendly interface in both English and Bengali for wider accessibility
- 📊 **Detailed Disease Information**: Comprehensive descriptions including symptoms, causes, and treatment recommendations
- 🖼️ **Intuitive Navigation**: Easy-to-use multi-page interface with smooth navigation between screens
- 💾 **Automatic Model Management**: Models are automatically downloaded from Google Drive on first run

## Technologies
- **Frontend Framework**: [Streamlit](https://streamlit.io/) - Interactive web application framework
- **Machine Learning**: 
  - [TensorFlow](https://www.tensorflow.org/) - Deep learning framework
  - TensorFlow Lite - Optimized models for efficient inference
- **Image Processing**:
  - [OpenCV](https://opencv.org/) - Computer vision library
  - [Pillow (PIL)](https://python-pillow.org/) - Image manipulation
- **Data Processing**: 
  - [NumPy](https://numpy.org/) - Numerical computing
  - [Pandas](https://pandas.pydata.org/) - Data analysis
- **Additional Tools**:
  - gdown - Google Drive file downloads
  - streamlit-webrtc - Real-time camera integration 

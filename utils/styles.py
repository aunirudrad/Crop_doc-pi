# utils/styles.py

def set_styles():
    """
    Sets the CSS styles for the Streamlit app.
    """
    styles = """
    <style>
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #004d40;
        margin-bottom: 20px;
    }
    .sub-title {
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        color: #00796b;
        margin-bottom: 20px;
    }
    button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px;
        border: none;
        cursor: pointer;
        border-radius: 5px;
    }
    button:hover {
        background-color: #45a049;
    }
    </style>
    """
    return styles

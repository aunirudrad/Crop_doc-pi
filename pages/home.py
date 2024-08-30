# pages/home.py
import streamlit as st

def home_page(navigate):
    st.write("<div class='title'>Hawkeye ~ Eagle</div>", unsafe_allow_html=True)
    st.write("<div class='sub-title'>Click to Detect (রোগ জানতে ট্যাপ করুন)</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Mango (আম)"):
            st.session_state["crop"] = "mango"
            navigate("camera")
        if st.button("Rice (ধান)"):
            st.session_state["crop"] = "ধান"
            navigate("camera")
        if st.button("Papaya (পেঁপে)"):
            st.session_state["crop"] = "পেঁপে"
            navigate("camera")
    with col2:
        if st.button("Lemon (লেবু)"):
            st.session_state["crop"] = "লেবু"
            navigate("camera")
        if st.button("Soybean (সয়াবিন)"):
            st.session_state["crop"] = "soybean"
            navigate("camera")
        if st.button("Potato (আলু)"):
            st.session_state["crop"] = "potato"
            navigate("camera")

    # Navigation button
    if st.button("Next (পরবর্তী ধাপে যান)", key="next"):
        navigate("camera")

import streamlit as st

def show_navbar():

    st.markdown(
        """
        <div style="
            background:#0E1117;
            padding:15px;
            border-radius:10px;
            border:1px solid #31333F;
            margin-bottom:20px;
        ">

        <h2 style="color:white;">
        🛡️ AI Financial Fraud Intelligence
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )
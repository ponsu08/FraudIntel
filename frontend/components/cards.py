import streamlit as st

def metric_card(title, value, delta=None):

    st.metric(
        label=title,
        value=value,
        delta=delta
    )


def info_card(title, text):

    st.markdown(
        f"""
        <div style="
        background:#1E1E1E;
        padding:20px;
        border-radius:12px;
        border-left:5px solid #00C853;
        ">

        <h4 style="color:white;">{title}</h4>

        <p style="color:#DDDDDD;">
        {text}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )
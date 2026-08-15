import streamlit as st

st.set_page_config(
    page_title="Settings",
    layout="wide"
)

st.title("⚙ Settings")

st.subheader("Backend")

backend = st.text_input(
    "Backend URL",
    value="http://127.0.0.1:8000"
)

st.subheader("Appearance")

theme = st.selectbox(
    "Theme",
    [
        "Dark",
        "Light"
    ]
)

st.subheader("Notifications")

email_alert = st.checkbox(
    "Email Alerts",
    value=True
)

sound = st.checkbox(
    "Sound Alerts",
    value=False
)

st.subheader("Reports")

auto_export = st.checkbox(
    "Auto Export Reports"
)

if st.button("Save Settings"):

    st.success("Settings saved successfully.")
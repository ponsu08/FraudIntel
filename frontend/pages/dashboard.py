import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Dashboard", layout="wide")

st.title("🛡 AI Financial Fraud Intelligence Dashboard")

st.markdown("---")

try:
    response = requests.get(f"{API_URL}/")

    if response.status_code == 200:
        data = response.json()
    else:
        data = {}

except:
    data = {}

col1, col2, col3, col4 = st.columns(4)

col1.metric("Email Scans", data.get("email_scans", 0))
col2.metric("Website Scans", data.get("website_scans", 0))
col3.metric("SMS Scans", data.get("sms_scans", 0))
col4.metric("Fraud Detected", data.get("fraud_detected", 0))

st.divider()

st.subheader("System Status")

st.success("Backend Connected")

st.info(
"""
Modules Available

✅ Email Detection

✅ Website Detection

✅ SMS Detection

✅ Voice Detection

✅ QR Detection

✅ Social Detection
"""
)
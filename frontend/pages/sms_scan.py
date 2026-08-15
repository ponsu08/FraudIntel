import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="SMS Scanner", layout="wide")

st.title("📱 SMS Fraud Scanner")

st.write("Paste the SMS message below.")

sms = st.text_area(
    "SMS Message",
    height=200,
    placeholder="Enter SMS content..."
)

if st.button("Scan SMS", use_container_width=True):

    if not sms.strip():
        st.warning("Please enter an SMS message.")
        st.stop()

    with st.spinner("Scanning SMS..."):

        try:

            response = requests.post(
                f"{API_URL}/sms",
                json={"text": sms}
            )

            if response.status_code == 200:

                result = response.json()

                st.success("Analysis Complete")

                col1, col2, col3 = st.columns(3)

                col1.metric(
                    "Prediction",
                    result.get("prediction", "Unknown")
                )

                col2.metric(
                    "Risk Score",
                    f"{result.get('risk_score',0)}%"
                )

                col3.metric(
                    "Confidence",
                    f"{result.get('confidence',0)}%"
                )

                st.subheader("Explanation")
                st.write(result.get("explanation", "No explanation available."))

            else:
                st.error(response.text)

        except Exception as e:
            st.error(f"Connection Error: {e}")
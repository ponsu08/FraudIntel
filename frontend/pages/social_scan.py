import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Social Media Scanner",
    layout="wide"
)

st.title("💬 Social Media Fraud Scanner")

st.write("Paste the social media message or post.")

text = st.text_area(
    "Message",
    height=220,
    placeholder="Paste WhatsApp, Instagram, Facebook, Telegram, or X message..."
)

if st.button("Analyze Message", use_container_width=True):

    if not text.strip():
        st.warning("Please enter a message.")
        st.stop()

    with st.spinner("Analyzing..."):

        try:

            response = requests.post(
                f"{API_URL}/social",
                json={
                    "text": text
                }
            )

            if response.status_code == 200:

                result = response.json()

                st.success("Analysis Completed")

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

                st.write(
                    result.get(
                        "explanation",
                        "No explanation available."
                    )
                )

            else:

                st.error(response.text)

        except Exception as e:

            st.error(str(e))
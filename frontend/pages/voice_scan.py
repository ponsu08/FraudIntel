import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Voice Scanner", layout="wide")

st.title("🎤 Voice Fraud Scanner")

uploaded_file = st.file_uploader(
    "Upload Voice Recording",
    type=["wav", "mp3", "m4a"]
)

if uploaded_file is not None:

    st.audio(uploaded_file)

    if st.button("Analyze Voice", use_container_width=True):

        with st.spinner("Analyzing Voice..."):

            try:

                files = {
                    "file": (
                        uploaded_file.name,
                        uploaded_file.getvalue(),
                        uploaded_file.type
                    )
                }

                response = requests.post(
                    f"{API_URL}/voice",
                    files=files
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

                    st.subheader("Transcript")

                    st.write(
                        result.get("transcript", "No transcript available.")
                    )

                    st.subheader("Explanation")

                    st.write(
                        result.get("explanation", "No explanation available.")
                    )

                else:

                    st.error(response.text)

            except Exception as e:

                st.error(f"Connection Error: {e}")
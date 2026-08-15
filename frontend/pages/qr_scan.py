import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="QR Scanner", layout="wide")

st.title("🔳 QR Code Fraud Scanner")

uploaded_image = st.file_uploader(
    "Upload QR Code Image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_image is not None:

    st.image(uploaded_image, use_container_width=True)

    if st.button("Scan QR Code", use_container_width=True):

        with st.spinner("Scanning QR Code..."):

            try:

                files = {
                    "file": (
                        uploaded_image.name,
                        uploaded_image.getvalue(),
                        uploaded_image.type
                    )
                }

                response = requests.post(
                    f"{API_URL}/qr",
                    files=files
                )

                if response.status_code == 200:

                    result = response.json()

                    st.success("QR Analysis Completed")

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

                    st.subheader("Decoded Content")

                    st.code(
                        result.get("decoded_text", "No data found.")
                    )

                    st.subheader("Explanation")

                    st.write(
                        result.get("explanation", "No explanation available.")
                    )

                else:

                    st.error(response.text)

            except Exception as e:

                st.error(f"Connection Error: {e}")
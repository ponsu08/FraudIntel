import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("🌐 Website Fraud Scanner")

url = st.text_input(
    "Enter Website URL",
    placeholder="https://example.com"
)

if st.button("Scan Website"):

    if url == "":
        st.warning("Enter a URL.")
        st.stop()

    with st.spinner("Checking Website..."):

        try:

            response = requests.post(
                f"{API_URL}/website",
                json={
                    "url": url
                }
            )

            if response.status_code == 200:

                result = response.json()

                st.success("Scan Completed")

                st.metric(
                    "Prediction",
                    result.get("prediction","")
                )

                st.metric(
                    "Risk Score",
                    f"{result.get('risk_score',0)}%"
                )

                st.metric(
                    "Confidence",
                    f"{result.get('confidence',0)}%"
                )

                st.subheader("Explanation")

                st.write(
                    result.get("explanation","")
                )

            else:

                st.error(response.text)

        except Exception as e:

            st.error(str(e))
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("📧 Email Fraud Scanner")

st.write("Paste an email below.")

email = st.text_area(
    "Email Content",
    height=250
)

if st.button("Scan Email"):

    if email.strip() == "":
        st.warning("Enter an email.")
        st.stop()

    with st.spinner("Scanning..."):

        try:

            response = requests.post(
                f"{API_URL}/email",
                json={
                    "text": email
                }
            )

            if response.status_code == 200:

                result = response.json()

                st.success("Analysis Complete")

                st.metric(
                    "Prediction",
                    result.get("prediction", "")
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
                    result.get("explanation","No explanation.")
                )

            else:

                st.error(response.text)

        except Exception as e:

            st.error(str(e))
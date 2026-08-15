import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Reports",
    layout="wide"
)

st.title("📄 Fraud Detection Reports")

try:

    response = requests.get(
        f"{API_URL}/report"
    )

    if response.status_code == 200:

        reports = response.json()

        if isinstance(reports, list) and len(reports) > 0:

            df = pd.DataFrame(reports)

            st.dataframe(
                df,
                use_container_width=True
            )

            csv = df.to_csv(index=False).encode("utf-8")

            st.download_button(
                "⬇ Download CSV",
                csv,
                "fraud_report.csv",
                "text/csv"
            )

        else:

            st.info("No reports available.")

    else:

        st.error(response.text)

except Exception as e:

    st.error(str(e))

st.divider()

if st.button("Download PDF Report"):

    try:

        response = requests.get(
            f"{API_URL}/report/download"
        )

        if response.status_code == 200:

            st.download_button(
                "Save PDF",
                response.content,
                "fraud_report.pdf",
                mime="application/pdf"
            )

        else:

            st.warning("PDF report not available.")

    except Exception as e:

        st.error(str(e))
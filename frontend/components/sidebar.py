import streamlit as st

def show_sidebar():

    with st.sidebar:

        st.title("🛡 AI Fraud")

        st.markdown("---")

        st.page_link(
            "pages/dashboard.py",
            label="Dashboard",
            icon="📊"
        )

        st.page_link(
            "pages/email_scan.py",
            label="Email Scanner",
            icon="📧"
        )

        st.page_link(
            "pages/website_scan.py",
            label="Website Scanner",
            icon="🌐"
        )

        st.page_link(
            "pages/sms_scan.py",
            label="SMS Scanner",
            icon="📱"
        )

        st.page_link(
            "pages/voice_scan.py",
            label="Voice Scanner",
            icon="🎤"
        )

        st.page_link(
            "pages/qr_scan.py",
            label="QR Scanner",
            icon="🔳"
        )

        st.page_link(
            "pages/social_scan.py",
            label="Social Scanner",
            icon="💬"
        )

        st.page_link(
            "pages/reports.py",
            label="Reports",
            icon="📄"
        )

        st.page_link(
            "pages/settings.py",
            label="Settings",
            icon="⚙"
        )
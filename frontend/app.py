import streamlit as st
from PIL import Image

# ===========================
# PAGE CONFIG
# ===========================

st.set_page_config(
    page_title="AI Financial Fraud Intelligence",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===========================
# LOAD CSS
# ===========================

def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )
    except FileNotFoundError:
        pass

local_css("assets/css/style.css")

# ===========================
# SIDEBAR
# ===========================

with st.sidebar:

    try:
        logo = Image.open("assets/images/logo.png")
        st.image(logo, width=90)
    except:
        st.markdown("# 🛡️")

    st.title("AI Fraud")

    st.caption("Cyber Security Dashboard")

    st.divider()

    st.page_link("app.py", label="Dashboard", icon="📊")
    st.page_link("pages/email_scan.py", label="Email Scanner", icon="📧")
    st.page_link("pages/website_scan.py", label="Website Scanner", icon="🌐")
    st.page_link("pages/sms_scan.py", label="SMS Scanner", icon="📱")
    st.page_link("pages/voice_scan.py", label="Voice Scanner", icon="🎤")
    st.page_link("pages/qr_scan.py", label="QR Scanner", icon="🔳")
    st.page_link("pages/social_scan.py", label="Social Scanner", icon="💬")
    st.page_link("pages/reports.py", label="Reports", icon="📄")
    st.page_link("pages/settings.py", label="Settings", icon="⚙️")

# ===========================
# HERO SECTION
# ===========================

left, right = st.columns([2, 1])

with left:

    st.markdown("""
# 🛡️ AI Financial Fraud Intelligence

### Detect • Analyze • Prevent Financial Fraud using Artificial Intelligence

Protect users from phishing emails, fake websites, SMS scams,
voice fraud, QR attacks, and malicious social media messages.

""")

    c1, c2 = st.columns(2)

    with c1:
        st.button("🚀 Start Scanning", use_container_width=True)

    with c2:
        st.button("📄 View Reports", use_container_width=True)

with right:

    try:
        banner = Image.open("assets/images/banner.png")
        st.image(banner, use_container_width=True)
    except:
        st.info("Add banner.png to assets/images")

st.divider()

# ===========================
# KPI CARDS
# ===========================

st.subheader("📊 Threat Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Scans",
        "1,248",
        "+14%"
    )

with col2:
    st.metric(
        "Frauds Detected",
        "96",
        "+8"
    )

with col3:
    st.metric(
        "Safe Requests",
        "1,152",
        "+6%"
    )

with col4:
    st.metric(
        "Detection Accuracy",
        "98.7%",
        "+0.4%"
    )

st.divider()

# ===========================
# FEATURES
# ===========================

st.subheader("🚀 Platform Features")

r1 = st.columns(3)

with r1[0]:
    st.info("""
### 🤖 AI Detection

Machine Learning models identify
fraudulent activities in real time.
""")

with r1[1]:
    st.info("""
### 🧠 Explainable AI

Every prediction includes
an understandable explanation.
""")

with r1[2]:
    st.info("""
### ⚡ Instant Analysis

Risk scores are generated
within seconds.
""")

st.divider()

# ===========================
# MODULES
# ===========================

st.subheader("🛡️ Detection Modules")

row1 = st.columns(3)

with row1[0]:
    st.success("📧 Email Phishing")

with row1[1]:
    st.success("🌐 Website Fraud")

with row1[2]:
    st.success("📱 SMS Scam")

row2 = st.columns(3)

with row2[0]:
    st.success("🎤 Voice Scam")

with row2[1]:
    st.success("🔳 QR Fraud")

with row2[2]:
    st.success("💬 Social Media Fraud")

st.divider()

# ===========================
# HOW IT WORKS
# ===========================

st.subheader("🔄 Detection Pipeline")

st.markdown """
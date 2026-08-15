import os
from dotenv import load_dotenv

load_dotenv()

# ====================================
# API Keys
# ====================================

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY", "")

# ====================================
# Database
# ====================================

DATABASE_URL = "sqlite:///database/fraud_logs.db"

# ====================================
# Model Paths
# ====================================

EMAIL_MODEL = "models/email_model.pkl"

SMS_MODEL = "models/sms_model.pkl"

WEBSITE_MODEL = "models/website_model.pkl"

VOICE_MODEL = "models/voice_model.pkl"

QR_MODEL = "models/qr_model.pkl"

SOCIAL_MODEL = "models/social_model.pkl"

SCALER_PATH = "models/scaler.pkl"

# ====================================
# Upload Folder
# ====================================

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ====================================
# Supported File Types
# ====================================

ALLOWED_IMAGE_TYPES = [
    ".jpg",
    ".jpeg",
    ".png"
]

ALLOWED_AUDIO_TYPES = [
    ".wav",
    ".mp3",
    ".m4a"
]

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB
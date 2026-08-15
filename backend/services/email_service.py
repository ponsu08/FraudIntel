"""
Email Phishing Detection Service
"""

import os
import joblib

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "email_model.pkl"
)

# Load model only once
email_model = joblib.load(MODEL_PATH)


class EmailService:

    @staticmethod
    def predict(email_text: str):

        if not email_text.strip():
            return {
                "success": False,
                "message": "Email text is empty."
            }

        prediction = email_model.predict([email_text])[0]

        try:
            probability = email_model.predict_proba([email_text])[0]
            confidence = round(max(probability) * 100, 2)
        except Exception:
            confidence = None

        return {
            "success": True,
            "prediction": int(prediction),
            "label": "Phishing" if prediction == 1 else "Legitimate",
            "confidence": confidence
        }
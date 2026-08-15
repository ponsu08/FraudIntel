"""
Social Media Phishing Detection Service

Detects phishing content in:
- Facebook posts
- Instagram messages
- WhatsApp forwards
- Telegram messages
- Twitter/X posts
- LinkedIn messages
"""

import os
import joblib

# ------------------------------------------------------
# Model Path
# ------------------------------------------------------

BASE_DIR = os.path.dirname(__file__)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "..",
    "models",
    "social_model.pkl"
)

# ------------------------------------------------------
# Load Trained Model
# ------------------------------------------------------

social_model = joblib.load(MODEL_PATH)


# ------------------------------------------------------
# Social Media Service
# ------------------------------------------------------

class SocialService:

    @staticmethod
    def predict(text: str):
        """
        Predict whether a social media message is phishing.
        """

        if text is None or len(text.strip()) == 0:
            return {
                "success": False,
                "message": "Social media text cannot be empty."
            }

        # Predict
        prediction = social_model.predict([text])[0]

        # Prediction probability
        try:
            probability = social_model.predict_proba([text])[0]
            confidence = round(max(probability) * 100, 2)
        except Exception:
            confidence = None

        # Risk level
        if confidence is None:
            risk_level = "Unknown"
        elif confidence >= 90:
            risk_level = "Critical"
        elif confidence >= 75:
            risk_level = "High"
        elif confidence >= 50:
            risk_level = "Medium"
        else:
            risk_level = "Low"

        # Suggested action
        if prediction == 1:
            recommendation = (
                "Do not click any links, do not download attachments, "
                "and report the message as phishing."
            )
        else:
            recommendation = (
                "No phishing indicators detected."
            )

        return {
            "success": True,
            "prediction": int(prediction),
            "label": (
                "Phishing"
                if prediction == 1
                else "Legitimate"
            ),
            "confidence": confidence,
            "risk_level": risk_level,
            "recommendation": recommendation
        }
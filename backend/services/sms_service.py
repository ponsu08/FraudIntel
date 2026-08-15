"""
SMS Phishing (Smishing) Detection Service
"""

import os
import joblib

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "sms_model.pkl"
)

# Load trained model
sms_model = joblib.load(MODEL_PATH)


class SMSService:

    @staticmethod
    def predict(sms_text: str):

        if not sms_text.strip():
            return {
                "success": False,
                "message": "SMS text is empty."
            }

        prediction = sms_model.predict([sms_text])[0]

        try:
            probability = sms_model.predict_proba([sms_text])[0]
            confidence = round(max(probability) * 100, 2)
        except Exception:
            confidence = None

        return {
            "success": True,
            "prediction": int(prediction),
            "label": "Smishing" if prediction == 1 else "Legitimate",
            "confidence": confidence
        }
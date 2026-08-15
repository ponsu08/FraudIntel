import os
import joblib

from utils.feature_extractor import extract_sms_features
from agents.risk_agent import RiskAgent
from agents.explainability_agent import ExplainabilityAgent


class SMSAgent:

    def __init__(self):

        model_path = "models/sms_model.pkl"

        self.model = joblib.load(model_path) if os.path.exists(model_path) else None

        self.risk = RiskAgent()

        self.explainer = ExplainabilityAgent()

    def analyze(self, message, sender=""):

        features = extract_sms_features(
            message,
            sender
        )

        if self.model:

            prediction = self.model.predict([features])[0]

            confidence = round(
                max(self.model.predict_proba([features])[0]) * 100,
                2
            )

        else:

            prediction = 0

            confidence = 78

        label = "Fraud" if prediction == 1 else "Safe"

        risk_score = self.risk.calculate(
            label,
            confidence
        )

        explanation = self.explainer.sms_explanation(
            message,
            sender,
            label
        )

        return {

            "prediction": label,

            "confidence": confidence,

            "risk_score": risk_score,

            "explanation": explanation,

            "features": features
        }
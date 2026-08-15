import joblib
import os

from utils.feature_extractor import extract_email_features
from agents.risk_agent import RiskAgent
from agents.explainability_agent import ExplainabilityAgent


class EmailAgent:

    def __init__(self):

        model_path = "models/email_model.pkl"

        self.model = joblib.load(model_path) if os.path.exists(model_path) else None

        self.risk = RiskAgent()

        self.explainer = ExplainabilityAgent()

    def analyze(self, subject, body, sender=""):

        features = extract_email_features(
            subject,
            body,
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

            confidence = 80.0

        label = "Fraud" if prediction == 1 else "Safe"

        risk_score = self.risk.calculate(label, confidence)

        explanation = self.explainer.email_explanation(
            subject,
            body,
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
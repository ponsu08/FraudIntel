import os
import joblib

from utils.speech_to_text import speech_to_text
from utils.feature_extractor import extract_voice_features

from agents.risk_agent import RiskAgent
from agents.explainability_agent import ExplainabilityAgent


class VoiceAgent:
    def __init__(self):
        model_path = "models/voice_model.pkl"

        self.model = None
        if os.path.exists(model_path):
            self.model = joblib.load(model_path)

        self.risk = RiskAgent()
        self.explainer = ExplainabilityAgent()

    def analyze(self, audio_path):
        # Convert speech to text
        transcript = speech_to_text(audio_path)

        if not transcript:
            return {
                "prediction": "Unknown",
                "confidence": 0.0,
                "risk_score": 0,
                "transcript": "",
                "features": None,
                "explanation": "Unable to recognize speech from the uploaded audio."
            }

        # Extract features
        features = extract_voice_features(transcript)

        # Default prediction
        prediction = 0
        confidence = 80.0

        # Use trained model if available
        if self.model is not None:
            prediction = int(self.model.predict([features])[0])

            if hasattr(self.model, "predict_proba"):
                confidence = round(
                    max(self.model.predict_proba([features])[0]) * 100,
                    2,
                )

        label = "Fraud" if prediction == 1 else "Safe"

        # Risk score
        risk_score = self.risk.calculate(label, confidence)

        # Generate explanation
        explanation = self.explainer.voice_explanation(
            transcript,
            label,
        )

        return {
            "prediction": label,
            "confidence": confidence,
            "risk_score": risk_score,
            "transcript": transcript,
            "features": features,
            "explanation": explanation,
        }
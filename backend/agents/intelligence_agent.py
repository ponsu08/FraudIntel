from agents.email_agent import EmailAgent
from agents.website_agent import WebsiteAgent
from agents.sms_agent import SMSAgent
from agents.voice_agent import VoiceAgent
from agents.qr_agent import QRAgent
from agents.social_agent import SocialAgent

from agents.risk_agent import RiskAgent
from agents.explainability_agent import ExplainabilityAgent


class IntelligenceAgent:

    def __init__(self):

        self.email_agent = EmailAgent()
        self.website_agent = WebsiteAgent()
        self.sms_agent = SMSAgent()
        self.voice_agent = VoiceAgent()
        self.qr_agent = QRAgent()
        self.social_agent = SocialAgent()

        self.risk_agent = RiskAgent()
        self.explainer = ExplainabilityAgent()

    def process(self, analysis_type, data):

        analysis_type = analysis_type.lower()

        try:

            if analysis_type == "email":

                result = self.email_agent.analyze(
                    subject=data.get("subject", ""),
                    body=data.get("body", ""),
                    sender=data.get("sender", "")
                )

            elif analysis_type == "website":

                result = self.website_agent.analyze(
                    data.get("url", "")
                )

            elif analysis_type == "sms":

                result = self.sms_agent.analyze(
                    message=data.get("message", ""),
                    sender=data.get("sender", "")
                )

            elif analysis_type == "voice":

                result = self.voice_agent.analyze(
                    data.get("audio_path", "")
                )

            elif analysis_type == "qr":

                result = self.qr_agent.analyze(
                    data.get("image_path", "")
                )

            elif analysis_type == "social":

                result = self.social_agent.analyze(
                    text=data.get("text", ""),
                    username=data.get("username", "")
                )

            else:

                return {

                    "success": False,

                    "message": f"Unsupported analysis type: {analysis_type}"
                }

            risk_level = self.risk_agent.level(
                result["risk_score"]
            )

            return {

                "success": True,

                "module": analysis_type,

                "prediction": result["prediction"],

                "confidence": result["confidence"],

                "risk_score": result["risk_score"],

                "risk_level": risk_level,

                "explanation": result["explanation"],

                "data": result
            }

        except Exception as e:

            return {

                "success": False,

                "error": str(e)
            }

    def analyze_multiple(self, requests):

        """
        Analyze multiple fraud inputs at once.

        requests example:

        [
            {
                "type":"email",
                "data":{...}
            },
            {
                "type":"sms",
                "data":{...}
            }
        ]
        """

        results = []

        for request in requests:

            result = self.process(

                request["type"],

                request["data"]

            )

            results.append(result)

        summary = self.explainer.overall_summary(results)

        return {

            "total_checks": len(results),

            "results": results,

            "summary": summary
        }
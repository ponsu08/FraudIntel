class ExplainabilityAgent:

    """
    Generates explanations for every prediction.
    """

    def email_explanation(self, subject, body, sender, prediction):

        if prediction == "Fraud":

            return (
                "The email was classified as fraudulent because it "
                "contains suspicious keywords, urgent language, "
                "possible phishing patterns, or suspicious sender details."
            )

        return (
            "The email appears legitimate. No significant phishing "
            "patterns or malicious indicators were detected."
        )

    def website_explanation(self, url, prediction):

        if prediction == "Fraud":

            return (
                "The website appears suspicious because of abnormal URL "
                "structure, possible impersonation, or unsafe domain features."
            )

        return (
            "The website appears safe based on URL structure and extracted features."
        )

    def sms_explanation(self, message, sender, prediction):

        if prediction == "Fraud":

            return (
                "The SMS contains characteristics commonly found in scam "
                "messages such as urgency, fake rewards, suspicious links, "
                "or requests for personal information."
            )

        return (
            "No strong scam indicators were detected in the SMS."
        )

    def voice_explanation(self, transcript, prediction):

        if prediction == "Fraud":

            return (
                "The voice transcript contains suspicious conversational "
                "patterns often associated with fraud calls, including "
                "pressure tactics and requests for sensitive information."
            )

        return (
            "No major fraud indicators were detected in the conversation."
        )

    def qr_explanation(self, qr_content, prediction):

        if prediction == "Fraud":

            return (
                "The QR code redirects to content that appears suspicious "
                "or contains unsafe links and potentially malicious destinations."
            )

        return (
            "The QR code appears safe based on the decoded content."
        )

    def social_explanation(self, text, username, prediction):

        if prediction == "Fraud":

            return (
                "The social media content contains indicators such as fake "
                "offers, impersonation, phishing language, or suspicious links."
            )

        return (
            "No major fraud indicators were found in the social media content."
        )

    def overall_summary(self, results):

        fraud_count = 0

        for result in results:

            if result["prediction"] == "Fraud":
                fraud_count += 1

        if fraud_count == 0:

            return "Overall analysis indicates a low probability of fraudulent activity."

        elif fraud_count == 1:

            return "One module detected suspicious activity. Manual verification is recommended."

        elif fraud_count <= 3:

            return "Multiple fraud indicators were detected. Exercise caution before proceeding."

        else:

            return (
                "Critical warning: Several modules identified strong fraud "
                "indicators. Immediate action is recommended."
            )
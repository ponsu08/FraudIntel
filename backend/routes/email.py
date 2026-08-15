from fastapi import APIRouter
from pydantic import BaseModel

from agents.email_agent import EmailAgent

router = APIRouter()

agent = EmailAgent()


class EmailRequest(BaseModel):
    subject: str
    body: str
    sender: str = ""


@router.post("/analyze")
def analyze_email(request: EmailRequest):
    """
    Analyze an email for phishing or fraud.
    """
    result = agent.analyze(
        subject=request.subject,
        body=request.body,
        sender=request.sender
    )

    return {
        "success": True,
        "module": "Email",
        "result": result
    }


@router.get("/health")
def health():
    return {
        "module": "Email",
        "status": "Running"
    }
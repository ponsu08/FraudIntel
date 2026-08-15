from fastapi import APIRouter
from pydantic import BaseModel

from agents.sms_agent import SMSAgent

router = APIRouter()

agent = SMSAgent()


class SMSRequest(BaseModel):
    message: str
    sender: str = ""


@router.post("/analyze")
def analyze_sms(request: SMSRequest):
    """
    Analyze an SMS message.
    """
    result = agent.analyze(
        message=request.message,
        sender=request.sender
    )

    return {
        "success": True,
        "module": "SMS",
        "result": result
    }


@router.get("/health")
def health():
    return {
        "module": "SMS",
        "status": "Running"
    }
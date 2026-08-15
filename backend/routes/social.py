from fastapi import APIRouter
from pydantic import BaseModel

from agents.social_agent import SocialAgent

router = APIRouter()

agent = SocialAgent()


class SocialRequest(BaseModel):
    text: str
    username: str = ""


@router.post("/analyze")
def analyze_social(request: SocialRequest):
    """
    Analyze a social media message/post.
    """

    result = agent.analyze(
        text=request.text,
        username=request.username
    )

    return {
        "success": True,
        "module": "Social",
        "result": result
    }


@router.get("/health")
def health():
    return {
        "module": "Social",
        "status": "Running"
    }
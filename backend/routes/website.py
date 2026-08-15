from fastapi import APIRouter
from pydantic import BaseModel

from agents.website_agent import WebsiteAgent

router = APIRouter()

agent = WebsiteAgent()


class WebsiteRequest(BaseModel):
    url: str


@router.post("/analyze")
def analyze_website(request: WebsiteRequest):
    """
    Analyze a website URL.
    """
    result = agent.analyze(request.url)

    return {
        "success": True,
        "module": "Website",
        "result": result
    }


@router.get("/health")
def health():
    return {
        "module": "Website",
        "status": "Running"
    }
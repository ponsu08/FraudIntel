from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.email import router as email_router
from routes.website import router as website_router
from routes.sms import router as sms_router
from routes.voice import router as voice_router
from routes.qr import router as qr_router
from routes.social import router as social_router
from routes.orchestrator import router as orchestrator_router
from routes.report import router as report_router

app = FastAPI(
    title="AI Fraud Detection System",
    description="Multi-Agent AI Fraud Detection Backend",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Routes
app.include_router(email_router, prefix="/email", tags=["Email"])

app.include_router(website_router, prefix="/website", tags=["Website"])

app.include_router(sms_router, prefix="/sms", tags=["SMS"])

app.include_router(voice_router, prefix="/voice", tags=["Voice"])

app.include_router(qr_router, prefix="/qr", tags=["QR"])

app.include_router(social_router, prefix="/social", tags=["Social"])

app.include_router(orchestrator_router, prefix="/analyze", tags=["Orchestrator"])

app.include_router(report_router, prefix="/report", tags=["Report"])


@app.get("/")
def home():
    return {
        "message": "AI Fraud Detection API Running",
        "status": "Success",
        "version": "1.0"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }
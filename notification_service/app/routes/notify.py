from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from app.models import NotificationLog
from datetime import datetime
from app.email_utils import send_email_notification  
from dotenv import load_dotenv

load_dotenv()
router = APIRouter()

class NotifyRequest(BaseModel):
    to_email: EmailStr
    subject: str
    body: str


class EmailOnly(BaseModel):
    email: EmailStr



@router.post("/notify/welcome")
async def send_welcome_email(payload: EmailOnly):
    subject = "🎉 Welcome to SecureChat(ewww so cringe)!"
    name = payload.email.split("@")[0]
    body = f"Hi {name}, thanks for signing up! You're now part of the SecureChat family 💬(even more cringe)"
    await send_email_notification(payload.email, subject, body)
    return {"message": "Welcome email sent"}

@router.post("/notify/login")
async def send_login_alert(payload: EmailOnly):
    subject = "🔐 Login Alert"
    body = f"A new login occurred on your account at {datetime.utcnow().isoformat()}."
    await send_email_notification(payload.email, subject, body)
    return {"message": "Login alert email sent"}
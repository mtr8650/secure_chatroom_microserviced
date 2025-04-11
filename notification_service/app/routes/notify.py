from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from app.models import NotificationLog
from datetime import datetime

router = APIRouter()

class NotifyRequest(BaseModel):
    to_email: EmailStr
    subject: str
    body: str

@router.post("/notify")
async def send_notification(payload: NotifyRequest):
    log = NotificationLog(
        recipient_email=payload.to_email,
        subject=payload.subject,
        content=payload.body,
        sent_at=datetime.utcnow()
    )
    await log.insert()
    return {"message": "Notification logged"}

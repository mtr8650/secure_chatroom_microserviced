from beanie import Document
from pydantic import Field
from datetime import datetime

class NotificationLog(Document):
    recipient_email: str
    subject: str
    content: str
    sent_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "notification_logs"

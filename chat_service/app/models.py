from beanie import Document
from pydantic import Field
from datetime import datetime

class Message(Document):
    sender_id: str
    receiver_id: str
    content: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "messages"

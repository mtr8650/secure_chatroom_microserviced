from beanie import Document
from pydantic import Field
from datetime import datetime

class UserProfile(Document):
    username: str
    bio: str | None = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "profiles"

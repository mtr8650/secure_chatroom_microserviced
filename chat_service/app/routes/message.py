from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.models import Message
from datetime import datetime
from typing import List
from app.dependencies import get_current_user

router = APIRouter()

class MessageRequest(BaseModel):
    receiver_id: str
    content: str

@router.post("/messages")
async def send_message(
    data: MessageRequest,
    user: dict = Depends(get_current_user)
):
    message = Message(
        sender_id=user["user_id"],
        receiver_id=data.receiver_id,
        content=data.content,
        timestamp=datetime.utcnow()
    )
    await message.insert()
    return {"message": "Message sent", "id": str(message.id)}

@router.get("/messages/{receiver_id}")
async def get_messages(
    receiver_id: str,
    user: dict = Depends(get_current_user)
) -> List[Message]:
    messages = await Message.find(
        {
            "$or": [
                {"sender_id": user["user_id"], "receiver_id": receiver_id},
                {"sender_id": receiver_id, "receiver_id": user["user_id"]}
            ]
        }
    ).sort("timestamp").to_list()

    return messages

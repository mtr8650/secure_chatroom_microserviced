from fastapi import APIRouter
from pydantic import BaseModel
from app.models import Message
from datetime import datetime
from fastapi import Query
from typing import List

router = APIRouter()

class MessageRequest(BaseModel):
    sender_id: str
    receiver_id: str
    content: str

@router.post("/message")
async def send_message(data: MessageRequest):
    message = Message(
        sender_id=data.sender_id,
        receiver_id=data.receiver_id,
        content=data.content,
        timestamp=datetime.utcnow()
    )
    await message.insert()
    return {"message": "Message sent", "id": str(message.id)}


@router.get("/messages")
async def get_messages(
    sender_id: str = Query(...),
    receiver_id: str = Query(...)
) -> List[Message]:
    messages = await Message.find(
        {
            "$or": [
                {"sender_id": sender_id, "receiver_id": receiver_id},
                {"sender_id": receiver_id, "receiver_id": sender_id}
            ]
        }
    ).sort("timestamp").to_list()
    
    return messages

from fastapi import APIRouter
from app.database import db
from app.models import UserProfile

router = APIRouter()

@router.get("/users")
async def get_users():
    users = await db["users"].find().to_list(100)
    print("Fetched users:", users)  
    return [{"id": str(user["_id"]), "email": user["email"]} for user in users]

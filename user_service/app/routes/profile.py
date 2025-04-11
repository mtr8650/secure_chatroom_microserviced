from fastapi import APIRouter, HTTPException ,Depends
from app.models import UserProfile
from beanie import PydanticObjectId
from app.dependencies import get_current_user

router = APIRouter()

@router.get("/profile")
async def get_profile(user_data: dict = Depends(get_current_user)):
    return {
        "message": "Authenticated access granted!",
        "user": user_data
    }
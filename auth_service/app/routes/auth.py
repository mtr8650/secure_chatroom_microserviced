from fastapi import APIRouter, HTTPException
from app.models import User
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
import httpx
from app.utils.jwt_utils import create_jwt_token
from datetime import datetime

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str   

@router.post("/register")
async def register_user(payload: RegisterRequest):
    existing = await User.find_one(User.email == payload.email)
    if existing:
        raise HTTPException(status_code=400, detail="This email has already been registered!")

    hashed = pwd_context.hash(payload.password)
    user = User(email=payload.email, hashed_password=hashed)
    await user.insert()
    async with httpx.AsyncClient() as client:
        await client.post("http://notification-service:8000/notify", json={
            "to_email": payload.email,
            "subject": "Welcome to the Chat App!",
            "body": f"Hi {payload.email.split('@')[0]}, your account has been created."
        })
    return {"message": "User registered successfully", "user_id": str(user.id)}




@router.post("/login")
async def login_user(payload: LoginRequest):
    user = await User.find_one(User.email == payload.email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not pwd_context.verify(payload.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect password")

    async with httpx.AsyncClient() as client:
        await client.post("http://notification-service:8000/notify", json={
            "to_email": payload.email,
            "subject": "New Login Alert",
            "body": f"A new device just logged in to your account at {datetime.utcnow().isoformat()}."
        })

    token = create_jwt_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.models import User
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017")

async def init_db():
    client = AsyncIOMotorClient(MONGO_URI)
    db = client.auth_db
    await init_beanie(database=db, document_models=[User])




from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import init_db
from app.routes.user import router as user_router
from app.routes.profile import router as profile_router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await init_db()

app.include_router(user_router)
app.include_router(profile_router)

@app.get("/ping")
async def ping():
    return {"message": "user service is alive!"}

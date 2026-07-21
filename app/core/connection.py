from motor.motor_asyncio import AsyncIOMotorClient

from app.config import MONGODB_URL, DATABASE_NAME

#esablish database connection wioth fastapi

client = AsyncIOMotorClient(MONGODB_URL)
database = client[DATABASE_NAME]
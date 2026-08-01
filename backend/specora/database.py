from motor.motor_asyncio import AsyncIOMotorClient

from .config import MONGODB_URI, DATABASE_NAME

client = AsyncIOMotorClient("mongodb://localhost:27017")

db = client["specora"]
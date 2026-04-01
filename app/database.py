from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings


class Database:
    def __init__(self):
        self.client = AsyncIOMotorClient(settings.MONGO_URI)
        self.db = self.client[settings.DATABASE_NAME]

    def get_collection(self, name: str):
        return self.db[name]

# Singleton instance
database = Database()
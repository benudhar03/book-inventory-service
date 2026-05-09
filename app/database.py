from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase, AsyncIOMotorCollection
from app.config import settings
from app.core.logging import logger

class Database:
    client: AsyncIOMotorClient | None = None
    db: AsyncIOMotorDatabase | None = None

    async def connect(self) -> None:
        logger.info("Connecting to MongoDB...")
        self.client = AsyncIOMotorClient(settings.MONGO_URI)
        self.db = self.client[settings.DATABASE_NAME]
        # Verify connection
        await self.client.admin.command("ping")
        logger.info(f"Connected to MongoDB: {settings.DATABASE_NAME}")

    async def disconnect(self) -> None:
        if self.client:
            self.client.close()
            logger.info("Disconnected from MongoDB")

    def get_collection(self, name: str) -> AsyncIOMotorCollection:
        if self.db is None:
            raise RuntimeError("Database not initialized. Call connect() first.")
        return self.db[name]

database = Database()
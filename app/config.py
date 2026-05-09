from dotenv import load_dotenv
import os

load_dotenv()

class Settings:

    APP_NAME: str = "Book Inventory Service"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    API_V1_PREFIX: str = "/api/v1"

    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    DATABASE_NAME = os.getenv("DATABASE_NAME", "books_py_db")

    # Add collection names here
    BOOK_COLLECTION: str = "books"

    
settings = Settings()
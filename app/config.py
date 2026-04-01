from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    DATABASE_NAME = os.getenv("DATABASE_NAME", "books_py_db")

    # Add collection names here
    BOOK_COLLECTION: str = "books"

    
settings = Settings()
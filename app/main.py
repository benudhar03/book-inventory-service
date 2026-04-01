from fastapi import FastAPI, HTTPException
from app.database import database
from app.schemas import BookCreate
from app.services import BookService
from app.config import settings

app = FastAPI()


# Initialize the BookService with the book collection
book_service = BookService(database.get_collection(settings.BOOK_COLLECTION))

@app.get("/books/search", tags=["Books"])
async def search_books(title: str):
    result = await book_service.search_books_by_title(title)
    return result

@app.post("/books/", tags=["Books"])
async def create_book(book: BookCreate):
    return await book_service.create_book(book.model_dump())

@app.get("/books/", tags=["Books"])
async def get_all_books():
    return await book_service.get_all_books()

@app.get("/books/author/{author}", tags=["Books"])
async def get_books_by_author(author: str):
    books = await book_service.get_books_by_author(author)
    if not books:
        raise HTTPException(status_code=404, detail="No books found for this Author")
    return books

@app.patch("/books/{book_id}/toggle-stock", tags=["Books"])
async def toggle_book_stock(book_id: str):
    updated_book = await book_service.toggle_book_stock(book_id)
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return {
        "message": "Book stock status toggled successfully",
        "book": updated_book
    }
from app.models import book_helper
from app.constants import ID
import uuid

class BookService:

    def __init__(self, book_collection):
        self.book_collection = book_collection


    #Private method (reusable)
    async def _get_book_by_id(self, book_id: str):
        return await self.book_collection.find_one({ID: book_id})
    
    # Create a new book
    async def create_book(self, data: dict):
        # Generate UUID as string
        data[ID] = str(uuid.uuid4())

        result = await self.book_collection.insert_one(data)
        new_book = await self._get_book_by_id(result.inserted_id)
        return book_helper(new_book)


    # Fetch all books
    async def get_all_books(self):
        books = []
        query = {
            "in_stock": True,
            "quantity": { "$gt": 0 }
        }
        async for book in self.book_collection.find(query):
            books.append(book_helper(book))
        return books
    

    # Fetch books by author
    async def get_books_by_author(self, author: str):
        books = []
        query = {
            "author": author,
            "in_stock": True
        }
        async for book in self.book_collection.find(query):
            books.append(book_helper(book))
        return books
    
    # Search books by title
    async def search_books_by_title(self, title: str):
        books = []
        # Step 1: Try exact / partial match
        query = {
            "title": {
                "$regex": title,
                "$options": "i"
            }
        }
        async for book in self.book_collection.find(query):
            books.append(book_helper(book))

        # Step 2: If found → return
        if books:
            return {
                "found": True,
                "results": books
            }    
        
        # Step 3: If NOT found → fallback
        fallback_books = await self.get_fallback_books()
        return {
            "found": False,
            "message": "No books found for given title. Showing available books.",
            "results": fallback_books
        }
    
    async def get_fallback_books(self, limit: int = 5):
        fallback_books = []
        async for book in self.book_collection.find({"in_stock": True}).limit(limit):
            fallback_books.append(book_helper(book))
        return fallback_books
    
    # Toggle book stock status
    async def toggle_book_stock(self, book_id: str):
        book = await self._get_book_by_id(book_id)
        if not book:
            return None
        
        new_stock_status = not book.get("in_stock", True)
        await self.book_collection.update_one(
            {ID: book_id},
            {"$set": {"in_stock": new_stock_status}}
        )
        updated_book = await self._get_book_by_id(book_id)
        return book_helper(updated_book)
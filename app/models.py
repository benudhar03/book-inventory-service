def book_helper(book) -> dict:
    return {
        "id": str(book.get("_id")),
        "title": book.get("title"),
        "description": book.get("description"),
        "author": book.get("author"),
        "year": book.get("year"),
        "price": book.get("price"),
        "genre": book.get("genre"),
        "publisher": book.get("publisher"),
        "published_date": book.get("published_date"),
        "in_stock": book.get("in_stock"),
        "quantity": book.get("quantity"),
        "created_at": book.get("created_at"),
    }
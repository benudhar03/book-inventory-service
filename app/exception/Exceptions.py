class BookInventoryException(Exception):
    """Base exception for Book Inventory Service."""
    pass


class BookNotFoundException(BookInventoryException):
    def __init__(self, identifier: str):
        self.identifier = identifier
        super().__init__(f"Book not found: {identifier}")


class BookAlreadyExistsException(BookInventoryException):
    def __init__(self, title: str):
        self.title = title
        super().__init__(f"Book already exists with title: {title}")


class DatabaseException(BookInventoryException):
    def __init__(self, message: str):
        super().__init__(f"Database error: {message}")


class InvalidBookDataException(BookInventoryException):
    def __init__(self, message: str):
        super().__init__(f"Invalid book data: {message}")
import pytest
from httpx import AsyncClient, ASGITransport
from fastapi import status
import pytest_asyncio
from app.main import app

# Mock data
mock_book = {
    "id": "123",
    "title": "Clean Code",
    "author": "Robert C. Martin",
    "price": 500,
    "in_stock": True
}


# -------------------------------
# Fixture for AsyncClient
# -------------------------------
@pytest_asyncio.fixture
async def async_client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client


# -------------------------------
# TEST: Get All Books
# -------------------------------
@pytest.mark.asyncio
async def test_get_all_books(async_client, mocker):
    mocker.patch(
        "app.services.BookService.get_all_books",
        return_value=[mock_book]
    )

    response = await async_client.get("/books/")

    assert response.status_code == status.HTTP_200_OK
    assert response.json()[0]["title"] == "Clean Code"


# -------------------------------
# TEST: Create Book
# -------------------------------
@pytest.mark.asyncio
async def test_create_book(async_client, mocker):
    payload = {
        "title": "Test Book",
        "description": "This is a valid description",
        "author": "Test Author",
        "year": 2020,
        "price": 100.0,
        "quantity": 1
    }
    mocker.patch(
        "app.services.BookService.create_book",
        return_value=mock_book
    )
    response = await async_client.post("/books/", json=payload)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["title"] == "Clean Code"


# -------------------------------
# TEST: Search Books
# -------------------------------
@pytest.mark.asyncio
async def test_search_books(async_client, mocker):
    mocker.patch(
        "app.services.BookService.search_books_by_title",
        return_value={"found": True, "results": [mock_book]}
    )
    response = await async_client.get("/books/search?title=Clean")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["found"] is True


# -------------------------------
# TEST: Toggle Stock
# -------------------------------
@pytest.mark.asyncio
async def test_toggle_stock(async_client, mocker):
    updated_book = {**mock_book, "in_stock": False}

    mocker.patch(
        "app.services.BookService.toggle_book_stock",
        return_value=updated_book
    )
    response = await async_client.patch("/books/123/toggle-stock")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["book"]["in_stock"] is False
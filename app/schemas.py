from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import datetime, timezone


class BookCreate(BaseModel):
    title: str = Field(..., min_length=2, max_length=100)
    description: str = Field(..., min_length=10, max_length=1000)
    author: str = Field(..., min_length=2, max_length=100)
    year: int = Field(..., ge=1900, le=2100)
    price: float = Field(..., ge=0)

    genre: Optional[str] = None
    publisher: Optional[str] = None
    published_date: Optional[datetime] = None
    
    in_stock: Optional[bool] = True
    quantity: Optional[int] = Field(default=1, ge=0)

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    #🔥 Custom Validators
    @field_validator("title")
    @classmethod
    def title_must_not_be_blank(cls, v):
        if not v.strip():
            raise ValueError("Title cannot be empty or blank")
        return v

    @field_validator("author")
    @classmethod
    def author_must_not_be_blank(cls, v):
        if not v.strip():
            raise ValueError("Author cannot be empty")
        return v

    @field_validator("price")
    @classmethod
    def price_must_be_reasonable(cls, v):
        if v > 100000:
            raise ValueError("Price seems unrealistic")
        return v
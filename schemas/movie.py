from pydantic import BaseModel, Field
from typing import Optional, List


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=1,  max_length=30)
    director: str = Field(min_length=1,  max_length=30)
    year: int = Field( ge=1000, le=2023)
    overview: str = Field(min_length=1,  max_length=1000)
    rating: float = Field(default=0.0, ge=0.0, le=10.0)
    genre: str = Field(min_length=1,  max_length=30)
    class Config:
        schema_extra = {
            "example": {
                "id": 0,
                "title": "a movie",
                "director": "a director",
                "year": 2000,
                "overview": "a overview",
                "rating": 0.0,
                "genre": "a genre"

                
            }
        }
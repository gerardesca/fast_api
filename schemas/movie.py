from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=30)
    overview: str = Field(min_length=5, max_length=50)
    year: int = Field(le=2023)
    rating: float = Field(ge=0, le=10)
    category: str = Field(min_length=5, max_length=20)

    class Config:
        schema_extra = {
            "example": {
                "title": "Mi pelicula",
                "overview": "Descripcion de la pelicula",
                "year": 2020,
                "rating": 9.5,
                "category": "Drama"
            }
        }
from pydantic import BaseModel

class Movie(BaseModel):
    name: str
    id: int
    cost: int
    director: str

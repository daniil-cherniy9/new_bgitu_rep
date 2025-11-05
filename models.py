from pydantic import BaseModel
from typing import Optional

class Movie(BaseModel):
    name: str
    id: int
    cost: int
    director: str
    rating: Optional[int] = None

class User(BaseModel):
    login: str
    password: str

class LoginRequest:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

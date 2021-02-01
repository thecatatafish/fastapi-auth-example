from typing import Optional, List

from pydantic import constr
from pydantic.main import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class PublicExample(BaseModel):
    current_time: str


class Movie(BaseModel):
    title: constr(
        min_length=1,
    )
    rating: int

    class Config:
        orm_mode = True
        schema_extra = {"example": {"title": "Good Will Hunting", "rating": 4}}


class UserBase(BaseModel):
    username: str


class User(UserBase):
    id: int
    is_active: Optional[bool] = None
    movies: List[Movie] = []

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    hashed_password: str

from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import crud
from ..database import get_db
from ..schemas import Movie, User
from ..utilities import get_current_active_user

router = APIRouter()


@router.post("/users/movie", response_model=Movie)
async def add_movie(
    movie: Movie,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    crud.add_movie(db, movie, current_user.id)
    return movie


@router.get("/users/movie", response_model=List[Movie])
def get_all_movies(
    current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)
):
    return crud.get_all_movies(db, current_user.id)

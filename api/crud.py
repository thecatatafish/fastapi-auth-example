from sqlalchemy.orm import Session

from . import models, schemas


def get_user_by_username(db: Session, username: str):
    """
    Get the user from the database if username exists
    If the user is not found the function returns None
    """
    return db.query(models.User).filter(models.User.username == username).first()


def create_user(db: Session, user: schemas.UserCreate):
    """
    Create a user in the database
    """
    hashed_password = user.hashed_password
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def add_movie(db: Session, movie: schemas.Movie, owner_id: int):
    """
    Add a movie in the database, where each move has an owner from
    the Users table.
    """
    db_movie = models.Movie(**movie.dict(), owner_id=owner_id)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie


def get_all_movies(db: Session, owner_id: int):
    """
    Get a list of all the moves owned by the requested owner
    """
    query = db.query(models.Movie).filter(models.Movie.owner_id == owner_id)
    return query.all()

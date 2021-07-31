from . import crud
from .database import get_db
from .schemas import UserCreate
from .utilities import get_password_hash


def populate_database():
    """
    Creates first users in the database for convenience
    """
    db = next(get_db())
    raw_password = "secret"
    for username in ["test1@test.com", "test2@test.com"]:
        user = UserCreate(
            username=username, hashed_password=get_password_hash(raw_password)
        )
        if not crud.get_user_by_username(db, user.username):
            print(f"Creating user: {user.username}")
            crud.create_user(db, user=user)

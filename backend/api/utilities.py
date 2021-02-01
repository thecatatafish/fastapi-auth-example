from datetime import timedelta, datetime

from fastapi import HTTPException, status, Depends
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from . import crud
from .database import get_db
from .schemas import TokenData, User
from .settings import settings


def get_credentials_exception():
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )


def verify_password(plain_password, hashed_password):
    return settings.pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return settings.pwd_context.hash(password)


def authenticate_user(db: Session, username: str, password: str):
    """
    Here we check if the user exists in the database and if the
    provided password matches the password in the database
    """
    user = crud.get_user_by_username(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=15)):
    """
    Create a token to send to an authenticated user that expires after a certain time (default of 15 minutes)
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


async def get_current_user(
    token: str = Depends(settings.oauth2_scheme), db: Session = Depends(get_db)
):
    """
    This is the function that checks if the user has a valid token
    """
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        username: str = payload.get("sub")
        if username is None:
            raise get_credentials_exception()
        token_data = TokenData(username=username)
    except JWTError:
        raise get_credentials_exception()
    user = crud.get_user_by_username(db, token_data.username)
    if user is None:
        raise get_credentials_exception()
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

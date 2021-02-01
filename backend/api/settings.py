from dataclasses import dataclass

from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext


@dataclass
class Settings:
    SECRET_KEY = ""
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


settings = Settings()

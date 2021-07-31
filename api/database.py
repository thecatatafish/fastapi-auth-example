from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def create_db_engine():
    SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"

    # This is an option only needed for SQLite (see FastAPI docs)
    connect_args = (
        {"check_same_thread": False}
        if SQLALCHEMY_DATABASE_URL.startswith("sqlite")
        else {}
    )

    return create_engine(SQLALCHEMY_DATABASE_URL, connect_args=connect_args)


engine = create_db_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .populate_database import populate_database
from .routers import users, auth, movies, public

models.Base.metadata.create_all(bind=engine)
populate_database()

app = FastAPI()
origins = ["http://0.0.0.0:8080"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.router, tags=["Authentication"])
app.include_router(users.router, tags=["Users"])
app.include_router(movies.router, tags=["Movies"])
app.include_router(public.router, tags=["Public"])

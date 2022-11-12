from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine
from .routes import users

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)

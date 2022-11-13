from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine
from .routes import users
from .routes import login
from .routes import loans
from .routes import guarantors
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(login.router)
app.include_router(loans.router)
app.include_router(guarantors.router)
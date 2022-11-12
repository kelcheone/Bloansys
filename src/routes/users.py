from fastapi import APIRouter, Depends, HTTPException
from src import database, models, schemas, crud
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("/")
def create_user(request: schemas.Customer, db: Session = Depends(database.get_db)):
    return crud.create_user(request, db)


@router.get("/")
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users

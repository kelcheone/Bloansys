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
def get_users(db: Session = Depends(database.get_db)):
    return crud.get_users(db)

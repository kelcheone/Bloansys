from fastapi import APIRouter, Depends, HTTPException
from src import database, models, schemas
from src.crud import UserCrud
from sqlalchemy.orm import Session
from typing import List


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("/")
def create_user(request: schemas.Customer, db: Session = Depends(database.get_db)):
    return UserCrud.create_user(request, db)


@router.get("/", response_model=List[schemas.ShowCustomer])
def get_users(db: Session = Depends(database.get_db)):
    return UserCrud.get_users(db)


@router.get("/{id}", response_model=schemas.ShowCustomer)
def get_user(id: int, db: Session = Depends(database.get_db)):
    return UserCrud.get_user(db, id)


@router.delete("/{id}")
def delete_user(id: int, db: Session = Depends(database.get_db)):
    return UserCrud.delete_user(db, id)


@router.put("/{id}")
def update_user(id: int, request: schemas.Customer, db: Session = Depends(database.get_db)):
    return UserCrud.update_user(id, request, db)
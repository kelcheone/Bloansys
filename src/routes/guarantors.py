from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.crud import GuarantorsCrud
from .. import database, schemas


router = APIRouter(
    prefix="/guarantors",
    tags=["Guarantors"],
)


@router.get("/")
def get_guarantors(db: Session = Depends(database.get_db)):
    return GuarantorsCrud.get_guarantors(db)


@router.post("/")
def create_guarantor(request: schemas.CreateGuarantor, db: Session = Depends(database.get_db)):
    return GuarantorsCrud.create_guarantor(db, request)


@router.get("/{id}")
def get_guarantor(id: int, db: Session = Depends(database.get_db)):
    return GuarantorsCrud.get_guarantor(db, id)


@router.delete("/{id}")
def delete_guarantor(id: int, db: Session = Depends(database.get_db)):
    return GuarantorsCrud.delete_guarantor(db, id)


@router.put("/{id}")
def update_guarantor(id: int, request: schemas.CreateGuarantor, db: Session = Depends(database.get_db)):
    return GuarantorsCrud.update_guarantor(db, id, request)
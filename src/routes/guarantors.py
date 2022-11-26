from fastapi import APIRouter, Depends, HTTPException, status, Body
from sqlalchemy.orm import Session
from src.crud import GuarantorsCrud, LoansCrud
from .. import database, schemas, Oauth2


router = APIRouter(
    prefix="/guarantors",
    tags=["Guarantors"],
)


@router.get("/")
def get_guarantors(db: Session = Depends(database.get_db), current_user: int = Depends(Oauth2.get_current_user)):
    print(current_user.user_id)
    return GuarantorsCrud.get_guarantors(db)


@router.get("/no")
def get_guarantors(db: Session = Depends(database.get_db), current_user: int = Depends(Oauth2.get_current_user)):
    print(current_user.user_id)
    return LoansCrud.get_user_loans_without_guarantee(db, current_user)


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

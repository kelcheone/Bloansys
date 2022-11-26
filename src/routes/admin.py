from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from src.crud import AdminCrud
from .. import models, schemas, database, Oauth2


router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.get("/active-users-count")
def active_users(db: Session = Depends(database.get_db)):
    return AdminCrud.get_active_users(db)


@router.get("/defaulted-users-count")
def defaulted_users(db: Session = Depends(database.get_db)):
    return AdminCrud.get_defaulted_loans(db)


@router.get("/all-loans-count")
def all_loans(db: Session = Depends(database.get_db)):
    return AdminCrud.all_loans(db)


@router.get("/pending-count")
def pending_loans(db: Session = Depends(database.get_db)):
    return AdminCrud.get_pending_loans(db)


@router.get("/unverified-count")
def unverified_users(db: Session = Depends(database.get_db)):
    return AdminCrud.get_unverified_users(db)


@router.get("/all-users-count")
def all_users(db: Session = Depends(database.get_db)):
    return AdminCrud.get_all_users_counts(db)


@router.get("/pending-loans")
def pending_loans(db: Session = Depends(database.get_db)):
    return AdminCrud.get_all_pending_loans(db)


@router.patch("/verify-user/{user_id}")
def verify_user(user_id: int, status: str, db: Session = Depends(database.get_db)):
    return AdminCrud.verify_user(user_id=user_id, status=status, db=db)


@router.patch("/approve-loan/{loan_id}")
def approve_loan(loan_id: int, status: str, db: Session = Depends(database.get_db)):
    return AdminCrud.approve_loan(loan_id, status, db)


@router.get("/all-users")
def all_users(db: Session = Depends(database.get_db)):
    return AdminCrud.get_all_users(db)

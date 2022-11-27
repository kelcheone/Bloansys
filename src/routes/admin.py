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
    return AdminCrud.get_unverified_users_counts(db)


@router.get("/all-users-count")
def all_users(db: Session = Depends(database.get_db)):
    return AdminCrud.get_all_users_counts(db)


@router.get("/pending-loans")
def pending_loans(db: Session = Depends(database.get_db)):
    return AdminCrud.get_all_pending_loans(db)


@router.get("/all-users")
def all_users(db: Session = Depends(database.get_db)):
    return AdminCrud.get_all_users(db)


@router.patch("/verify-user/{user_id}")
def verify_user(user_id: int,  db: Session = Depends(database.get_db)):
    return AdminCrud.verify_user(user_id=user_id,  db=db)


@router.patch("/reject-verification/{user_id}")
def reject_verification(user_id: int,  db: Session = Depends(database.get_db)):
    return AdminCrud.reject_verification(user_id=user_id, db=db)


@router.patch("/approve-loan/{loan_id}")
def approve_loan(loan_id: int,  db: Session = Depends(database.get_db)):
    return AdminCrud.approve_loan(loan_id=loan_id, db=db)


@router.patch("/reject-loan/{loan_id}")
def reject_loan(loan_id: int,  db: Session = Depends(database.get_db)):
    return AdminCrud.reject_loan(loan_id=loan_id, db=db)


@router.get("/all-unverified-users")
def all_unverified_users(db: Session = Depends(database.get_db)):
    return AdminCrud.get_all_unverified_users(db)


@router.patch("/verify-user/{user_id}")
def verify_user(user_id: int,  db: Session = Depends(database.get_db)):
    return AdminCrud.verify_user(user_id=user_id,  db=db)


@router.patch("/verify-all-users")
def verify_all_users(db: Session = Depends(database.get_db)):
    return AdminCrud.verify_all_users(db=db)


@router.patch("/reject-verification/{user_id}")
def reject_verification(user_id: int,  db: Session = Depends(database.get_db)):
    return AdminCrud.reject_verification(user_id=user_id, db=db)


@router.get("/all-user-details/{user_id}")
def all_user_details(user_id: int, db: Session = Depends(database.get_db)):
    return AdminCrud.get_user_details(user_id=user_id, db=db)


@router.put("/update-user-details/{user_id}")
def update_user_details(user_id: int, user: schemas.UserUpdate, db: Session = Depends(database.get_db)):
    return AdminCrud.update_user(user_id=user_id, user=user, db=db)

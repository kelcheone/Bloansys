from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from src.crud import AdminCrud
from .. import models, schemas, database, Oauth2


router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.get("/active-users-count")
def active_users(db: Session = Depends(database.get_db), current_user: int = Depends(Oauth2.get_current_user)):
    return AdminCrud.get_active_users(db, current_user)


@router.get("/defaulted-users-count")
def defaulted_users(db: Session = Depends(database.get_db), current_user: int = Depends(Oauth2.get_current_user)):
    return AdminCrud.get_defaulted_loans(db, current_user)


@router.get("/all-loans-count")
def all_loans(db: Session = Depends(database.get_db), current_user: int = Depends(Oauth2.get_current_user)):
    return AdminCrud.all_loans(db, current_user)


@router.get("/pending-count")
def pending_loans(db: Session = Depends(database.get_db), current_user: int = Depends(Oauth2.get_current_user)):
    return AdminCrud.get_pending_loans(db, current_user)


@router.get("/unverified-count")
def unverified_users(db: Session = Depends(database.get_db), current_user: int = Depends(Oauth2.get_current_user)):
    return AdminCrud.get_unverified_users_counts(db, current_user)


@router.get("/all-users-count")
def all_users(db: Session = Depends(database.get_db), current_user: int = Depends(Oauth2.get_current_user)):
    return AdminCrud.get_all_users_counts(db, current_user)


@router.get("/pending-loans")
def pending_loans(db: Session = Depends(database.get_db), current_user: int = Depends(Oauth2.get_current_user)):
    return AdminCrud.get_all_pending_loans(db, current_user)


@router.get("/all-users")
def all_users(db: Session = Depends(database.get_db), current_user: int = Depends(Oauth2.get_current_user)):
    return AdminCrud.get_all_users(db, current_user)


@router.patch("/verify-user/{user_id}")
def verify_user(user_id: int,  db: Session = Depends(database.get_db), current_user: int = Depends(Oauth2.get_current_user)):
    return AdminCrud.verify_user(user_id=user_id,  db=db, current_user=current_user)


@router.patch("/reject-verification/{user_id}")
def reject_verification(user_id: int,  db: Session = Depends(database.get_db), current_user: int = Depends(Oauth2.get_current_user)):
    return AdminCrud.reject_verification(user_id=user_id, db=db, current_user=current_user)


@router.patch("/approve-loan/{loan_id}")
def approve_loan(loan_id: int,  db: Session = Depends(database.get_db), current_user: int = Depends(Oauth2.get_current_user)):
    return AdminCrud.approve_loan(loan_id=loan_id, db=db, current_user=current_user)


@router.patch("/reject-loan/{loan_id}")
def reject_loan(loan_id: int,  db: Session = Depends(database.get_db), current_user: int = Depends(Oauth2.get_current_user)):
    return AdminCrud.reject_loan(loan_id=loan_id, db=db, current_user=current_user)


@router.get("/all-unverified-users")
def all_unverified_users(db: Session = Depends(database.get_db), current_user: int = Depends(Oauth2.get_current_user)):
    return AdminCrud.get_all_unverified_users(db, current_user)


@router.patch("/verify-user/{user_id}")
def verify_user(user_id: int,  db: Session = Depends(database.get_db), current_user: int = Depends(Oauth2.get_current_user)):
    return AdminCrud.verify_user(user_id=user_id,  db=db, current_user=current_user)


@router.patch("/verify-all-users")
def verify_all_users(db: Session = Depends(database.get_db), current_user: int = Depends(Oauth2.get_current_user)):
    return AdminCrud.verify_all_users(db=db, current_user=current_user)


@router.patch("/reject-verification/{user_id}")
def reject_verification(user_id: int,  db: Session = Depends(database.get_db), current_user: int = Depends(Oauth2.get_current_user)):
    return AdminCrud.reject_verification(user_id=user_id, db=db, current_user=current_user)


@router.get("/all-user-details/{user_id}")
def all_user_details(user_id: int, db: Session = Depends(database.get_db), current_user: int = Depends(Oauth2.get_current_user)):
    return AdminCrud.get_user_details(user_id=user_id, db=db, current_user=current_user)


@router.put("/update-user-details/{user_id}")
def update_user_details(user_id: int, user: schemas.UserUpdate, db: Session = Depends(database.get_db), current_user: int = Depends(Oauth2.get_current_user)):
    return AdminCrud.update_user(user_id=user_id, user=user, db=db, current_user=current_user)


@router.get("/loan-details/{loan_id}", response_model=schemas.ShowLoan)
def loan_details(loan_id: int, db: Session = Depends(database.get_db), current_user: int = Depends(Oauth2.get_current_user)):
    return AdminCrud.get_loan(loan_id=loan_id, db=db, current_user=current_user)


@router.get("/no-guarantor-loans")
def no_guarantor_loans(db: Session = Depends(database.get_db), current_user: int = Depends(Oauth2.get_current_user)):
    return AdminCrud.get_loans_without_guarantors(db=db, current_user=current_user)

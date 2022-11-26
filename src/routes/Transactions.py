from fastapi import APIRouter, Response, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import database, Oauth2
from src.crud import TransactionsCrud


router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)

# Get current user transactions using loan id


@router.get("/me")
def get_transactions(db: Session = Depends(database.get_db), current_user: int = Depends(Oauth2.get_current_user)):
    return TransactionsCrud.get_transactions(db, current_user)


@router.get("/paid")
def get_transaction_of_paid_loans(db: Session = Depends(database.get_db), current_user: int = Depends(Oauth2.get_current_user)):
    return TransactionsCrud.get_transaction_of_paid_loans(db, current_user)

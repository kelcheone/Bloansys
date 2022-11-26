from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas


# Get current user transactions using loan id


def get_transactions(db: Session, current_user: int):
    transactions = db.query(models.Transaction).filter(
        models.Transaction.user_id == current_user.user_id).all()
    return transactions


def get_transaction_of_paid_loans(db: Session, current_user: int):
    transactions = db.query(models.Transaction).filter(
        models.Transaction.user_id == current_user.user_id, models.Transaction.transaction_type == "Paid").all()
    if not transactions:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"You have no paid loans")
    return transactions

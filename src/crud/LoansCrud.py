from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from .. import models, schemas


def create_loan(request: schemas.CreateLoan, db: Session):
    new_loan = models.Loan(
        amount=request.amount,
        due_date=request.due_date,
        interest=request.interest,
        balance=request.amount,
        customer_id=request.customer_id,
    )
    db.add(new_loan)
    db.commit()
    db.refresh(new_loan)
    return new_loan


def get_loans(db: Session):
    loans = db.query(models.Loan).all()
    return loans


def get_loan(db: Session, loan_id: int):
    loan = db.query(models.Loan).filter(
        models.Loan.loan_id == loan_id).first()
    if not loan:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Loan with the id {loan_id} is not available")
    return loan


def delete_loan(db: Session, loan_id: int):
    loan = db.query(models.Loan).filter(
        models.Loan.loan_id == loan_id)
    if not loan.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Loan with the id {loan_id} is not available")
    loan.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update_loan(id: int, request: schemas.UpdateLoan, db: Session):
    loan = db.query(models.Loan).filter(
        models.Loan.loan_id == id)
    if not loan.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Loan with the id {id} is not available")
    request.balance = request.amount
    loan.update(request.dict(), synchronize_session=False)
    db.commit()
    return loan.first()


# get amount paid and return the balance


def pay_loan(id: int, request: schemas.PayLoan, db: Session):
    loan = db.query(models.Loan).filter(models.Loan.loan_id == id)
    if not loan.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Loan with the id {id} is not available")
    loan.update({'balance': models.Loan.balance - request.amount},
                synchronize_session=False)
    db.commit()
    return loan.first()

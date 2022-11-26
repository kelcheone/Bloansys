from datetime import datetime
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from .. import models, schemas
from decimal import Decimal


def create_loan(request: schemas.CreateLoan, db: Session, current_user: int):
    new_loan = models.Loan(
        amount=request.amount,
        paid=0.0,
        interest=request.interest,
        due_date=request.due_date,
        user_id=current_user.user_id,
        created_at=datetime.now()
    )
    db.add(new_loan)
    db.commit()
    db.refresh(new_loan)

    # Create a transaction for the loan
    new_transaction = models.Transaction(
        user_id=current_user.user_id,
        amount=request.amount,
        transaction_type="Pending",
        loan_id=new_loan.loan_id,
        transaction_date=datetime.now()
    )
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)

    return new_transaction


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


def delete_loan(db: Session, loan_id: int, current_user: int):
    # make sure the loan belongs to the current user
    loan = db.query(models.Loan).filter(
        models.Loan.loan_id == loan_id, models.Loan.user_id == current_user.user_id)
    if not loan.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Loan with the id {loan_id} is not available")
    loan.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update_loan(id: int, request: schemas.UpdateLoan, db: Session, current_user: int):
    # make sure the loan belongs to the current user
    loan = db.query(models.Loan).filter(
        models.Loan.loan_id == id, models.Loan.user_id == current_user.user_id)
    if not loan.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Loan with the id {id} is not available")
    request.balance = request.amount
    # Update the loan with user_id being the current user
    loan.update(request.dict(), synchronize_session=False)
    db.commit()
    return loan.first()


def get_user_loans(db: Session, current_user: int):
    loans = db.query(models.Loan).filter(
        models.Loan.user_id == current_user.user_id).all()
    return loans


# get user loans without a guarantor
def get_user_loans_without_guarantee(db: Session, current_user: int):

    # Loans where the guarantors is an empty list
    loans = db.query(models.Loan).filter(
        models.Loan.user_id == current_user.user_id, models.Loan.guarantors == None).all()
    return loans


def get_my_loans(db: Session, current_user: int):
    loans = db.query(models.Loan).filter(
        models.Loan.user_id == current_user.user_id).all()
    if not loans:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"You have no loans")
    return loans


def user_loan_details(db: Session, current_user: int):
    loans = db.query(models.Loan).filter(
        models.Loan.user_id == current_user.user_id).all()

    # make due date of type string to datetime type
    for loan in loans:
        loan.due_date = datetime.strptime(loan.due_date, '%Y-%m-%d')
    diff = []
    for loan in loans:
        diff.append((loan.due_date - loan.created_at).days)

    data = schemas.UserLoanDetails(
        loans=len(loans),

        time=str(
            # in months
            round(sum(diff)/30, 2)

        ),
        apr=sum([loan.interest for loan in loans]),
        Balance=sum([loan.amount - Decimal(loan.paid) for loan in loans])
    )

    return data


def pay_loan(request: schemas.PayLoan, db: Session):
    loan = db.query(models.Loan).filter(
        models.Loan.loan_id == request.loan_id)
    if not loan.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Loan with the id {id} is not available")
# only update the paaid field
# update by adding the amount paid to the existing paid amount of the loan
    loan.update({"paid": loan.first().paid + request.amount},
                synchronize_session=False)
    #
    # loan.update({"paid": request.amount}, synchronize_session=False)

    db.commit()
    # generate transaction
    new_transaction = models.Transaction(
        user_id=loan.first().user_id,
        amount=request.amount,
        transaction_type="Paid",
        loan_id=loan.first().loan_id,
        transaction_date=datetime.now()
    )
    db.add(new_transaction)
    db.commit()
    return new_transaction

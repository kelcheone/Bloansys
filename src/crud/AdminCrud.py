from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from datetime import datetime

from .. import models, schemas


def get_active_users(db: Session):
    # Get all the loans where the due date is greater than the current date
    loans = db.query(models.Loan).all()
    if not loans:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"There are no loans")
    active_loans = []
    for loan in loans:
        # make due_date a datetime object
        due_date = datetime.strptime(loan.due_date, '%Y-%m-%d')
        if due_date > datetime.now():
            active_loans.append(loan)
    total_amount = 0
    for loan in active_loans:
        total_amount += loan.amount

    return {"accounts": len(active_loans), "total_amount": total_amount}


def get_defaulted_loans(db: Session):
    # Get all the loans where the due date is less than the current date
    loans = db.query(models.Loan).all()
    if not loans:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"There are no loans")

    defaulted_loans = []
    for loan in loans:
        # make due_date a datetime object
        due_date = datetime.strptime(loan.due_date, '%Y-%m-%d')
        if due_date < datetime.now():
            defaulted_loans.append(loan)

    # get the length and the total amount of the defaulted loans
    total_amount = 0
    for loan in defaulted_loans:
        total_amount += loan.amount

    return {"accounts": len(defaulted_loans), "total_amount": total_amount}


def all_loans(db: Session):
    loans = db.query(models.Loan).all()
    if not loans:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"There are no loans")

    total_amount = 0
    for loan in loans:
        total_amount += loan.amount

    return {"accounts": len(loans), "total_amount": total_amount}


# All pending loans
def get_pending_loans(db: Session):
    loans = db.query(models.Loan).filter(
        models.Loan.status == "pending").all()
    if not loans:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"There are no pending loans")

    total_amount = 0
    for loan in loans:
        total_amount += loan.amount

    return {"accounts": len(loans), "total_amount": total_amount}

# all unverified users


def get_unverified_users(db: Session):
    users = db.query(models.User).filter(
        models.User.status == "unverified").all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"There are no unverified users")

    return {"accounts": len(users)}

# all users


def get_all_users_counts(db: Session):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"There are no users")

    return {"accounts": len(users)}


# All loan pending Appliations
def get_all_pending_loans(db: Session):
    loans = db.query(models.Loan).filter(
        models.Loan.status == "pending").all()
    if not loans:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"There are no pending loans")
    # from user_id get usernames
    names = []
    for loan in loans:
        user = db.query(models.User).filter(
            models.User.user_id == loan.user_id).first()
        names.append(user.first_name + " " + user.last_name)

    # put all into PendingLoan schema
    pending_loans = []
    for i in range(len(loans)):
        pending_loans.append(schemas.PendingLoans(
            loan_id=loans[i].loan_id,
            user_name=names[i],
            amount=loans[i].amount,
            due_date=loans[i].due_date,
            interest=loans[i].interest,
            guarantors=len(loans[i].guarantors),
        ))

    return pending_loans

# Approve or reject the loan application


def approve_loan(db: Session, loan_id: int, status: str):
    loan = db.query(models.Loan).filter(
        models.Loan.loan_id == loan_id).first()
    if not loan:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"There is no loan with the id {loan_id}")
    loan.status = status
    db.commit()
    return {"message": "Loan status updated"}


def verify_user(db: Session, user_id: int, status: str):
    user = db.query(models.User).filter(
        models.User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"There is no user with the id {user_id}")
    user.status = status
    db.commit()
    return {"message": "User status updated"}


# all users
def get_all_users(db: Session):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"There are no users")

    # return users in AdminCustomerDetails schema
    total_borrowed = []
    total_paid = []
    for user in users:
        loans = db.query(models.Loan).filter(
            models.Loan.user_id == user.user_id).all()
        total_borrowed.append(sum([loan.amount for loan in loans]))
        total_paid.append(sum([loan.paid for loan in loans]))

    # get

    admin_users = []
    for i in range(len(users)):
        admin_users.append(schemas.AdminCustomerDetails(
            user_id=users[i].user_id,
            name=users[i].first_name + " " + users[i].last_name,
            Borrowed=total_borrowed[i],
            paid=total_paid[i],
            status=users[i].status,
            loans=len(loans)
        ))

    return admin_users

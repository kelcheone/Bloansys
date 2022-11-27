from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from src.crud import LoansCrud
from .. import models, schemas, database, Oauth2


router = APIRouter(
    prefix="/loans",
    tags=["Loans"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_loan(request: schemas.CreateLoan, db: Session = Depends(database.get_db), current_user: int = Depends(Oauth2.get_current_user)):
    return LoansCrud.create_loan(request, db, current_user)


@router.get("/my-loans", status_code=status.HTTP_200_OK)
def get_loans(db: Session = Depends(database.get_db), current_user: int = Depends(Oauth2.get_current_user)):
    return LoansCrud.get_user_loans(db, current_user)


@router.get("/details", status_code=status.HTTP_200_OK)
def get_loans(db: Session = Depends(database.get_db), current_user: int = Depends(Oauth2.get_current_user)):
    return LoansCrud.user_loan_details(db, current_user)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowLoan)
def get_loan(id: int, db: Session = Depends(database.get_db)):
    return LoansCrud.get_loan(db, id)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_loan(id: int, db: Session = Depends(database.get_db), current_user: int = Depends(Oauth2.get_current_user)):
    return LoansCrud.delete_loan(db, id, current_user)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_loan(id: int, request: schemas.UpdateLoan, db: Session = Depends(database.get_db), current_user: int = Depends(Oauth2.get_current_user)):
    return LoansCrud.update_loan(id, request, db, current_user)


# get user loans
@router.get("/user/{id}", status_code=status.HTTP_200_OK, response_model=list[schemas.ShowLoan])
def get_user_loans(current_user: int = Depends(Oauth2.get_current_user), db: Session = Depends(database.get_db)):
    return LoansCrud.get_user_loans(db, current_user)


@router.get("/my-loans", status_code=status.HTTP_200_OK, response_model=list[schemas.ShowLoan])
def my_loans(current_user: int = Depends(Oauth2.get_current_user), db: Session = Depends(database.get_db)):
    return LoansCrud.get_my_loans(db, current_user)


@router.patch("/pay", status_code=status.HTTP_202_ACCEPTED)
def pay_loan(request: schemas.PayLoan, db: Session = Depends(database.get_db)):
    return LoansCrud.pay_loan(request, db)

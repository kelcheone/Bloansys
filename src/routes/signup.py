# Sign up page
from fastapi import APIRouter, Response, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.schemas import Customer, ShowCustomer

from .. import models, utils
from ..database import get_db

router = APIRouter(tags=["Registration"])


@router.post('/signup')
def signup(customer: Customer, db: Session = Depends(get_db)):
    # Check if the user already exists
    user = db.query(models.User).filter(
        models.User.email == customer.email).first()
    if user:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="User already exists")
    # Hash the password
    hashed_password = utils.get_password_hash(customer.password)
    # Create a new user
    new_user = models.User(
        first_name=customer.first_name,
        last_name=customer.last_name,
        national_id=customer.national_id,
        phone_number=customer.phone_number,
        email=customer.email,
        password=hashed_password
    )
    # Save the new user
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return Response(status_code=status.HTTP_201_CREATED)

from fastapi import APIRouter, Response, Depends, HTTPException, status, Body, Request
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from src.schemas import Customer, ShowCustomer

from src.schemas import Token, SignInRequest, TokenJson
from .. import models, utils, Oauth2

from ..database import get_db

router = APIRouter(tags=["Authentication"])


@router.post('/signup')
def signup(customer: Customer, db: Session = Depends(get_db)):
    # Check if the user already exists
    user = db.query(models.User).filter(
        models.User.email == customer.email).first()
    if user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User already exists")
    # Hash the password
    hashed_password = utils.hash_password(customer.password)
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


@router.post("/signin", response_model=TokenJson)
def login_for_access_token(
    signin_request: SignInRequest, db: Session = Depends(get_db)
):
    user = db.query(models.User).filter(
        models.User.email == signin_request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not utils.verify_password(signin_request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = Oauth2.create_access_token(
        data={"user_id": user.user_id, "user_email": user.email}
    )
    return {"token": access_token, "token_type": "bearer"}


"""
@router.post('/login')
def login_for_access_token(
    signin_request: SignInRequest, db: Session = Depends(get_db)):

    print({"user_credentials": signin_request})

    user = db.query(models.User).filter(
        models.User.email == signin_request.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")

    if not utils.verify_password(signin_request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    # Create access token by getting the user id and passing it to the create_access_token function
    access_token = Oauth2.create_access_token(
        data={"user_id": user.user_id, "user_email": user.email})

    # access_token = Oauth2.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

"""

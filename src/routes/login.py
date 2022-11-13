from fastapi import APIRouter, Response, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.schemas import Token
from .. import models, utils, Oauth2

from ..database import get_db

router = APIRouter(tags=["Authentication"])


@router.post('/login')
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    user = db.query(models.Customer).filter(
        models.Customer.email == user_credentials.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")

    if not utils.verify_password(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    # Create access token by getting the user id and passing it to the create_access_token function
    access_token = Oauth2.create_access_token(
        data={"customer_id": user.customer_id})

    # access_token = Oauth2.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

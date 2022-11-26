from fastapi import APIRouter, Response, Depends, HTTPException, status, Body, Request
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.schemas import SignInRequest, TokenJson
from .. import models, utils, Oauth2

from ..database import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


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

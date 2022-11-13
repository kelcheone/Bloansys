from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from src.config import configs
from src.database import get_db
from sqlalchemy.orm import Session
from . import models

from src.schemas import TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = f"{configs.secret_key}"
ALGORITHM = f"{configs.algorithm}"
ACCESS_TOKEN_EXPIRE_MINUTES = configs.expiry_time


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    endoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return endoded_jwt


def verify_token_access(token: str, credentials_exception):
    try:

        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)

        id: str = payload.get("customer_id")
        if id == None:
            raise credentials_exception
        token_data = TokenData(id=id)
    except JWTError:
        raise credentials_exception
    return token_data


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})

    gtoken = verify_token_access(token, credentials_exception)

    user = db.query(models.Customer).filter(
        gtoken.id == models.Customer.customer_id).first()
    return user

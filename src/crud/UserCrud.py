from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status

from .. import models, schemas
from src.utils import hash_password


def get_user(db: Session, user_id: int):
    user = db.query(models.User).filter(
        models.User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {user_id} is not available")
    return user


def create_user(request: schemas.Customer, db: Session):
    new_user = models.User(
        first_name=request.first_name,
        last_name=request.last_name,
        password=hash_password(request.password),
        national_id=request.national_id,
        phone_number=request.phone_number,
        email=request.email,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_users(db: Session):
    users = db.query(models.User).all()
    return users


def delete_user(db: Session, user_id: int):
    user = db.query(models.User).filter(
        models.User.user_id == user_id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {user_id} is not available")
    user.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update_user(id: int, request: schemas.UpdateCustomer, db: Session):
    customer = db.query(models.User).filter(
        models.User.user_id == id)
    if not customer.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")

    customer.update(request.dict(), synchronize_session=False)
    db.commit()
    return customer.first()

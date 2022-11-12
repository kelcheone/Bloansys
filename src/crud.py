from sqlalchemy.orm import Session

from . import models, schemas
from src.utils import hash_password


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_user(request: schemas.Customer, db: Session):
    new_user = models.Customer(
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
    users = db.query(models.Customer).all()
    return users

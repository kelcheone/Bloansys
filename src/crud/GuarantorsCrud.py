from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas


def create_guarantor(db: Session, guarantor: schemas.CreateGuarantor):
    db_guarantor = models.Guarantor(**guarantor.dict())
    db.add(db_guarantor)
    db.commit()
    db.refresh(db_guarantor)
    return db_guarantor


def get_guarantors(db: Session):
    guarantors = db.query(models.Guarantor).all()
    return guarantors


def get_guarantor(db: Session, id: int):
    guarantor = db.query(models.Guarantor).filter(
        models.Guarantor.guarantor_id == id).first()
    if not guarantor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Guarantor with the id {id} is not available")
    return guarantor


def delete_guarantor(db: Session, id: int):
    guarantor = db.query(models.Guarantor).filter(
        models.Guarantor.guarantor_id == id)
    if not guarantor.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Guarantor with the id {id} is not available")
    guarantor.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update_guarantor(db: Session, id: int, guarantor: schemas.CreateGuarantor):
    db_guarantor = db.query(models.Guarantor).filter(
        models.Guarantor.guarantor_id == id)
    if not db_guarantor.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Guarantor with the id {id} is not available")
    db_guarantor.update(guarantor.dict())
    db.commit()
    return 'updated successfully'

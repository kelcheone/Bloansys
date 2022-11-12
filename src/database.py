from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import configs


SQL_ALCHEMY_URL = f"postgresql://{configs.db_username}:{configs.db_password}@{configs.db_hostname}:{configs.db_port}/{configs.db_name}"

engine = create_engine(SQL_ALCHEMY_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

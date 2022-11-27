from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    password = Column(String(200))
    email = Column(String(150), unique=True)
    national_id = Column(String(20))
    status = Column(String, default="unverified")
    role = Column(String, default="user")

    file_path = Column(String(100))
    phone_number = Column(String(20))
    loans = relationship("Loan", back_populates="customer",
                         cascade="all, delete")


class Loan(Base):
    __tablename__ = "loans"

    loan_id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer)
    due_date = Column(String(50))
    interest = Column(Integer)
    paid = Column(Integer)
    status = Column(String, default="pending")
    created_at = Column(String(50))
    user_id = Column(Integer, ForeignKey(
        "users.user_id", ondelete="CASCADE"))
    customer = relationship(
        "User", back_populates="loans", cascade="all, delete")
    guarantors = relationship(
        "Guarantor", back_populates="loan", cascade="all, delete")

    class Config:
        orm_mode = True


class Guarantor(Base):
    __tablename__ = "guarantors"

    guarantor_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    national_id = Column(String(20))
    phone_number = Column(String(20))
    email = Column(String(150))
    loan_id = Column(Integer, ForeignKey("loans.loan_id", ondelete="CASCADE"))
    loan = relationship("Loan", back_populates="guarantors",
                        cascade="all, delete")


class Transaction(Base):
    __tablename__ = "transactions"

    transaction_id = Column(Integer, primary_key=True,
                            index=True, autoincrement=True)
    amount = Column(Integer)
    transaction_type = Column(String(50))
    transaction_date = Column(String(50))
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"))
    loan_id = Column(Integer, ForeignKey("loans.loan_id", ondelete="CASCADE"))


class Roles(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey(
        "users.user_id", ondelete="CASCADE"))

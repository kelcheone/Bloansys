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
    balance = Column(Integer)
    user_id = Column(Integer, ForeignKey(
        "users.user_id", ondelete="CASCADE"))
    customer = relationship(
        "User", back_populates="loans", cascade="all, delete")
    guarantors = relationship(
        "Guarantor", back_populates="loan", cascade="all, delete")


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

    transaction_id = Column(Integer, primary_key=True, index=True)
    loan_id = Column(Integer, ForeignKey("loans.loan_id", ondelete="CASCADE"))
    user_id = Column(Integer, ForeignKey(
        "users.user_id", ondelete="CASCADE"))
    borrow_date = Column(String(50))


class Roles(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey(
        "users.user_id", ondelete="CASCADE"))

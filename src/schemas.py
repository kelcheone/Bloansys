from typing import Union

from pydantic import BaseModel


class Loan(BaseModel):
    loan_id: int
    amount: float
    due_date: str
    interest: float
    balance: float
    customer_id: int
    guarantors: list[dict] = []

    class Config:
        orm_mode = True


class Guarantor(BaseModel):
    guarantor_id: int
    first_name: str
    last_name: str
    national_id: str
    phone_number: str
    email: str
    loan_id: int

    class Config:
        orm_mode = True


class Transaction(BaseModel):
    transaction_id: int
    loan_id: int
    customer_id: int
    borrow_date: str

    class Config:
        orm_mode = True


class Customer(BaseModel):
    first_name: str
    last_name: str
    password: str
    national_id: str
    phone_number: str
    email: str

    class Config:
        orm_mode = True

# createCustomer inherits from Customer and hass an additional password field


class CreateCustomer(Customer):
    password: str

    class Config:
        orm_mode = True


class UpdateCustomer(BaseModel):
    first_name: Union[str, None] = None
    last_name: Union[str, None] = None
    password: Union[str, None] = None
    national_id: Union[str, None] = None
    phone_number: Union[str, None] = None
    email: Union[str, None] = None

    class Config:
        orm_mode = True


class ShowCustomer(BaseModel):
    customer_id: int
    first_name: str
    last_name: str
    national_id: str
    phone_number: str
    email: str
    loans: list[Loan] = []

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        orm_mode = True

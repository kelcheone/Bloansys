from typing import Union

from pydantic import BaseModel, EmailStr


class Loan(BaseModel):
    loan_id: int
    amount: float
    due_date: str
    interest: float
    balance: float
    user_id: int
    guarantors: list

    class Config:
        orm_mode = True


class Guarantor(BaseModel):
    guarantor_id: int
    first_name: str
    last_name: str
    national_id: str
    phone_number: str
    email: EmailStr
    loan_id: int

    class Config:
        orm_mode = True


class Transaction(BaseModel):
    transaction_id: int
    loan_id: int
    user_id: int
    borrow_date: str

    class Config:
        orm_mode = True


# user_id
'''
first_name
last_name
password
email
national_id
file_path
phone_number
role
'''


class Customer(BaseModel):
    first_name: str
    last_name: str
    password: str
    national_id: str
    phone_number: str
    email: EmailStr

    class Config:
        orm_mode = True


class UpdateCustomer(BaseModel):
    first_name: Union[str, None] = None
    last_name: Union[str, None] = None
    password: Union[str, None] = None
    national_id: Union[str, None] = None
    phone_number: Union[str, None] = None
    email: Union[EmailStr, None] = None

    class Config:
        orm_mode = True


class ShowCustomer(BaseModel):

    """
    user_id
first_name
last_name
password
email
national_id
file_path
phone_number
    """
    user_id: int
    first_name: str
    last_name: str
    national_id: str
    phone_number: str
    email: EmailStr
    # return loans and guarantors
    loans: list[Loan] = []

    class Config:
        orm_mode = True


class CreateLoan(BaseModel):
    amount: float
    due_date: str
    interest: float


class ShowLoan(BaseModel):
    loan_id: int
    amount: float
    due_date: str
    interest: float
    balance: float
    user_id: int
    customer: Customer
    guarantors: list[Guarantor] = []

    class Config:
        orm_mode = True


class ShowLoanMin(BaseModel):
    loan_id: int
    amount: float
    balance: float
    user_id: int

    class Config:
        orm_mode = True


class UpdateLoan(BaseModel):
    amount: Union[float, None] = None
    due_date: Union[str, None] = None
    interest: Union[float, None] = None
    balance: Union[float, None] = None

    class Config:
        orm_mode = True


class PayLoan(BaseModel):
    loan_id: int
    amount: float

    class Config:
        orm_mode = True


class CreateGuarantor(BaseModel):
    first_name: str
    last_name: str
    national_id: str
    phone_number: str
    email: EmailStr
    loan_id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        orm_mode = True


class TokenData(BaseModel):
    id: int = None

    class Config:
        orm_mode = True


class SignInRequest(BaseModel):
    username: str
    password: str


class TokenJson(BaseModel):
    token: str
    token_type: str

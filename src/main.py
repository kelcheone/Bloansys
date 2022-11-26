from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from .routes import users, loans, login, guarantors, signup, Transactions

app = FastAPI()

# cors
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(users.router)
app.include_router(login.router)
app.include_router(loans.router)
app.include_router(guarantors.router)
app.include_router(signup.router)
app.include_router(Transactions.router)


@ app.get("/")
def read_root():
    return {"Hello": "World"}

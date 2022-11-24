from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from .routes import users
from .routes import login
from .routes import loans
from .routes import guarantors

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


@ app.get("/")
def read_root():
    return {"Hello": "World"}

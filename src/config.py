from pydantic import BaseSettings


class Settings(BaseSettings):
    db_hostname: str
    db_port: str
    db_password: str
    db_name: str
    db_username: str
    secret_key: str
    algorithm: str
    expiry_time: int
    database_url: str

    class Config:
        env_file = ".env"


configs = Settings()

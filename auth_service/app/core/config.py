from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SERVICE_NAME: str = "auth-service"
    DATABASE_URL: str
    REDIS_URL: str = "redis://redis:6379"
    SECRET_KEY: str
    DEBUG: bool = False

    class Config:
        env_file = ".env"

settings = Settings()
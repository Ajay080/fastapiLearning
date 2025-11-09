from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "My FastAPI application"
    debug: bool = False
    database_url: str | None = None

    class Config:
        env_file = ".env"

# 👇 This line should be outside the class
settings = Settings()

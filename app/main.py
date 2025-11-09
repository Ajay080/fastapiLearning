from fastapi import FastAPI 
from app.core.config import settings  # Import settings from the config module

app = FastAPI(title=settings.app_name)  # Initialize FastAPI application with a title

@app.get('/')
def root():
    return {
        "app_name": settings.app_name,
        "debug": settings.debug,
        "database_url": settings.database_url
    }
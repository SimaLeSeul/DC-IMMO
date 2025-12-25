# backend/app/core/config.py
from pydantic_settings import BaseSettings
from typing import List
import secrets

class Settings(BaseSettings):
    """Configuration de l'application"""
    
    # Informations générales
    APP_NAME: str = "Gestion Immobilisations"
    DEBUG: bool = True
    API_V1_STR: str = "/api/v1"
    
    # Base de données
    DATABASE_URL: str = "postgresql://immobilisations_user:immobilisations_pass@localhost:5432/immobilisations_db"
    
    # Sécurité JWT
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS - Origins autorisées
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:3000",  # React dev
        "http://localhost:8000",  # Backend
    ]
    
    class Config:
        env_file = ".env"
        case_sensitive = True

# Instance unique de Settings
settings = Settings()

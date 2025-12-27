"""
Configuration de l'application
"""

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Paramètres de configuration"""
    
    # Application
    APP_NAME: str = "API Gestion Immobilisations"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    
    # Base de données PostgreSQL
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "immobilisations_user"
    POSTGRES_PASSWORD: str = "immobilisations_password"
    POSTGRES_DB: str = "immobilisations_db"
    
    # URL de connexion PostgreSQL
    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )
    
    # JWT
    SECRET_KEY: str = "votre-cle-secrete-super-securisee-changez-moi-en-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS
    BACKEND_CORS_ORIGINS: list = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
    ]
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Instance globale des settings
settings = Settings()

from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    PROJECT_NAME: str = "DC-IMMO API"
    API_V1_STR: str = "/api/v1"
    
    # CORS
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173"
    ]
    
    # Database
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "dcimmo_user"
    POSTGRES_PASSWORD: str = "dcimmo_password"
    POSTGRES_DB: str = "dcimmo_db"
    DB_ECHO: bool = False  # Active les logs SQL si True
    
    @property
    def DATABASE_URL(self) -> str:
        """Construit l'URL de connexion PostgreSQL"""
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}/{self.POSTGRES_DB}"
    
    # Security
    SECRET_KEY: str = "votre-cle-secrete-super-longue-et-complexe-changez-moi-en-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 heures
    
    # First superuser (admin initial)
    FIRST_SUPERUSER_EMAIL: str = "admin@dcimmo.com"
    FIRST_SUPERUSER_PASSWORD: str = "admin123"
    FIRST_SUPERUSER_USERNAME: str = "admin"
    
    class Config:
        case_sensitive = True


settings = Settings()

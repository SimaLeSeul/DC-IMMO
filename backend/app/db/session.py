"""
Configuration de la session SQLAlchemy
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Créer le moteur de base de données
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,  # Vérifie la connexion avant de l'utiliser
    echo=False  # Mettre à True pour voir les requêtes SQL
)

# Créer une factory de sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """
    Générateur de session de base de données
    À utiliser comme dépendance FastAPI
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

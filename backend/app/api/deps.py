"""
Dépendances FastAPI
"""

from typing import Generator
from app.db.session import SessionLocal


def get_db() -> Generator:
    """
    Dependency pour obtenir une session DB
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

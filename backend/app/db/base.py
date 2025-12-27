"""
Import de tous les modèles pour SQLAlchemy
IMPORTANT: Base doit être importé en premier, puis tous les modèles
"""

# 1. Importer Base en premier
from app.db.base_class import Base

# 2. Importer TOUS les modèles (obligatoire pour create_all)
from app.models.user import User
from app.models.categorie import Categorie
from app.models.societe import Societe
from app.models.immobilisation import Immobilisation
from app.models.amortissement import Amortissement

# 3. Exposer Base et tous les modèles
__all__ = [
    "Base",
    "User",
    "Categorie",
    "Societe",
    "Immobilisation",
    "Amortissement",
]

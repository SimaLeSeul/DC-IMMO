"""
Script d'initialisation de la base de données
Crée les tables et ajoute des données de test
"""

import sys
from pathlib import Path

# Ajouter le répertoire backend au PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent))

from sqlalchemy.orm import Session
from datetime import date, datetime

# ✅ FORCER l'import des modèles AVANT create_all
from app.db.base import Base  # Import Base et tous les modèles
from app.db.session import engine, SessionLocal
from app.models.user import User
from app.models.categorie import Categorie
from app.models.societe import Societe
from app.models.immobilisation import Immobilisation
from app.core.security import get_password_hash


def init_db() -> None:
    """Initialise la base de données avec des données de test"""
    
    # 1. Créer toutes les tables
    print("🔧 Création des tables...")
    Base.metadata.drop_all(bind=engine)  # ⚠️ Supprime TOUTES les tables
    Base.metadata.create_all(bind=engine)
    print("✅ Tables créées avec succès!")
    
    # 2. Créer une session
    db: Session = SessionLocal()
    
    try:
        # 3. Vérifier/créer l'utilisateur admin
        print("\n🔧 Vérification utilisateur admin...")
        admin = db.query(User).filter(User.email == "admin@dcimmo.fr").first()
        if not admin:
            admin = User(
                email="admin@dcimmo.fr",
                username="admin",
                hashed_password=get_password_hash("admin123"),
                nom="Admin",
                prenom="Super",
                is_active=True,
                is_superuser=True
            )
            db.add(admin)
            db.commit()
            db.refresh(admin)
            print(f"✅ Utilisateur créé: {admin.email}")
        else:
            print(f"ℹ️  Utilisateur existe déjà: {admin.email}")
        
        # 4. Créer des catégories
        print("\n🔧 Vérification catégories...")
        cat_info = db.query(Categorie).filter(Categorie.code == "INFO").first()
        if not cat_info:
            cat_info = Categorie(
                code="INFO",
                libelle="Informatique",
                duree_amortissement=3,
                taux_amortissement=33.33
            )
            db.add(cat_info)
            db.commit()
            db.refresh(cat_info)
            print(f"✅ Catégorie créée: {cat_info.code} - {cat_info.libelle}")
        else:
            print(f"ℹ️  Catégorie existe déjà: {cat_info.code}")
        
        # 5. Créer une société
        print("\n🔧 Vérification sociétés...")
        societe = db.query(Societe).filter(Societe.code == "SOC001").first()
        if not societe:
            societe = Societe(
                code="SOC001",
                raison_sociale="Société Exemple SARL",
                siret="12345678901234",
                adresse="123 Rue de Test",
                ville="Paris",
                code_postal="75001",
                pays="France"
            )
            db.add(societe)
            db.commit()
            db.refresh(societe)
            print(f"✅ Société créée: {societe.code} - {societe.raison_sociale}")
        else:
            print(f"ℹ️  Société existe déjà: {societe.code}")
        
        # 6. Créer une immobilisation
        print("\n🔧 Vérification immobilisations...")
        immo = db.query(Immobilisation).filter(Immobilisation.code == "IMMO001").first()
        if not immo:
            immo = Immobilisation(
                code="IMMO001",
                libelle="Ordinateur portable Dell",
                date_acquisition=date(2024, 1, 1),
                valeur_origine=1500.00,
                categorie_id=cat_info.id,
                societe_id=societe.id
            )
            db.add(immo)
            db.commit()
            db.refresh(immo)
            print(f"✅ Immobilisation créée: {immo.code} - {immo.libelle}")
        else:
            print(f"ℹ️  Immobilisation existe déjà: {immo.code}")
        
        print("\n🎉 Base de données initialisée avec succès!")
        
    except Exception as e:
        print(f"\n❌ Erreur lors de l'initialisation: {e}")
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    init_db()

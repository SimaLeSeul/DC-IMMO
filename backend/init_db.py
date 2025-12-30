"""
Script d'initialisation de la base de données
"""

from app.db.session import SessionLocal, engine
from app.db.base import Base
from app.models.user import User
from app.models.societe import Societe
from app.models.categorie import Categorie
from app.core.security import get_password_hash


def init_db():
    """Initialise la base de données avec les données de base"""
    
    print("🔧 Création des tables...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print("✅ Tables créées avec succès!")
    
    db = SessionLocal()
    
    try:
        # Créer l'utilisateur admin
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
        
        # Créer les catégories par défaut
        print("\n🔧 Vérification catégories...")
        categories_data = [
            {"code": "INFO", "libelle": "Informatique", "duree": 3, "taux": 33.33},
            {"code": "MOB", "libelle": "Mobilier", "duree": 10, "taux": 10.00},
            {"code": "MAT", "libelle": "Matériel de transport", "duree": 5, "taux": 20.00},
            {"code": "IMMO", "libelle": "Immobilier", "duree": 20, "taux": 5.00},
        ]
        
        for cat_data in categories_data:
            cat = db.query(Categorie).filter(Categorie.code == cat_data["code"]).first()
            if not cat:
                cat = Categorie(
                    code=cat_data["code"],
                    libelle=cat_data["libelle"],
                    duree_amortissement=cat_data["duree"],
                    taux_amortissement=cat_data["taux"]
                )
                db.add(cat)
                db.commit()
                db.refresh(cat)
                print(f"✅ Catégorie créée: {cat.code} - {cat.libelle}")
            else:
                print(f"ℹ️  Catégorie existe déjà: {cat.code} - {cat.libelle}")
        
        # Créer une société de test
        print("\n🔧 Vérification sociétés...")
        societe = db.query(Societe).filter(Societe.code == "SOC001").first()
        
        if not societe:
            societe = Societe(
                code="SOC001",
                raison_sociale="DC Consulting SARL",
                siret="12345678900012",
                adresse="123 rue Example",
                code_postal="75001",
                ville="Paris",
                pays="France",  # ✅ Maintenant supporté
                forme_juridique="SARL"
            )
            db.add(societe)
            db.commit()
            db.refresh(societe)
            print(f"✅ Société créée: {societe.code} - {societe.raison_sociale}")
        else:
            print(f"ℹ️  Société existe déjà: {societe.code} - {societe.raison_sociale}")
        
        print("\n🎉 Base de données initialisée avec succès!")
        
    except Exception as e:
        print(f"\n❌ Erreur lors de l'initialisation: {e}")
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    init_db()

# backend/test_crud.py
from datetime import date
from decimal import Decimal
from sqlalchemy.orm import Session

from app.core.database import SessionLocal, engine, Base
from app.crud import user, societe, immobilisation
from app.schemas.user import UserCreate
from app.schemas.societe import SocieteCreate
from app.schemas.immobilisation import ImmobilisationCreate


def test_crud():
    """Test complet des opérations CRUD."""
    
    # Créer toutes les tables
    Base.metadata.create_all(bind=engine)
    
    db: Session = SessionLocal()
    
    try:
        print("\n" + "="*50)
        print("🧪 TEST DES SERVICES CRUD")
        print("="*50 + "\n")
        
        # 0. Nettoyage préalable
        print("🧹 0. Nettoyage préalable...")
        existing_user = user.get_by_email(db, email="admin@dcimmo.fr")
        if existing_user:
            user.remove(db, id=existing_user.id)
            print("✅ Utilisateur existant supprimé")
        
        existing_societe = societe.get_by_code(db, code="SOC001")
        if existing_societe:
            # Supprimer les immobilisations associées d'abord
            db.query(immobilisation.model).filter(
                immobilisation.model.societe_id == existing_societe.id
            ).delete()
            societe.remove(db, id=existing_societe.id)
            print("✅ Société existante supprimée")
        
        # 1. Test User
        print("\n📝 1. Création d'un utilisateur...")
        user_data = UserCreate(
            email="admin@dcimmo.fr",
            username="admin",
            password="Admin123!",  # ← CHANGÉ : majuscule + chiffre + caractère spécial
            nom="Admin",
            prenom="Super"
        )
        user_created = user.create(db, obj_in=user_data)
        print(f"✅ User créé : {user_created.username} (ID: {user_created.id})")
        
        print("\n🔍 2. Récupération par email...")
        user_found = user.get_by_email(db, email="admin@dcimmo.fr")
        print(f"✅ User trouvé : {user_found.email}")
        
        print("\n🔐 3. Test authentification...")
        authenticated = user.authenticate(db, email="admin@dcimmo.fr", password="Admin123!")  # ← CHANGÉ
        if authenticated:
            print("✅ Authentification : OK")
        else:
            print("❌ Authentification : ÉCHEC")
        
        # 2. Test Societe
        print("\n📝 4. Création d'une société...")
        societe_data = SocieteCreate(
            code="SOC001",
            raison_sociale="Test Company SARL",
            siret="12345678901234",
            adresse="123 Rue de Test",
            code_postal="75001",
            ville="Paris",
            pays="FRA",
            telephone="0123456789",
            email="contact@testcompany.fr"
        )
        societe_created = societe.create(db, obj_in=societe_data)
        print(f"✅ Société créée : {societe_created.raison_sociale} (ID: {societe_created.id})")
        
        print("\n🔍 5. Récupération par code...")
        societe_found = societe.get_by_code(db, code="SOC001")
        print(f"✅ Société trouvée : {societe_found.code}")
        
        # 3. Test Immobilisation
        print("\n📝 6. Création d'une immobilisation...")
        immo_data = ImmobilisationCreate(
            code="IMMO001",
            libelle="Ordinateur portable Dell",
            societe_id=societe_created.id,
            valeur_acquisition=Decimal("1000.00"),
            valeur_residuelle=Decimal("100.00"),
            date_acquisition=date(2024, 1, 15),
            duree_amortissement=3
        )
        immo_created = immobilisation.create(db, obj_in=immo_data)
        print(f"✅ Immobilisation créée : {immo_created.libelle} (ID: {immo_created.id})")
        
        print("\n🔍 7. Récupération des immobilisations de la société...")
        immos = immobilisation.get_by_societe(db, societe_id=societe_created.id)
        print(f"✅ {len(immos)} immobilisation(s) trouvée(s)")
        
        # 4. Test liste
        print("\n📋 8. Liste de tous les utilisateurs...")
        all_users = user.get_multi(db)
        print(f"✅ {len(all_users)} utilisateur(s) en base")
        
        print("\n📋 9. Liste de toutes les sociétés...")
        all_societes = societe.get_multi(db)
        print(f"✅ {len(all_societes)} société(s) en base")
        
        print("\n📋 10. Liste de toutes les immobilisations...")
        all_immos = immobilisation.get_multi(db)
        print(f"✅ {len(all_immos)} immobilisation(s) en base")
        
        # 5. Test update
        print("\n🔄 11. Mise à jour de l'immobilisation...")
        from app.schemas.immobilisation import ImmobilisationUpdate
        immo_update = ImmobilisationUpdate(
            libelle="Ordinateur portable Dell XPS 15",
            valeur_residuelle=Decimal("150.00")
        )
        immo_updated = immobilisation.update(db, db_obj=immo_created, obj_in=immo_update)
        print(f"✅ Immobilisation mise à jour : {immo_updated.libelle}")
        print(f"   Nouvelle valeur résiduelle : {immo_updated.valeur_residuelle}€")
        
        # 6. Test delete
        print("\n🗑️  12. Suppression de l'immobilisation...")
        immobilisation.remove(db, id=immo_created.id)
        print(f"✅ Immobilisation supprimée : ID {immo_created.id}")
        
        # Vérification
        deleted_immo = immobilisation.get(db, id=immo_created.id)
        if deleted_immo is None:
            print("✅ Vérification : Immobilisation bien supprimée")
        else:
            print("❌ Vérification : L'immobilisation existe encore !")
        
        print("\n" + "="*50)
        print("✅ TOUS LES TESTS SONT PASSÉS !")
        print("="*50 + "\n")
        
    except Exception as e:
        print(f"\n❌ ERREUR : {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        db.close()


if __name__ == "__main__":
    test_crud()

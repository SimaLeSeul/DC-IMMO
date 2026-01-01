import sys
import logging
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy.orm import Session
from app.db.session import SessionLocal, engine
from app.db.base import Base
from app.models.user import User
from app.models.role import Role
from app.models.societe import Societe
from app.models.exercice import Exercice
from app.models.plan_comptable import PlanComptable
from app.models.compte_comptable import CompteComptable
from app.models.categorie import Categorie
from app.core.security import get_password_hash

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init_db(db: Session) -> None:
    """Initialise la base de données avec les données de base"""
    
    try:
        # Créer les rôles de base
        logger.info("📋 Création des rôles...")
        roles_data = [
            {"code": "ADMIN", "libelle": "Administrateur", "description": "Accès complet au système"},
            {"code": "MANAGER", "libelle": "Gestionnaire", "description": "Gestion des immobilisations et rapports"},
            {"code": "COMPTABLE", "libelle": "Comptable", "description": "Gestion comptable et amortissements"},
            {"code": "USER", "libelle": "Utilisateur", "description": "Consultation uniquement"}
        ]
        
        roles = {}
        for role_data in roles_data:
            role = db.query(Role).filter(Role.code == role_data["code"]).first()
            if not role:
                role = Role(**role_data)
                db.add(role)
                logger.info(f"✅ Rôle créé: {role_data['libelle']}")
            roles[role_data["code"]] = role
        
        db.commit()
        
        # Créer un utilisateur admin par défaut
        logger.info("👤 Création de l'utilisateur admin...")
        admin = db.query(User).filter(User.email == "admin@dcimmo.com").first()
        
        if not admin:
            admin = User(
                email="admin@dcimmo.com",
                nom="Système",
                prenom="Administrateur",
                hashed_password=get_password_hash("Admin@2024!"),
                is_active=True,
                is_superuser=True
            )
            admin.roles.append(roles["ADMIN"])
            db.add(admin)
            db.commit()
            logger.info("✅ Utilisateur admin créé")
            logger.info("   📧 Email: admin@dcimmo.com")
            logger.info("   🔑 Password: Admin@2024!")
        else:
            logger.info("ℹ️  Utilisateur admin déjà existant")
        
        # Créer une société de démonstration
        logger.info("🏢 Création de la société de démonstration...")
        societe = db.query(Societe).filter(Societe.code == "DEMO").first()
        if not societe:
            societe = Societe(
                code="DEMO",
                raison_sociale="Société de Démonstration SARL",
                siret="12345678901234",
                adresse="123 Avenue des Champs-Élysées",
                ville="Paris",
                code_postal="75008",
                pays="France",
                telephone="+33 1 23 45 67 89",
                email="contact@demo-societe.fr"
            )
            db.add(societe)
            db.commit()
            logger.info("✅ Société de démonstration créée")
        else:
            logger.info("ℹ️  Société déjà existante")
        
        # Créer un exercice comptable
        logger.info("📅 Création de l'exercice comptable 2024...")
        from datetime import date
        exercice = db.query(Exercice).filter(
            Exercice.societe_id == societe.id,
            Exercice.annee == 2024
        ).first()
        
        if not exercice:
            exercice = Exercice(
                societe_id=societe.id,
                annee=2024,
                date_debut=date(2024, 1, 1),
                date_fin=date(2024, 12, 31),
                est_cloture=False,
                statut='OUVERT'
            )

            db.add(exercice)
            db.commit()
            logger.info("✅ Exercice comptable 2024 créé")
        else:
            logger.info("ℹ️  Exercice 2024 déjà existant")
        
        # Créer un plan comptable
        logger.info("📊 Création du plan comptable...")
        plan = db.query(PlanComptable).filter(
            PlanComptable.societe_id == societe.id,
            PlanComptable.code == "PCG"
        ).first()
        
        if not plan:
            plan = PlanComptable(
                societe_id=societe.id,
                code="PCG",
                nom="Plan Comptable Général",  # ✅ Champ obligatoire ajouté
                libelle="Plan Comptable Général",
                description="Plan comptable général français",
                is_actif=True
            )
            db.add(plan)
            db.commit()
            logger.info("✅ Plan comptable créé")
            
            # Créer quelques comptes de base
            logger.info("📝 Création des comptes comptables de base...")
            comptes_data = [
                {"numero": "2154", "libelle": "Matériel industriel", "type_compte": "IMMOBILISATION"},
                {"numero": "2183", "libelle": "Matériel de bureau et informatique", "type_compte": "IMMOBILISATION"},
                {"numero": "2182", "libelle": "Matériel de transport", "type_compte": "IMMOBILISATION"},
                {"numero": "28154", "libelle": "Amortissement matériel industriel", "type_compte": "AMORTISSEMENT"},
                {"numero": "28183", "libelle": "Amortissement matériel de bureau", "type_compte": "AMORTISSEMENT"},
                {"numero": "68112", "libelle": "Dotations aux amortissements", "type_compte": "CHARGE"},
            ]
            
            for compte_data in comptes_data:
                compte = CompteComptable(
                    plan_comptable_id=plan.id,
                    **compte_data,
                    est_actif=True
                )
                db.add(compte)
            
            db.commit()
            logger.info(f"✅ {len(comptes_data)} comptes comptables créés")
        else:
            logger.info("ℹ️  Plan comptable déjà existant")
        
        # Créer des catégories
        logger.info("🏷️  Création des catégories d'immobilisations...")
        categories_data = [
            {"code": "MAT_INFO", "libelle": "Matériel Informatique"},
            {"code": "MAT_INDUS", "libelle": "Matériel Industriel"},
            {"code": "MAT_TRANSP", "libelle": "Matériel de Transport"},
            {"code": "MOB_BUR", "libelle": "Mobilier de Bureau"},
        ]
        
        for cat_data in categories_data:
            cat = db.query(Categorie).filter(
                Categorie.societe_id == societe.id,
                Categorie.code == cat_data["code"]
            ).first()
            
            if not cat:
                cat = Categorie(
                    societe_id=societe.id,
                    **cat_data
                )
                db.add(cat)
        
        db.commit()
        logger.info(f"✅ {len(categories_data)} catégories créées")
        
        logger.info("\n✨ Initialisation terminée avec succès!")
        logger.info("\n🔐 Identifiants de connexion:")
        logger.info("   📧 Email: admin@dcimmo.com")
        logger.info("   🔑 Mot de passe: Admin@2024!")
        
    except Exception as e:
        logger.error(f"❌ Erreur lors de l'initialisation: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
        raise


if __name__ == "__main__":
    logger.info("🚀 Démarrage de l'initialisation de la base de données...\n")
    logger.info("📦 Création des tables...")
    Base.metadata.create_all(bind=engine)
    logger.info("✅ Tables créées\n")
    
    db = SessionLocal()
    try:
        init_db(db)
    finally:
        db.close()
        logger.info("\n👋 Connexion à la base fermée")

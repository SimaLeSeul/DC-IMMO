# Import all the models, so that Base has them before being
# imported by Alembic or other parts of the app
from app.db.base_class import Base  # noqa

# ORDRE CRITIQUE : importer les modèles SANS dépendances en premier
from app.models.role import Role  # noqa
from app.models.societe import Societe  # noqa
from app.models.plan_comptable import PlanComptable  # noqa
from app.models.compte_comptable import CompteComptable  # noqa
from app.models.exercice import Exercice  # noqa
from app.models.categorie import Categorie  # noqa

# Modèles qui dépendent de User (AVANT User!)
from app.models.notification import Notification  # noqa
from app.models.audit_log import AuditLog  # noqa

# User (après ses dépendances)
from app.models.user import User  # noqa

# Modèles qui dépendent de User ou autres (APRÈS User)
from app.models.immobilisation import Immobilisation  # noqa
from app.models.amortissement import Amortissement  # noqa
from app.models.dotation import Dotation  # noqa
from app.models.cession import Cession  # noqa
from app.models.evenement import Evenement  # noqa
from app.models.document import Document  # noqa
from app.models.piece_jointe import PieceJointe  # noqa

# test_quick.py
from app.db.session import SessionLocal
from app.db import base  # ← IMPORTANT : Force l'import de tous les modèles
from app.models.compte_comptable import CompteComptable
from app.models.immobilisation import Immobilisation

print("🧪 Test rapide des relations...")
db = SessionLocal()

try:
    print("\n1. Vérification des propriétés:")
    print(f"   - CompteComptable.immobilisations_acquisition: {hasattr(CompteComptable, 'immobilisations_acquisition')}")
    print(f"   - CompteComptable.immobilisations_amortissement: {hasattr(CompteComptable, 'immobilisations_amortissement')}")
    print(f"   - CompteComptable.immobilisations_dotation: {hasattr(CompteComptable, 'immobilisations_dotation')}")
    
    print("\n2. Test de requêtes:")
    comptes = db.query(CompteComptable).count()
    immos = db.query(Immobilisation).count()
    print(f"   - Comptes comptables: {comptes}")
    print(f"   - Immobilisations: {immos}")
    
    print("\n3. Test de jointure:")
    result = db.query(Immobilisation).join(CompteComptable, Immobilisation.compte_acquisition_id == CompteComptable.id, isouter=True).first()
    print(f"   - Jointure OK: {result is not None or immos == 0}")
    
    print("\n✅ TOUT FONCTIONNE!")
    
except Exception as e:
    print(f"\n❌ ERREUR: {e}")
    import traceback
    traceback.print_exc()
    
finally:
    db.close()

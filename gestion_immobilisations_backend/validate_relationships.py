#!/usr/bin/env python3
import re
from pathlib import Path
from collections import defaultdict

models_dir = Path("app/models")

# Structure: relationships[ClassA][property_name] = (ClassB, back_populates_name)
relationships = defaultdict(dict)

print("🔍 Analyse des relations SQLAlchemy...\n")

# Parcourir tous les fichiers models
for file in models_dir.glob("*.py"):
    if file.name in ["__init__.py", "base.py"]:
        continue
    
    content = file.read_text()
    
    # Extraire le nom de la classe
    class_match = re.search(r'class (\w+)\(', content)
    if not class_match:
        continue
    class_name = class_match.group(1)
    
    # Trouver toutes les relations
    rel_pattern = r'(\w+)\s*=\s*relationship\(["\'](\w+)["\']\s*,\s*back_populates=["\'](\w+)["\']'
    for match in re.finditer(rel_pattern, content):
        property_name = match.group(1)
        target_class = match.group(2)
        back_populates = match.group(3)
        
        relationships[class_name][property_name] = (target_class, back_populates)

# Vérifier la réciprocité
errors = []
for class_name, props in relationships.items():
    for prop_name, (target_class, back_pop) in props.items():
        # Vérifier si la classe cible a la relation inverse
        if target_class not in relationships:
            errors.append(f"❌ {class_name}.{prop_name} → {target_class} (classe introuvable)")
            continue
        
        if back_pop not in relationships[target_class]:
            errors.append(f"❌ {class_name}.{prop_name} → {target_class}.{back_pop} (relation manquante)")
        else:
            reverse_target, reverse_back = relationships[target_class][back_pop]
            if reverse_target != class_name:
                errors.append(f"❌ {class_name}.{prop_name} ↔️ {target_class}.{back_pop} → {reverse_target} (incohérence)")
            elif reverse_back != prop_name:
                errors.append(f"❌ {class_name}.{prop_name} ↔️ {target_class}.{back_pop} ← {reverse_back} (back_populates incorrect)")

if errors:
    print("⚠️  ERREURS DÉTECTÉES:\n")
    for error in errors:
        print(error)
    print(f"\n❌ {len(errors)} erreur(s) trouvée(s)")
else:
    print("✅ Toutes les relations sont cohérentes!")

print(f"\n📊 {len(relationships)} classes analysées")

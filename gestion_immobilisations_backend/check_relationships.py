import re
from pathlib import Path

models_dir = Path("app/models")
relationships = {}

# Lire tous les fichiers models
for file in models_dir.glob("*.py"):
    if file.name == "__init__.py":
        continue
    
    content = file.read_text()
    
    # Trouver le nom de la classe
    class_match = re.search(r'class (\w+)\(', content)
    if not class_match:
        continue
    class_name = class_match.group(1)
    
    # Trouver tous les back_populates
    back_pops = re.findall(r'back_populates=["\'](\w+)["\']', content)
    
    for back_pop in back_pops:
        if class_name not in relationships:
            relationships[class_name] = set()
        relationships[class_name].add(back_pop)

print("🔍 Relations déclarées par classe:\n")
for cls, rels in sorted(relationships.items()):
    print(f"{cls}:")
    for rel in sorted(rels):
        print(f"  - {rel}")
    print()

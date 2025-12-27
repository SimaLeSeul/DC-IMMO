#!/usr/bin/env zsh

autoload -U colors && colors

echo "${fg[cyan]}🔧 Reconstruction des fichiers ignorés par .gitignore${reset_color}\n"

# =============================================================================
# 1. BACKEND .ENV
# =============================================================================
echo "${fg[green]}1️⃣  Création de backend/.env...${reset_color}"

cat > backend/.env << 'ENVFILE'
# .env - Configuration DC-IMMO Backend

# Project
PROJECT_NAME=DC-IMMO API
API_V1_STR=/api/v1

# Database PostgreSQL
POSTGRES_SERVER=localhost
POSTGRES_USER=immobilisations_user
POSTGRES_PASSWORD=immobilisations_pass
POSTGRES_DB=immobilisations_db
POSTGRES_PORT=5432

# Database URL
DATABASE_URL=postgresql://immobilisations_user:immobilisations_pass@localhost:5432/immobilisations_db

# Security - JWT
SECRET_KEY=09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=10080

# First Superuser
FIRST_SUPERUSER_EMAIL=admin@dcimmo.fr
FIRST_SUPERUSER_PASSWORD=admin123

# CORS Origins
BACKEND_CORS_ORIGINS=["http://localhost:3000","http://localhost:5173","http://localhost:8080"]

# Environment
ENVIRONMENT=development
ENVFILE

echo "${fg[blue]}✓ backend/.env créé${reset_color}"

# =============================================================================
# 2. VÉRIFIER SI PYTHON VENV EXISTE
# =============================================================================
echo "\n${fg[green]}2️⃣  Vérification de l'environnement virtuel Python...${reset_color}"

if [[ ! -d "backend/venv" ]]; then
    echo "${fg[yellow]}⚠️  venv n'existe pas, création...${reset_color}"
    cd backend
    python3 -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    cd ..
    echo "${fg[blue]}✓ venv créé et dépendances installées${reset_color}"
else
    echo "${fg[blue]}✓ venv existe déjà${reset_color}"
fi

# =============================================================================
# 3. FRONTEND .ENV (SI BESOIN)
# =============================================================================
echo "\n${fg[green]}3️⃣  Vérification de frontend/.env...${reset_color}"

if [[ ! -f "frontend/.env" ]]; then
    cat > frontend/.env << 'FRONTENV'
REACT_APP_API_URL=http://localhost:8000
REACT_APP_API_V1_STR=/api/v1
FRONTENV
    echo "${fg[blue]}✓ frontend/.env créé${reset_color}"
else
    echo "${fg[blue]}✓ frontend/.env existe déjà${reset_color}"
fi

# =============================================================================
# 4. VÉRIFIER DOCKER VOLUME
# =============================================================================
echo "\n${fg[green]}4️⃣  Vérification du volume Docker PostgreSQL...${reset_color}"

if docker volume ls | grep -q "dc-immo_postgres_data"; then
    echo "${fg[blue]}✓ Volume PostgreSQL existe${reset_color}"
else
    echo "${fg[yellow]}⚠️  Volume PostgreSQL n'existe pas (sera créé au premier démarrage)${reset_color}"
fi

# =============================================================================
# 5. RÉSUMÉ
# =============================================================================
echo "\n${fg[cyan]}═══════════════════════════════════════════════════${reset_color}"
echo "${fg[cyan]}✅ RECONSTRUCTION TERMINÉE${reset_color}"
echo "${fg[cyan]}═══════════════════════════════════════════════════${reset_color}\n"

echo "${fg[yellow]}📋 Fichiers créés/vérifiés:${reset_color}"
echo "  ${fg[green]}✓${reset_color} backend/.env"
echo "  ${fg[green]}✓${reset_color} backend/venv/"
echo "  ${fg[green]}✓${reset_color} frontend/.env"

echo "\n${fg[yellow]}🚀 Prochaines étapes:${reset_color}"
echo "  ${fg[cyan]}1.${reset_color} Démarrer PostgreSQL:"
echo "     ${fg[blue]}docker-compose up -d db${reset_color}"
echo ""
echo "  ${fg[cyan]}2.${reset_color} Attendre que PostgreSQL soit prêt (10-15 sec):"
echo "     ${fg[blue]}docker-compose logs -f db${reset_color}"
echo "     ${fg[green]}(Attendez le message: 'database system is ready')${reset_color}"
echo ""
echo "  ${fg[cyan]}3.${reset_color} Initialiser la base de données:"
echo "     ${fg[blue]}cd backend${reset_color}"
echo "     ${fg[blue]}source venv/bin/activate${reset_color}"
echo "     ${fg[blue]}python init_db.py${reset_color}"
echo ""
echo "  ${fg[cyan]}4.${reset_color} Démarrer le backend:"
echo "     ${fg[blue]}uvicorn app.main:app --reload${reset_color}"
echo ""
echo "  ${fg[cyan]}5.${reset_color} Tester l'API:"
echo "     ${fg[blue]}http://localhost:8000/docs${reset_color}"

echo "\n${fg[yellow]}🔑 Identifiants par défaut:${reset_color}"
echo "  Email:    ${fg[green]}admin@dcimmo.fr${reset_color}"
echo "  Password: ${fg[green]}admin123${reset_color}"

echo "\n${fg[yellow]}📊 Vérifier l'état:${reset_color}"
echo "  ${fg[blue]}docker-compose ps${reset_color}     # État des containers"
echo "  ${fg[blue]}docker-compose logs db${reset_color} # Logs PostgreSQL"


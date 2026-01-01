from fastapi import FastAPI

app = FastAPI(
    title="DC-IMMO API",
    version="1.0.0",
    description="API de gestion des immobilisations"
)

@app.get("/")
async def root():
    return {"message": "Bienvenue sur l'API DC-IMMO"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

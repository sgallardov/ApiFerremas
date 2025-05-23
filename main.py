from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from rutas import usuarios, vendedores, sucursales, contactos, productos, productos_usd, pagos
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

app = FastAPI(
    title="API Ferremas",
    description="API para el sistema de Ferremas",
    version="1.0.0"
)

# Obtener el entorno actual y puerto
ENVIRONMENT = os.getenv("ENVIRONMENT", "production")
FRONTEND_URL = os.getenv("FRONTEND_URL", "*")

# Configuración de CORS
origins = [
    "*",  # Permite todas las origins en desarrollo
    "http://localhost",
    "http://localhost:3000",
    "https://ferremas.cl",
    "https://www.ferremas.cl"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas
app.include_router(usuarios.router)
app.include_router(vendedores.router)
app.include_router(sucursales.router)
app.include_router(contactos.router)
app.include_router(productos.router)
app.include_router(productos_usd.router)
app.include_router(pagos.router)

@app.get("/")
async def root():
    return {
        "message": "Bienvenido a la API de Ferremas",
        "environment": ENVIRONMENT,
        "version": "1.0.0",
        "status": "running"
    }

# No es necesario el bloque if __name__ == "__main__" ya que Railway usará el Procfile

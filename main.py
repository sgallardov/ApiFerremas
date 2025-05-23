from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from rutas import usuarios, vendedores, sucursales, contactos, productos, productos_usd, pagos
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

app = FastAPI()

# Obtener el entorno actual
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")

# Configuración de CORS basada en el entorno
origins = ["http://localhost:3000"]  # URL de desarrollo por defecto

if ENVIRONMENT == "production":
    origins.append(FRONTEND_URL)  # URL de producción

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
        "version": "1.0.0"
    }

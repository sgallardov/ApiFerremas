from fastapi import APIRouter, HTTPException
from modelos.usuario import obtener_usuarios

router = APIRouter(
    tags=["usuarios"]
)

@router.get("/usuarios", response_model=list)
async def ruta_obtener_usuarios():
    """
    Endpoint para obtener la lista de todos los usuarios.
    """
    usuarios = obtener_usuarios()
    if usuarios is not None:
        return usuarios
    raise HTTPException(status_code=500, detail="No se pudieron obtener los usuarios")
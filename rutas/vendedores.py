from fastapi import APIRouter, HTTPException
from modelos.vendedor import obtener_vendedores, obtener_vendedor_por_id, obtener_vendedores_por_sucursal
from utilidades.auth import autenticar_usuario

router = APIRouter(
    tags=["vendedoresFerremas"]
)

@router.get("/vendedores", response_model=list)
async def ruta_obtener_vendedores(username: str, password: str):
    # Verificar credenciales
    usuario = autenticar_usuario(username, password)
    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    if usuario["role"] != "admin":
        raise HTTPException(status_code=403, detail="Se requiere rol de administrador")

    vendedores = obtener_vendedores()
    if vendedores is not None:
        return vendedores
    raise HTTPException(status_code=500, detail="No se pudieron obtener los vendedores")

@router.get("/vendedores/{vendedor_id}", response_model=dict)
async def ruta_obtener_vendedor_por_id(vendedor_id: str, username: str, password: str):
    # Verificar credenciales
    usuario = autenticar_usuario(username, password)
    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    if usuario["role"] != "admin":
        raise HTTPException(status_code=403, detail="Se requiere rol de administrador")

    vendedor = obtener_vendedor_por_id(vendedor_id)
    if vendedor is not None:
        return vendedor
    raise HTTPException(status_code=404, detail=f"No se pudo encontrar el vendedor con ID {vendedor_id}")

@router.get("/vendedores/sucursal/{sucursal_id}", response_model=list)
async def ruta_obtener_vendedores_por_sucursal(sucursal_id: str, username: str, password: str):
    # Verificar credenciales
    usuario = autenticar_usuario(username, password)
    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    if usuario["role"] != "admin":
        raise HTTPException(status_code=403, detail="Se requiere rol de administrador")

    vendedores = obtener_vendedores_por_sucursal(sucursal_id)
    if vendedores is not None:
        return vendedores
    raise HTTPException(status_code=500, detail=f"No se pudieron obtener los vendedores de la sucursal {sucursal_id}")
from fastapi import APIRouter, HTTPException
from modelos import sucursal
from utilidades.auth import autenticar_usuario

router = APIRouter(
    prefix="/sucursales",
    tags=["sucursalesFerremas"]
)

@router.get("/", summary="Obtener todas las sucursales")
async def listar_sucursales(username: str, password: str):
    """
    Obtener todas las sucursales.
    Requiere autenticación de cliente.
    """
    # Verificar credenciales
    usuario = autenticar_usuario(username, password)
    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    if usuario["role"] != "client":
        raise HTTPException(status_code=403, detail="Solo los clientes pueden ver las sucursales")

    resultado = sucursal.obtener_sucursales()
    if resultado is None:
        raise HTTPException(status_code=500, detail="No se pudieron obtener las sucursales")
    return resultado

@router.get("/{sucursal_id}", summary="Obtener sucursal por ID")
async def obtener_sucursal(sucursal_id: str, username: str, password: str):
    """
    Obtener una sucursal específica por su ID.
    Requiere autenticación de cliente.
    """
    # Verificar credenciales
    usuario = autenticar_usuario(username, password)
    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    if usuario["role"] != "client":
        raise HTTPException(status_code=403, detail="Solo los clientes pueden ver las sucursales")

    resultado = sucursal.obtener_sucursal_por_id(sucursal_id)
    if resultado is None:
        raise HTTPException(status_code=404, detail="Sucursal no encontrada")
    return resultado
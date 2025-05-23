from fastapi import APIRouter, HTTPException
from modelos.contacto import enviar_contacto, obtener_solicitudes_contacto
from utilidades.auth import autenticar_usuario

router = APIRouter(
    tags=["contactoSoporte"]
)

@router.post("/contacto", response_model=dict)
async def ruta_enviar_contacto(mensaje: str, username: str, password: str):
    """
    Endpoint para enviar una solicitud de contacto.
    Requiere autenticación de cliente.
    Solo requiere el mensaje del cliente.
    """
    # Verificar credenciales
    usuario = autenticar_usuario(username, password)
    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    if usuario["role"] != "client":
        raise HTTPException(status_code=403, detail="Solo los clientes pueden enviar solicitudes de contacto")
    
    resultado = enviar_contacto({"mensaje": mensaje})
    if resultado is not None:
        return {"mensaje": "Solicitud de contacto enviada exitosamente", "solicitud": resultado}
    raise HTTPException(status_code=500, detail="No se pudo enviar la solicitud de contacto")

@router.get("/contacto", response_model=list)
async def ruta_obtener_solicitudes_contacto(username: str, password: str):
    """
    Endpoint para obtener todas las solicitudes de contacto.
    Requiere autenticación de administrador.
    """
    # Verificar credenciales
    usuario = autenticar_usuario(username, password)
    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    if usuario["role"] != "admin":
        raise HTTPException(status_code=403, detail="Se requiere rol de administrador")

    solicitudes = obtener_solicitudes_contacto()
    if solicitudes is not None:
        return solicitudes
    raise HTTPException(status_code=500, detail="No se pudieron obtener las solicitudes de contacto")
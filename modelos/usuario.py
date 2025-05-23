import requests
import json
import os
from pathlib import Path

API_URL = "https://ea2p2assets-production.up.railway.app"
AUTH_TOKEN = "SaGrP9ojGS39hU9ljqbXxQ=="

HEADERS = {
    "Authorization": f"Bearer {AUTH_TOKEN}",
    "Content-Type": "application/json",
    "X-Authentication": AUTH_TOKEN
}

# Definimos los permisos asociados a cada rol
ROLES_PERMISOS = {
    "admin": ["crear_producto", "editar_producto", "eliminar_producto", "ver_pedidos", "gestionar_usuarios"],
    "mantenedor": ["crear_producto", "editar_producto", "ver_pedidos"],
    "jefe_tienda": ["ver_pedidos", "gestionar_vendedores"],
    "bodega": ["ver_pedidos"],
    "cliente": ["ver_productos", "realizar_pedido"],
    "service_account": ["integracion_externa"]
}

# Ruta al archivo de usuarios
USUARIOS_FILE = Path(__file__).parent.parent / "data" / "usuarios.json"

def _ensure_data_directory():
    """Asegura que el directorio data y el archivo usuarios.json existan"""
    data_dir = Path(__file__).parent.parent / "data"
    data_dir.mkdir(exist_ok=True)
    
    if not USUARIOS_FILE.exists():
        with open(USUARIOS_FILE, 'w', encoding='utf-8') as f:
            json.dump({"usuarios": []}, f, indent=4)

def _load_usuarios():
    """Carga los usuarios desde el archivo JSON"""
    _ensure_data_directory()
    try:
        with open(USUARIOS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"usuarios": []}

def _save_usuarios(usuarios_data):
    """Guarda los usuarios en el archivo JSON"""
    _ensure_data_directory()
    with open(USUARIOS_FILE, 'w', encoding='utf-8') as f:
        json.dump(usuarios_data, f, indent=4)

def obtener_usuarios():
    """
    Obtiene la lista de todos los usuarios.
    """
    return _load_usuarios()["usuarios"]

def obtener_usuario_por_id(usuario_id):
    """
    Obtiene los detalles de un usuario específico por su ID.
    """
    usuarios = _load_usuarios()["usuarios"]
    for usuario in usuarios:
        if usuario["id"] == usuario_id:
            return usuario
    return None

def crear_usuario(data_usuario):
    """
    Crea un nuevo usuario con los datos proporcionados.
    """
    usuarios_data = _load_usuarios()
    
    # Generar nuevo ID
    ultimo_id = max([int(u["id"].replace("U", "")) for u in usuarios_data["usuarios"]] + [0])
    nuevo_id = f"U{str(ultimo_id + 1).zfill(3)}"
    
    # Crear nuevo usuario
    nuevo_usuario = {
        "id": nuevo_id,
        **data_usuario
    }
    
    usuarios_data["usuarios"].append(nuevo_usuario)
    _save_usuarios(usuarios_data)
    return nuevo_usuario

def obtener_permisos_por_rol(rol):
    """
    Devuelve la lista de permisos asociados a un rol específico.
    """
    return ROLES_PERMISOS.get(rol, [])

def verificar_permiso(rol, permiso):
    """
    Verifica si un rol tiene un permiso específico.
    """
    permisos = obtener_permisos_por_rol(rol)
    return permiso in permisos

def obtener_usuario_por_username(username):
    """
    Obtiene un usuario por su nombre de usuario.
    """
    usuarios = _load_usuarios()["usuarios"]
    for usuario in usuarios:
        if usuario["user"] == username:
            return usuario
    return None
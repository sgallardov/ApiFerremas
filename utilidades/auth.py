import json

def obtener_usuario_por_username(username: str):
    try:
        with open("data/usuarios.json", "r") as f:
            data = json.load(f)
            for usuario in data["usuarios"]:
                if usuario["user"] == username:
                    return usuario
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None
    return None

def autenticar_usuario(username: str, password: str):
    usuario = obtener_usuario_por_username(username)
    if not usuario:
        return None
    if usuario["password"] != password:
        return None
    return usuario 
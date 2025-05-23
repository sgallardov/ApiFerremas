import requests

API_URL = "https://ea2p2assets-production.up.railway.app"
AUTH_TOKEN = "SaGrP9ojGS39hU9ljqbXxQ=="

HEADERS = {
    "Authorization": f"Bearer {AUTH_TOKEN}",
    "Content-Type": "application/json",
    "X-Authentication": AUTH_TOKEN
}

def obtener_productos():
    try:
        response = requests.get(f"{API_URL}/data/articulos", headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Error al obtener productos:", e)
        return None

def obtener_producto_por_id(producto_id):
    try:
        response = requests.get(f"{API_URL}/data/articulos/{producto_id}", headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Error al obtener producto:", e)
        return None

def crear_producto(data_producto):
    try:
        response = requests.post(f"{API_URL}/data/articulos", json=data_producto, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Error al crear producto:", e)
        return None

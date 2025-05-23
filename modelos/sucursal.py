import requests

API_URL = "https://ea2p2assets-production.up.railway.app"
AUTH_TOKEN = "SaGrP9ojGS39hU9ljqbXxQ=="

HEADERS = {
    "Authorization": f"Bearer {AUTH_TOKEN}",
    "Content-Type": "application/json",
    "X-Authentication": AUTH_TOKEN
}

def obtener_sucursales():
    """
    Obtiene la lista de todas las sucursales.
    """
    try:
        response = requests.get(f"{API_URL}/data/sucursales", headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Error al obtener sucursales:", e)
        return None

def obtener_sucursal_por_id(sucursal_id):
    """
    Obtiene los detalles de una sucursal específica por su ID.
    """
    try:
        response = requests.get(f"{API_URL}/data/sucursales/{sucursal_id}", headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error al obtener la sucursal con ID {sucursal_id}:", e)
        return None

def crear_sucursal(data_sucursal):
    """
    Crea una nueva sucursal con los datos proporcionados.
    """
    try:
        response = requests.post(f"{API_URL}/data/sucursales", json=data_sucursal, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Error al crear sucursal:", e)
        return None
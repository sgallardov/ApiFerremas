import requests

API_URL = "https://ea2p2assets-production.up.railway.app"
AUTH_TOKEN = "SaGrP9ojGS39hU9ljqbXxQ=="

HEADERS = {
    "Authorization": f"Bearer {AUTH_TOKEN}",
    "Content-Type": "application/json",
    "X-Authentication": AUTH_TOKEN
}

def obtener_vendedores():
    """
    Obtiene la lista de todos los vendedores.
    """
    try:
        response = requests.get(f"{API_URL}/data/vendedores", headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Error al obtener vendedores:", e)
        return None

def obtener_vendedor_por_id(vendedor_id):
    """
    Obtiene los detalles de un vendedor específico por su ID.
    """
    try:
        response = requests.get(f"{API_URL}/data/vendedores/{vendedor_id}", headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error al obtener el vendedor con ID {vendedor_id}:", e)
        return None

def obtener_vendedores_por_sucursal(sucursal_id):
    """
    Obtiene todos los vendedores que pertenecen a una sucursal específica.
    """
    try:
        # Primero obtenemos todos los vendedores
        vendedores = obtener_vendedores()
        if vendedores is None:
            return None
        
        # Filtramos los vendedores por sucursal
        vendedores_sucursal = [
            vendedor for vendedor in vendedores 
            if vendedor.get("sucursal") == sucursal_id
        ]
        
        return vendedores_sucursal
    except Exception as e:
        print(f"Error al obtener vendedores de la sucursal {sucursal_id}:", e)
        return None


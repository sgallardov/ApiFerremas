import requests
from decimal import Decimal

API_KEY = "cur_live_vT3RbaFj5gzhdv2Y7GPrx3kwRqC19puYKx4rPx1S"
BASE_URL = "https://api.currencyapi.com/v3"

def obtener_tasa_cambio_clp_usd():
    """
    Obtiene la tasa de cambio actual de CLP a USD usando currencyapi.com
    """
    try:
        url = f"{BASE_URL}/latest"
        params = {
            "apikey": API_KEY,
            "base_currency": "USD",  # Cambiamos a USD como base
            "currencies": "CLP"      # Obtenemos el valor en CLP
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        # Obtenemos cuántos CLP equivalen a 1 USD y calculamos el inverso
        clp_rate = Decimal(str(data['data']['CLP']['value']))
        return Decimal('1') / clp_rate  # Convertimos a cuántos USD equivalen a 1 CLP
    except Exception as e:
        print(f"Error al obtener tasa de cambio: {e}")
        return None

def convertir_clp_a_usd(monto_clp):
    """
    Convierte un monto de CLP a USD usando la tasa actual
    """
    try:
        # Aseguramos que monto_clp sea un Decimal
        if isinstance(monto_clp, str):
            monto_clp = monto_clp.replace(',', '')  # Removemos comas si existen
        monto_decimal = Decimal(str(monto_clp))
        
        tasa = obtener_tasa_cambio_clp_usd()
        if tasa is None:
            return None
        
        resultado = monto_decimal * tasa
        # Redondeamos a 2 decimales
        return round(resultado, 2)
    except Exception as e:
        print(f"Error en la conversión: {e}")
        return None 
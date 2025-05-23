from datetime import datetime

# Simulación de almacenamiento en memoria (puedes reemplazarlo con una base de datos)
SOLICITUDES_CONTACTO = []

def enviar_contacto(data_contacto):
    """
    Guarda una solicitud de contacto en memoria (o en una base de datos).
    Solo requiere el mensaje del cliente.
    """
    try:
        solicitud = {
            "id": len(SOLICITUDES_CONTACTO) + 1,
            "mensaje": data_contacto["mensaje"],
            "fecha": datetime.now().isoformat()
        }
        SOLICITUDES_CONTACTO.append(solicitud)
        return solicitud
    except Exception as e:
        print("Error al guardar la solicitud de contacto:", e)
        return None

def obtener_solicitudes_contacto():
    """
    Devuelve todas las solicitudes de contacto almacenadas.
    """
    return SOLICITUDES_CONTACTO
from fastapi import APIRouter, HTTPException
from modelos.producto import obtener_producto_por_id
from utilidades.conversor_moneda import convertir_clp_a_usd
from utilidades.auth import autenticar_usuario
import stripe
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configurar Stripe con la clave secreta
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
if not STRIPE_SECRET_KEY:
    raise ValueError("La clave secreta de Stripe no está configurada en las variables de entorno")
stripe.api_key = STRIPE_SECRET_KEY

router = APIRouter(
    tags=["pedidoYPago"]
)

@router.post("/hacerPedidoYPagar", response_model=dict)
async def hacer_pedido_y_pagar(producto_id: str, username: str, password: str):
    """
    Crea una sesión de pago en Stripe para un producto específico usando el precio en USD.
    Requiere autenticación de cliente.
    """
    # Verificar credenciales
    usuario = autenticar_usuario(username, password)
    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    if usuario["role"] != "client":
        raise HTTPException(status_code=403, detail="Solo los clientes pueden realizar pagos")

    try:
        # Obtener el producto de nuestra base de datos
        producto = obtener_producto_por_id(producto_id)
        if producto is None:
            raise HTTPException(status_code=404, detail=f"No se encontró el producto con ID {producto_id}")

        # Convertir el precio a USD
        precio_usd = convertir_clp_a_usd(producto["precio"])
        if precio_usd is None:
            raise HTTPException(status_code=500, detail="Error al convertir el precio a USD")

        # Crear un producto en Stripe
        stripe_product = stripe.Product.create(
            name=producto["nombre"],
            description=f"Compra de {producto['nombre']}"
        )

        # Crear un precio en Stripe (convertir el precio USD a centavos)
        precio_en_centavos = int(float(precio_usd) * 100)
        stripe_price = stripe.Price.create(
            unit_amount=precio_en_centavos,
            currency="usd",
            product=stripe_product.id,
        )

        # Crear la sesión de pago
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': stripe_price.id,
                'quantity': 1,
            }],
            mode='payment',
            success_url="https://api.ferremas.cl/pagos/success",  # URL de éxito del API
            cancel_url="https://api.ferremas.cl/pagos/cancel",    # URL de cancelación del API
        )

        return {
            "id": session.id,
            "url": session.url,
            "precio_usd": precio_usd
        }

    except stripe.error.StripeError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 
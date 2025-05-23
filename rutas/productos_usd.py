from fastapi import APIRouter, HTTPException
from modelos.producto import obtener_productos, obtener_producto_por_id
from utilidades.conversor_moneda import convertir_clp_a_usd

router = APIRouter(
    tags=["productosFerremasUsd"]
)

@router.get("/productos-usd", response_model=list)
async def ruta_obtener_productos_usd():
    """
    Endpoint para obtener la lista de productos con precios en USD.
    """
    productos = obtener_productos()
    if productos is None:
        raise HTTPException(status_code=500, detail="No se pudieron obtener los productos")
    
    # Convertir los precios a USD
    for producto in productos:
        precio_usd = convertir_clp_a_usd(producto["precio"])
        if precio_usd is not None:
            producto["precio_usd"] = precio_usd
    
    return productos

@router.get("/productos-usd/{producto_id}", response_model=dict)
async def ruta_obtener_producto_usd(producto_id: str):
    """
    Endpoint para obtener un producto específico con precio en USD.
    """
    producto = obtener_producto_por_id(producto_id)
    if producto is None:
        raise HTTPException(status_code=404, detail=f"No se encontró el producto con ID {producto_id}")
    
    # Convertir el precio a USD
    precio_usd = convertir_clp_a_usd(producto["precio"])
    if precio_usd is not None:
        producto["precio_usd"] = precio_usd
    
    return producto 
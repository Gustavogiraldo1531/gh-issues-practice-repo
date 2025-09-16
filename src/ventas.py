from typing import List, Dict, Tuple

def calcular_factura(items: List[Dict], iva: float = 0.19, descuento: float = 0.0, incluye_iva_en_precios: bool = False) -> Tuple[float, float, float]:
    """
    Calcula subtotal, iva y total.
    items: lista de dicts con keys: nombre, precio, cantidad
    iva: 0.19 = 19%
    descuento: 0.10 = 10%
    incluye_iva_en_precios: si True, los precios ya incluyen IVA
    """
    subtotal = 0.0
    for it in items:
        precio = float(it.get("precio", 0))
        cantidad = int(it.get("cantidad", 0))
        subtotal += precio * cantidad

    if incluye_iva_en_precios:
        base = subtotal
        iva_calc = base * (iva / (1 + iva))  # aproximacion
    else:
        base = subtotal
        iva_calc = base * iva

    total_bruto = base + iva_calc
    total_desc = total_bruto * (1 - descuento)
    return round(subtotal, 2), round(iva_calc, 2), round(total_desc, 2)

from typing import List, Dict, Tuple
from decimal import Decimal, ROUND_HALF_UP

def calcular_factura(items: List[Dict], iva: float = 0.19, descuento: float = 0.1, incluye_iva_en_precios: bool = False) -> Tuple[float, float, float]:
    """
    Calcula subtotal, iva y total.
    items: lista de dicts con keys: nombre, precio, cantidad
    iva: 0.19 = 19%
    descuento: 0.10 = 10%
    incluye_iva_en_precios: si True, los precios ya incluyen IVA
    """
    subtotal = Decimal("0.00")
    for it in items:
        precio = Decimal(str(it.get("precio", 0)))
        cantidad = int(it.get("cantidad", 0))
        #Validación de entradas
        if precio < 0:
            raise ValueError(f"Precio negativo no permitido: {precio}")
        if cantidad < 0:
            raise ValueError(f"Cantidad negativa no permitida: {cantidad}")
        subtotal += precio * cantidad

    iva = Decimal(str(iva))
    descuento = Decimal(str(descuento))

    if incluye_iva_en_precios:
        base = (subtotal / (Decimal("1.0") + iva)) * (Decimal("1.0") - descuento)  # quitar descuento antes de calcular IVA
        iva_calc = base * iva  # calculo correcto de iva si precio incluye iva
        valor_descuento = base * descuento
    else:
        base = subtotal * (Decimal("1.0") - descuento) # quitar descuento antes de calcular IVA
        iva_calc = base * iva
        valor_descuento = base * descuento # se agrega valor del descuento

    total_bruto = base + iva_calc

    # --- Redondeo contable (2 decimales, hacia arriba al 0.5) ---
    def r(x: Decimal) -> Decimal:
        return x.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    return r(subtotal), r(iva_calc), r(valor_descuento)

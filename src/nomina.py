from typing import Dict
from decimal import Decimal, ROUND_HALF_UP

TWO = Decimal('0.01')
def _to_dec(x) -> Decimal:
    return Decimal(str(x))

def calcular_nomina(basico_mensual: float, 
                    horas_mes: int, 
                    horas_extra: int, 
                    horas_noche: int = 0) -> Dict[str, float]:
    """
    Calcula la nomina basica con horas extras y recargos nocturnos.
    - basico_mensual >= 0.
    - horas_mes > 0 (valor por defecto 240 si es 0 o negativo).  
    - horas_extra >= 0.
    - horas_noche >= 0.
    Retorna un diccionario con: basico, extras, recargos, total. 
    """ 
    if basico_mensual < 0:
        raise ValueError("El basico mensual debe ser mayor o igual a 0.")
    if horas_mes <= 0:
        raise ValueError("Las horas del mes deben ser mayores a 0.")
    if horas_extra < 0 or horas_noche < 0:
        raise ValueError("Las horas extras y nocturnas deben ser mayores o iguales a 0.")
    B = _to_dec(basico_mensual)
    HM = _to_dec(horas_mes)
    HE = _to_dec(horas_extra)
    HN = _to_dec(horas_noche)

    valor_hora = (B / HM)
    extras = (valor_hora * HE * Decimal('1.5'))
    recargos = (valor_hora * HN * Decimal('0.35'))
    total = B + extras + recargos

    return {
        'basico': float(B.quantize(TWO, rounding=ROUND_HALF_UP)),
        'extras': float(extras.quantize(TWO, rounding=ROUND_HALF_UP)),
        'recargos': float(recargos.quantize(TWO, rounding=ROUND_HALF_UP)),
        'total': float(total.quantize(TWO, rounding=ROUND_HALF_UP))}
from typing import Dict

def calcular_nomina(basico_mensual: float, horas_mes: int, horas_extra: int, recargo_noche: bool = False) -> Dict[str, float]:
    """
    basico_mensual: salario base del mes
    horas_mes: horas ordinarias del mes (ej. 240)
    horas_extra: cantidad de horas extra
    recargo_noche: aplica recargo nocturno simple
    Retorna dict con 'basico', 'extras', 'recargos', 'total'
    """
    if horas_mes <= 0:
        horas_mes = 240  # valor por defecto
    valor_hora = basico_mensual / horas_mes
    extras = horas_extra * valor_hora * 1.5
    recargos = valor_hora * 0.35 if recargo_noche else 0.0
    total = basico_mensual + extras + recargos
    return {
        "basico": round(basico_mensual, 2),
        "extras": round(extras, 2),
        "recargos": round(recargos, 2),
        "total": round(total, 2),
    }

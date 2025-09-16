from datetime import datetime
from typing import List, Dict

def clasificar_antiguedad(facturas: List[Dict], hoy: str) -> Dict[str, float]:
    """
    facturas: lista de dicts con keys: fecha (YYYY-MM-DD), saldo
    hoy: fecha de referencia (YYYY-MM-DD)
    Retorna un dict con buckets: '0-30', '31-60', '61-90', '90+'
    """
    ref = datetime.strptime(hoy, "%Y-%m-%d").date()
    buckets = {"0-30": 0.0, "31-60": 0.0, "61-90": 0.0, "90+": 0.0}
    for f in facturas:
        fecha = datetime.strptime(f["fecha"], "%Y-%m-%d").date()
        dias = (ref - fecha).days
        saldo = float(f.get("saldo", 0))
        if dias <= 30:
            buckets["0-30"] += saldo
        elif dias <= 60:
            buckets["31-60"] += saldo
        elif dias <= 90:
            buckets["61-90"] += saldo
        else:
            buckets["90+"] += saldo
    return {k: round(v, 2) for k, v in buckets.items()}

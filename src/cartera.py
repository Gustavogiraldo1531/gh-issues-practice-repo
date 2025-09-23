from datetime import datetime
from typing import List, Dict
from decimal import Decimal, ROUND_HALF_UP

TWO = Decimal('0.01')
def _to_dec(x) -> Decimal:
    return Decimal(str(x))

def clasificar_antiguedad(
    facturas: List[Dict],
    hoy : str,
    tratar_futuras_como_cero: bool = True
    ) -> Dict[str, float]:
    """
    Clasifica saldos en buckets: "0-30", "31-60", "61-90", "91+".
    Si una fecha es futura y tratar_futuras_como_cero es True, se clasifica en 0 dias
    (quedará en 0-30). Si es False, se lanza ValueError.
    """
    try:
        ref = datetime.strptime(hoy, "%Y-%m-%d").date()
    except Exception:
        raise ValueError("La fecha 'hoy' debe tener formato YYYY-MM-DD.")
    buckets = {"0-30": Decimal('0.00'), "31-60": Decimal('0.00'), 
               "61-90": Decimal('0.00'), "91+": Decimal('0.00'),}
    
    for f in facturas:
        try:
            fecha = datetime.strptime(f['fecha'], "%Y-%m-%d").date()
        except Exception:
            raise ValueError(f"Formato de fecha invalido en factura: {f.get('fecha')}")
        try:
            saldo = _to_dec(f.get("saldo",0))
        except Exception:
            raise ValueError("Saldo ivalido (no numerico)")
        
        if saldo < 0:
            raise ValueError("Saldo no puede ser negativo.")
        
        dias = (ref - fecha).days
        if dias < 0:
            if tratar_futuras_como_cero:
                dias = 0
            else:
                raise ValueError("Fecha de factura no puede ser futura.")
        if dias <= 30:
            buckets["0-30"] += saldo
        elif dias <= 60:
            buckets["31-60"] += saldo
        elif dias <= 90:
            buckets["61-90"] += saldo
        else:
            buckets["91+"] += saldo
        


from decimal import Decimal, ROUND_HALF_UP

TWO = Decimal('0.01')

def _to_dec(x) -> Decimal:
    return Decimal(str(x))

def formatear_cop(valor) -> str:
    """Formatea un valor numérico a una cadena con formato de moneda COP.
    Soporta valores negativos."""
    try:
        n = _to_dec(valor).quantize(TWO, rounding=ROUND_HALF_UP)
    except Exception:
        n = Decimal('0.00')
    
    signo = '-' if n < 0 else ''
    n = abs(n)
    entero = int(n)
    dec = int((n - entero) * 100)

    #Miles punto
    entero_str = f"{entero:,}".replace(",", ".")
    dec_str = f"{dec:02d}"

    return f"{signo}${entero_str},{dec_str}"
#Ejemplo de uso: 12345678.9 -> $1.234.567,90

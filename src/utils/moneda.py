def formatear_cop(valor: float) -> str:
    """
    Devuelve un string con formato COP simple, sin localizacion avanzada.
    Ej: 1234567.8 -> "$ 1,234,567.80"
    """
    try:
        n = float(valor)
    except Exception:
        n = 0.0
    entero = int(n)
    dec = abs(n - entero)
    return "$ " + f"{entero:,}" + f"{dec:.2f}"[1:]

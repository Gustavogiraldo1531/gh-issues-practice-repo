import pandas as pd
from pathlib import Path
from .ventas import calcular_factura
from .cartera import clasificar_antiguedad
from .nomina import calcular_nomina
from .utils.moneda import formatear_cop

BASE = Path(__file__).resolve().parent.parent
DATA = BASE / "data"

def demo_ventas():
    df = pd.read_csv(DATA / "items.csv")
    items = df.to_dict(orient="records")
    subtotal, iva, total = calcular_factura(items, iva=0.19, descuento=0.05, incluye_iva_en_precios=False)
    print("=== VENTAS ===")
    print("Subtotal:", formatear_cop(subtotal))
    print("IVA:", formatear_cop(iva))
    print("Total:", formatear_cop(total))

def demo_cartera():
    df = pd.read_csv(DATA / "cartera.csv")
    facturas = df.to_dict(orient="records")
    buckets = clasificar_antiguedad(facturas, hoy="2025-09-01")
    print("\n=== CARTERA ===")
    for k, v in buckets.items():
        print(k, ":", formatear_cop(v))

def demo_nomina():
    print("\n=== NOMINA ===")
    resultado = calcular_nomina(basico_mensual=1300000, horas_mes=240, horas_extra=10, recargo_noche=True)
    for k, v in resultado.items():
        if k != "basico":
            print(k, ":", formatear_cop(v))
        else:
            print(k, ":", formatear_cop(v))

if __name__ == "__main__":
    demo_ventas()
    demo_cartera()
    demo_nomina()

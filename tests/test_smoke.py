from src.ventas import calcular_factura
from src.cartera import clasificar_antiguedad
from src.nomina import calcular_nomina

def test_smoke_ventas():
    items = [{"nombre":"A","precio":1000,"cantidad":2}]
    s, i, t = calcular_factura(items, iva=0.19, descuento=0.0, incluye_iva_en_precios=False)
    assert s == 2000 and i >= 0 and t >= s

def test_smoke_cartera():
    facturas = [{"fecha":"2025-08-01","saldo":1000.0},{"fecha":"2025-06-01","saldo":2000.0}]
    buckets = clasificar_antiguedad(facturas, hoy="2025-09-01")
    assert set(buckets.keys()) == {"0-30","31-60","61-90","90+"}

def test_smoke_nomina():
    r = calcular_nomina(1000000, 240, 5, recargo_noche=False)
    assert r["total"] >= r["basico"]

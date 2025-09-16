# Sistema Mini-ERP (Practica de Issues, PRs y mejoras)

Este repositorio esta pensado para que tres estudiantes practiquen **creacion de Issues**, **organizacion del trabajo** y **Pull Requests**.
Contiene un conjunto minimo de modulos (ventas, cartera, nomina y utilidades) y datos de ejemplo.

## Objetivo de la practica
- Ejecutar el proyecto y **explorar comportamientos**.
- Reportar **Issues** claros (bug, enhancement, documentation o tests).
- Proponer y aplicar **mejoras** con Pull Requests.
- Vincular PRs a Issues con "Closes #N".
- Usar un **Project (Kanban)** para organizar el trabajo.

## Reglas
- No se indicaran los errores de forma explicita. El equipo debe **descubrirlos** revisando el codigo, ejecutando escenarios y leyendo resultados.
- Cada estudiante debe abrir **al menos 2 Issues** y **1 Pull Request**.
- Deben existir **al menos 3 PRs** integrados en total.
- No merges directos a `main`; trabajar con ramas por cambio (ej. `fix/...`, `feat/...`, `docs/...`, `test/...`).

## Como ejecutar
```
pip install -r requirements.txt
python -m src.main
```

## Sugerencias de exploracion (sin spoilers)
- Revisar resultados al cambiar parametros de entrada.
- Validar limites (valores cero, negativos, montos grandes, tasas y porcentajes).
- Observar formatos de salida y consistencia entre modulos.
- Comprobar que los reportes clasifiquen correctamente los datos.

## Lineamientos para Issues
- Titulo breve y claro.
- Descripcion con contexto, pasos para reproducir (si aplica) y comportamiento esperado.
- Usar etiquetas: `bug`, `enhancement`, `documentation`, `tests`.
- Asignar responsable y vincular al tablero de Project.

## Lineamientos para PRs
- Rama por cambio.
- Mensajes de commit claros.
- Descripcion del PR con referencia al Issue: `Closes #N`.
- Agregar o actualizar pruebas cuando corresponda.
- Mantener el codigo simple y consistente.

## Estructura
- `src/ventas.py`: logica de facturacion de ventas.
- `src/cartera.py`: reporte de antiguedad de saldos.
- `src/nomina.py`: calculo de nomina basica.
- `src/utils/moneda.py`: utilidades de formato de moneda.
- `src/main.py`: script de demostracion.
- `data/`: csvs de ejemplo.
- `tests/`: pruebas basicas de referencia.

## Entregables sugeridos
- 6+ Issues (mezcla de bug/enhancement/docs/tests).
- 3+ PRs integrados, cada uno cerrando un Issue.
- Captura del tablero Kanban con las tarjetas movidas de "To do" a "Done".

Buena practica: traten el repositorio como un proyecto real.

name: Bug report
description: Reporta un error o comportamiento inesperado
title: "[BUG] "
labels: ["bug"]
body:
  - type: textarea
    id: context
    attributes:
      label: Contexto
      description: Que estabas intentando hacer
  - type: textarea
    id: steps
    attributes:
      label: Pasos para reproducir
      placeholder: |
        1. ...
        2. ...
        3. ...
  - type: textarea
    id: expected
    attributes:
      label: Comportamiento esperado
  - type: textarea
    id: actual
    attributes:
      label: Comportamiento actual

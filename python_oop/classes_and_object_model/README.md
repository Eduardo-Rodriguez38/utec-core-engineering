# Clases y modelo de objetos en Python

Proyecto de introducción a la Programación Orientada a Objetos (POO) en Python.

## Objetivos

- Entender la diferencia entre una clase y una instancia
- Definir clases y crear objetos
- Inicializar atributos con `__init__`
- Implementar métodos de instancia
- Aplicar encapsulamiento y validar datos
- Representar objetos con `__str__` y `__repr__`

## Archivos

| Archivo | Descripción |
|---------|-------------|
| `0-square.py` | Define una clase vacía `Square` que representa un cuadrado |
| `1-square.py` | Define `Square` con un atributo privado `size` asignado al crear el objeto |
| `2-square.py` | Agrega validación de `size`: debe ser entero (`TypeError`) y mayor o igual a 0 (`ValueError`) |
| `3-square.py` | Agrega el método `area()` que devuelve el área del cuadrado |
| `4-square.py` | Agrega getter y setter (`@property`) para `size`, con validación en el setter |

## Requisitos

- Ubuntu 20.04
- Python 3.8
- Estilo PEP8 (pycodestyle)

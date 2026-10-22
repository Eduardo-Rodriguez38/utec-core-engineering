# Manejo de excepciones en Python

Proyecto del curso UTEC sobre manejo de errores en tiempo de ejecución usando `try` / `except`, `else`, `finally` y `raise`.

## Tareas

- **0. safe_print_list.py**: imprime hasta `x` elementos de una lista y devuelve cuántos imprimió. Usa `except IndexError` para no fallar cuando `x` es mayor que la lista.
- **1. safe_print_integer.py**: imprime un entero con `"{:d}".format()` y devuelve `True`; si no es entero, captura `ValueError` o `TypeError` y devuelve `False`.
- **2. safe_print_list_integers.py**: imprime solo los enteros de los primeros `x` elementos; omite los que no son enteros capturando `ValueError` y `TypeError`. No captura `IndexError` a propósito.
- **3. safe_print_division.py**: divide `a / b` dentro de un `try`; si hay `ZeroDivisionError` o `TypeError` el resultado es `None`. Usa `finally` para imprimir siempre el resultado.
- **4. raise_exception.py**: lanza un `TypeError` de forma explícita usando `raise`.
- **5. raise_exception_msg.py**: lanza un `NameError` con un mensaje personalizado usando `raise NameError(message)`.

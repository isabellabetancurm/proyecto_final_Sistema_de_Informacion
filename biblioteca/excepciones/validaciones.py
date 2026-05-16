"""
Módulo de validaciones para el sistema de la biblioteca.
"""

#función para validar que el campo no esté vacío
def validar_entrada(mensaje):
    """Valida que la cadena de texto no esté vacía."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("-> Error: Este campo es obligatorio.")

#función para validar que el año sea válido
def validar_año(mensaje):
    """Valida que el año sea un entero dentro de un rango válido."""
    while True:
        try:
            año = int(input(mensaje))
            if 1800 <= año <= 2026:
                return año
            print("-> Error: Ingrese un año válido (1800-2026).")
        except ValueError:
            print("-> Error: Debe ser un número entero.")

#función para validar que la edad sea válida
def validar_edad(mensaje):
    """Valida que la edad sea un número entero positivo."""
    while True:
        try:
            edad = int(input(mensaje))
            if 1 <= edad <= 120:
                return edad
            print("-> Error: Ingrese una edad válida (1-120).")
        except ValueError:
            print("-> Error: Debe ser un número entero.")

#función para validar que el salario sea válido
def validar_salario(mensaje):
    """Valida que el salario sea un número mayor a cero."""
    while True:
        try:
            salario = float(input(mensaje))
            if salario > 0:
                return salario
            print("-> Error: El salario debe ser mayor a 0.")
        except ValueError:
            print("-> Error: Debe ser un número.")

#función para validar el número de edición
def validar_numero(mensaje):
    """Valida que el valor ingresado sea un número entero positivo."""
    while True:
        try:
            numero = int(input(mensaje))
            if numero > 0:
                return numero
            print("-> Error: Debe ser un número mayor a 0.")
        except ValueError:
            print("-> Error: Debe ser un número entero.")
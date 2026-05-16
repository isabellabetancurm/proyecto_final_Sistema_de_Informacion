"""
Módulo de excepciones personalizadas para el sistema de la biblioteca.
"""

#excepción cuando un libro no está disponible para préstamo
class LibroNoDisponibleError(Exception):
    def __init__(self, mensaje="El libro no esta disponible para prestamo."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

#excepción cuando un libro no se encuentra en el catálogo
class LibroNoEncontradoError(Exception):
    def __init__(self, mensaje="El libro no se encuentra en el catalogo."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

#excepción cuando un usuario no está registrado en el sistema
class UsuarioNoEncontradoError(Exception):
    def __init__(self, mensaje="El usuario no se encuentra registrado en el sistema."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

#excepción cuando un usuario ya está registrado en el sistema
class UsuarioYaExisteError(Exception):
    def __init__(self, mensaje="El usuario ya esta registrado en el sistema."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

#excepción cuando un usuario supera el límite de libros prestados
class PrestamoMaximoError(Exception):
    def __init__(self, mensaje="El usuario ha alcanzado el limite maximo de libros prestados."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

#excepción cuando el salario ingresado no es válido
class SalarioInvalidoError(Exception):
    def __init__(self, mensaje="El salario debe ser un valor mayor a 0."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

#excepción cuando un empleado no se encuentra en el sistema
class EmpleadoNoEncontradoError(Exception):
    def __init__(self, mensaje="El empleado no se encuentra registrado en el sistema."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
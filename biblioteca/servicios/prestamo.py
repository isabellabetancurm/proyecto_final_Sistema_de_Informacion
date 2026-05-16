#composición: Préstamo une a un usuario con un libro y registra quien tiene prestado que libro y en que fecha
class Préstamo:

    #método constructor: se ejecuta automáticamente al crear un objeto y obliga a que el prestamo siempre tenga usuario, libro y fecha desde el principio
    def __init__(self, usuario, libro, fecha_prestamo: str):

        #encapsulamiento: atributos privados
        self.__usuario          = usuario
        self.__libro            = libro
        self.__fecha_prestamo   = fecha_prestamo
        self.__fecha_devolucion = None    #None (vacío) hasta que el libro sea devuelto

    #getters: métodos para obtener el valor de los atributos privados
    def get_usuario(self):
        return self.__usuario

    def get_libro(self):
        return self.__libro

    def get_fecha_prestamo(self) -> str:
        return self.__fecha_prestamo

    def get_fecha_devolucion(self):
        return self.__fecha_devolucion

    #métodos: acciones que puede realizar el préstamo
    def registrar_devolucion(self, fecha_devolucion: str):
        #registramos la fecha de devolucion y cerramos el prestamo
        self.__fecha_devolucion = fecha_devolucion
        self.__libro.devolver()
        print(f'Préstamo cerrado. Libro devuelto el {fecha_devolucion}.')

    def mostrar_info(self):
        #si la fecha de devolución está vacío, el préstamo está activo
        estado = "Activo" if self.__fecha_devolucion is None else "Cerrado"
        print(f'Prestamo        : {self.__libro.get_titulo()}')
        print(f'Usuario         : {self.__usuario.get_nombre()}')
        print(f'Fecha prestamo  : {self.__fecha_prestamo}')
        print(f'Fecha devolucion: {self.__fecha_devolucion if self.__fecha_devolucion else "Pendiente"}')
        print(f'Estado          : {estado}')
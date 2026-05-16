#clase
class Usuario:

    #método constructor: se ejecuta automáticamente al crear un objeto
    def __init__(self, nombre: str, cedula: str, edad: int, telefono: str, direccion: str):

        #encapsulamiento: atributos privados
        self.__nombre           = nombre
        self.__cedula           = cedula
        self.__edad             = edad
        self.__telefono         = telefono
        self.__direccion        = direccion
        self.__libros_prestados = []    #lista vacia, el usuario no tiene libros al inicio

    #getters: métodos para obtener el valor de los atributos privados
    def get_nombre(self) -> str:
        return self.__nombre

    def get_cedula(self) -> str:
        return self.__cedula

    def get_edad(self) -> int:
        return self.__edad

    def get_telefono(self) -> str:
        return self.__telefono

    def get_direccion(self) -> str:
        return self.__direccion

    def get_libros_prestados(self) -> list:
        return self.__libros_prestados

    #setters: métodos para modificar el valor de los atributos privados
    def set_telefono(self, telefono: str):
        self.__telefono = telefono

    def set_direccion(self, direccion: str):
        self.__direccion = direccion

    #métodos: acciones que puede realizar el usuario
    def agregar_libro_prestado(self, libro):
        self.__libros_prestados.append(libro)

    def quitar_libro_prestado(self, libro):
        self.__libros_prestados.remove(libro)

    def mostrar_info(self):
        print(f'Usuario  : {self.__nombre}')
        print(f'Cedula   : {self.__cedula}')
        print(f'Edad     : {self.__edad} anos')
        print(f'Telefono : {self.__telefono}')
        print(f'Direccion: {self.__direccion}')
        print(f'Libros prestados: {len(self.__libros_prestados)}')
        #si tiene libros prestados, los muestra uno por uno
        if(len(self.__libros_prestados) > 0):
            for libro in self.__libros_prestados:
                print(f'  - {libro.get_titulo()}')
#clase madre: define los atributos y métodos base para todos los tipos de libros
class Libro:

    #método constructor: se ejecuta automáticamente al crear un objeto y obliga a que el libro siempre tenga todos sus datos desde el principio.
    def __init__(self, titulo: str, autor: str, año: int):

        #encapsulamiento: atributos privados, o sea, que no se pueden modificar desde afuera
        self.__titulo     = titulo
        self.__autor      = autor
        self.__año        = año
        self.__disponible = True    #por defecto el libro está disponible

    #getters: métodos para obtener el valor de los atributos privados
    def get_titulo(self) -> str:
        return self.__titulo

    def get_autor(self) -> str:
        return self.__autor

    def get_año(self) -> int:
        return self.__año

    def get_disponible(self) -> bool:
        return self.__disponible

    #setters: métodos para modificar el valor de los atributos privados
    def set_titulo(self, titulo: str):
        self.__titulo = titulo

    def set_autor(self, autor: str):
        self.__autor = autor

    def set_disponible(self, disponible: bool):
        self.__disponible = disponible

    #métodos: acciones que puede realizar el libro
    def prestar(self):
        if(self.__disponible):
            self.__disponible = False
            print(f' El Libro "{self.__titulo}" ha sido prestado exitosamente.')
        else:
            print(f' El Libro "{self.__titulo}" no está disponible en este momento.')

    def devolver(self):
        self.__disponible = True
        print(f' El Libro "{self.__titulo}" devuelto. Ya está disponible.')

    #este método sera sobreescrito por cada clase hija (polimorfismo)
    def mostrar_info(self):
        estado = "Disponible" if self.__disponible else "Prestado"
        print(f'  Título: {self.__titulo} — {self.__autor} ({self.__año}) | {estado}')   
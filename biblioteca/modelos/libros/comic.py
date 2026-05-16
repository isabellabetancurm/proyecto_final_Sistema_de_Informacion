from modelos.libros.libro import Libro

#herencia: Cómic hereda todos los atributos y métodos de Libro
#Cómic es la clase hija, Libro es la clase madre
class Comic(Libro):

    #método constructor
    def __init__(self, titulo: str, autor: str, año: int, editorial: str, numero_edicion: int):

        #llamamos al constructor de la clase madre (Libro)
        super().__init__(titulo, autor, año)

        #atributos propios de los cómics
        self.__editorial      = editorial
        self.__numero_edicion = numero_edicion

    #getters
    def get_editorial(self) -> str:
        return self.__editorial

    def get_numero_edicion(self) -> int:
        return self.__numero_edicion

    #polimorfismo: sobreescribimos mostrar_info de la clase madre
    def mostrar_info(self):
        super().mostrar_info()
        print(f'  Categoria: Cómic | Editorial: {self.__editorial} | Edicion: {self.__numero_edicion}')
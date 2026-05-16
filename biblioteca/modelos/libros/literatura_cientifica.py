from modelos.libros.libro import Libro

#herencia: literatura_cientifica hereda todos los atributos y métodos de Libro
#literatura_cientifica es la clase hija, Libro es la clase madre
class literatura_cientifica(Libro):

    #método constructor
    def __init__(self, titulo: str, autor: str, año: int, area_ciencia: str, nivel: str):

        #llamamos al constructor de la clase madre (Libro)
        super().__init__(titulo, autor, año)

        #atributos propios de la literatura cientifica
        self.__area_ciencia = area_ciencia
        self.__nivel        = nivel        #basico, intermedio, avanzado

    #getters
    def get_area_ciencia(self) -> str:
        return self.__area_ciencia

    def get_nivel(self) -> str:
        return self.__nivel

    #polimorfismo: sobreescribimos mostrar_info de la clase madre, el mismo método muestra información diferente según el tipo de libro
    def mostrar_info(self):
        super().mostrar_info()
        print(f'  Categoria: Literatura Cientifica | Area: {self.__area_ciencia} | Nivel: {self.__nivel}')

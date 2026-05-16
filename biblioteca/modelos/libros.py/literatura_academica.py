from libro import Libro

#herencia: literatura_academica hereda todos los atributos y métodos de Libro
#literatura_academica es la clase hija, Libro es la clase madre
class literatura_academica(Libro):

    #método constructor
    def __init__(self, titulo: str, autor: str, año: int, materia: str, nivel_educativo: str):

        #llamamos al constructor de la clase madre (Libro)
        super().__init__(titulo, autor, año)

        #atributos propios de la literatura academica
        self.__materia        = materia
        self.__nivel_educativo = nivel_educativo    #bachillerato, universidad, posgrado

    #getters
    def get_materia(self) -> str:
        return self.__materia

    def get_nivel_educativo(self) -> str:
        return self.__nivel_educativo

    #polimorfismo: sobreescribimos mostrar_info de la clase madre
    def mostrar_info(self):
        super().mostrar_info()
        print(f'  Categoria: Literatura Academica | Materia: {self.__materia} | Nivel educativo: {self.__nivel_educativo}')
from libro import Libro

#herencia: Bibliografia_artistica hereda todos los atributos y métodos de Libro
#Bibliografia_artistica es la clase hija, Libro es la clase madre
class Bibliografia_artistica(Libro):

    #método constructor
    def __init__(self, titulo: str, autor: str, año: int, tipo_arte: str, tecnica: str):

        #llamamos al constructor de la clase madre (Libro)
        super().__init__(titulo, autor, año)

        #atributos propios de la bibliografia artistica
        self.__tipo_arte = tipo_arte    #pintura, fotografia, escultura, arquitectura
        self.__tecnica   = tecnica      #acuarela, oleo, digital, etc

    #getters
    def get_tipo_arte(self) -> str:
        return self.__tipo_arte

    def get_tecnica(self) -> str:
        return self.__tecnica

    #polimorfismo: sobreescribimos mostrar_info de la clase madre
    def mostrar_info(self):
        super().mostrar_info()
        print(f'  Categoria: Bibliografia Artistica | Tipo de arte: {self.__tipo_arte} | Tecnica: {self.__tecnica}')
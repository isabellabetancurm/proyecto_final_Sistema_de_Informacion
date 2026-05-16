from modelos.libros.libro import Libro

#herencia: Poesía hereda todos los atributos y métodos de Libro
#Poesía es la clase hija, Libro es la clase madre
class Poesia(Libro):

    #método constructor
    def __init__(self, titulo: str, autor: str, año: int, estilo: str, num_poemas: int):

        #llamamos al constructor de la clase madre (Libro)
        super().__init__(titulo, autor, año)

        #atributos propios de la poesía
        self.__estilo     = estilo        #clasica, contemporanea, romantica
        self.__num_poemas = num_poemas

    #getters
    def get_estilo(self) -> str:
        return self.__estilo

    def get_num_poemas(self) -> int:
        return self.__num_poemas

    #polimorfismo: sobreescribimos mostrar_info de la clase madre
    def mostrar_info(self):
        super().mostrar_info()
        print(f'  Categoria: Poesía | Estilo: {self.__estilo} | Numero de poemas: {self.__num_poemas}')
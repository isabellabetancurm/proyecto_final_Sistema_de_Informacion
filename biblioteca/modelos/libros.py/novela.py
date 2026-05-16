from libro import Libro

#herencia: novela hereda todos los atributos y métodos de Libro
#novela es la clase hija, Libro es la clase madre
class Novela (Libro):

    #método constructor
    def __init__(self, titulo: str, autor: str, año: int, subgenero: str, num_paginas: int):

        #llamamos al constructor de la clase madre (Libro)
        super().__init__(titulo, autor, año)

        #atributos propios de la novela
        self.__subgenero   = subgenero      #thriller, drama, historica, aventura
        self.__num_paginas = num_paginas

    #getters
    def get_subgenero(self) -> str:
        return self.__subgenero

    def get_num_paginas(self) -> int:
        return self.__num_paginas

    #polimorfismo: sobreescribimos mostrar_info de la clase madre
    def mostrar_info(self):
        super().mostrar_info()
        print(f'  Categoria: Novela | Subgenero: {self.__subgenero} | Paginas: {self.__num_paginas}')
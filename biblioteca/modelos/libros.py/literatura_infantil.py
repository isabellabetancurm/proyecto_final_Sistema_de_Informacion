from libro import Libro

#herencia: literatura_infantil hereda todos los atributos y métodos de Libro
#literatura_infantil es la clase hija, Libro es la clase madre
class literatura_infantil(Libro):

    #método constructor
    def __init__(self, titulo: str, autor: str, año: int, edad_recomendada: int, ilustrado: bool):

        #llamamos al constructor de la clase madre (Libro)
        super().__init__(titulo, autor, año)

        #atributos propios de la literatura infantil
        self.__edad_recomendada = edad_recomendada    #edad en años
        self.__ilustrado        = ilustrado            #True o False

    #getters
    def get_edad_recomendada(self) -> int:
        return self.__edad_recomendada

    def get_ilustrado(self) -> bool:
        return self.__ilustrado

    #polimorfismo: sobreescribimos mostrar_info de la clase madre
    def mostrar_info(self):
        super().mostrar_info()
        ilustrado = "Si" if self.__ilustrado else "No"
        print(f'  Categoria: Literatura Infantil | Edad recomendada: {self.__edad_recomendada} años | Ilustrado: {ilustrado}')
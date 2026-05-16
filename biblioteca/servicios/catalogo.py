#composición: Catálogo contiene una lista de libros
#el catálogo es el corazón de la biblioteca
class Catalogo:

    #método constructor
    def __init__(self):
        #lista vacia de libros al inicio
        self.__libros = []

    #métodos: acciones que puede realizar el catálogo
    def agregar_libro(self, libro: Libro):
        self.__libros.append(libro)
        print(f'Libro "{libro.get_titulo()}" agregado al catálogo.')

    def eliminar_libro(self, titulo: str):
        for libro in self.__libros:
            if(libro.get_titulo().lower() == titulo.lower()):
                self.__libros.remove(libro)
                print(f'Libro "{titulo}" eliminado del catálogo.')
                return
        print(f'El libro "{titulo}" no se encuentra en el catálogo.')

    def buscar_libro(self, titulo: str):
        for libro in self.__libros:
            if(libro.get_titulo().lower() == titulo.lower()):
                return libro
        return None

    def mostrar_catalogo(self):
        print(f'\n=== Catálogo de la Biblioteca — {len(self.__libros)} libros ===')
        if(len(self.__libros) > 0):
            for libro in self.__libros:
                libro.mostrar_info()
        else:
            print('El catálogo esta vacío.')

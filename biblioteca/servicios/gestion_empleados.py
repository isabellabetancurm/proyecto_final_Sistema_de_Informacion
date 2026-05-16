#composición: GestionEmpleados contiene una lista de empleados y se encarga de administrar el personal de la biblioteca
class GestionEmpleados:

    #método constructor
    def __init__(self):
        #lista vacía de empleados al inicio
        self.__empleados = []

    #métodos: acciones que puede realizar la gestion de empleados
    def agregar_empleado(self, empleado):
        #agregamos un empleado a la lista
        self.__empleados.append(empleado)
        print(f'Empleado "{empleado.get_nombre()}" agregado al sistema.')

    def eliminar_empleado(self, nombre: str):
        #buscamos el empleado por nombre y lo eliminamos
        for empleado in self.__empleados:
            if(empleado.get_nombre().lower() == nombre.lower()):
                self.__empleados.remove(empleado)
                print(f'Empleado "{nombre}" eliminado del sistema.')
                return
        print(f'El empleado "{nombre}" no se encuentra en el sistema.')

    def buscar_empleado(self, nombre: str):
        #buscamos un empleado por nombre y lo retornamos
        for empleado in self.__empleados:
            if(empleado.get_nombre().lower() == nombre.lower()):
                return empleado
        return None

    def mostrar_empleados(self):
        #mostramos todos los empleados registrados
        print(f'\n=== Personal de la Biblioteca — {len(self.__empleados)} empleados ===')
        if(len(self.__empleados) > 0):
            for empleado in self.__empleados:
                empleado.mostrar_info()
                print('---')
        else:
            print('No hay empleados registrados.')
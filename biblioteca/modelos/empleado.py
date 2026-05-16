#clase
class Empleado:

    #método constructor: se ejecuta automáticamente al crear un objeto
    #obliga a que el empleado siempre tenga todos sus datos desde el principio
    def __init__(self, nombre: str, cedula: str, telefono: str, salario: float):

        #encapsulamiento: atributos privados
        self.__nombre   = nombre
        self.__cedula   = cedula
        self.__telefono = telefono
        self.__salario  = salario

    #getters: métodos para obtener el valor de los atributos privados
    def get_nombre(self) -> str:
        return self.__nombre

    def get_cedula(self) -> str:
        return self.__cedula

    def get_telefono(self) -> str:
        return self.__telefono

    def get_salario(self) -> float:
        return self.__salario

    #setters: métodos para modificar el valor de los atributos privados
    def set_telefono(self, telefono: str):
        self.__telefono = telefono

    def set_salario(self, salario: float):
        if(salario > 0):
            self.__salario = salario
        else:
            print('El salario debe ser mayor a 0.')

    #métodos: acciones que puede realizar el empleado
    def mostrar_info(self):
        print(f'Empleado : {self.__nombre}')
        print(f'Cedula   : {self.__cedula}')
        print(f'Telefono : {self.__telefono}')
        print(f'Salario  : ${self.__salario:,.0f}')
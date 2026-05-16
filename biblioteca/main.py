#importamos todos los modelos
from modelos.libros.libro import Libro
from modelos.libros.literatura_cientifica import literatura_cientifica
from modelos.libros.literatura_academica import literatura_academica
from modelos.libros.literatura_infantil import literatura_infantil
from modelos.libros.novela import Novela
from modelos.libros.comic import Comic
from modelos.libros.poesia import Poesia
from modelos.libros.bibliografia_artistica import Bibliografia_artistica
from modelos.usuario import Usuario
from modelos.empleado import Empleado
from servicios.catalogo import Catalogo
from servicios.prestamo import Prestamo
from servicios.gestion_empleados import GestionEmpleados
from excepciones.excepciones import LibroNoDisponibleError, LibroNoEncontradoError, UsuarioNoEncontradoError
from excepciones.validaciones import validar_entrada, validar_año, validar_edad, validar_salario, validar_numero

# ═══════════════════════════════════════════════════════════
#  PARTE 1: DEMOSTRACIÓN DEL SISTEMA CON DATOS FIJOS
# ═══════════════════════════════════════════════════════════

print("\n========================================")
print("   SISTEMA DE INFORMACION - BIBLIOTECA  ")
print("========================================")

# ───────────────────────────────────────────
# instancia de objetos: creamos los libros
# ───────────────────────────────────────────
print("\n--- Instancia de objetos ---")

#herencia y polimorfismo: cada libro es de una categoria diferente
libro1 = literatura_cientifica("Cosmos", "Carl Sagan", 1980, "Astronomia", "Avanzado")
libro2 = literatura_academica("Calculo", "James Stewart", 2015, "Matematicas", "Universidad")
libro3 = literatura_infantil("El Principito", "Antoine de Saint-Exupery", 1943, 8, True)
libro4 = Novela("Cien Anos de Soledad", "Gabriel Garcia Marquez", 1967, "Drama", 471)
libro5 = Comic("Watchmen", "Alan Moore", 1987, "DC Comics", 1)
libro6 = Poesia("Veinte Poemas de Amor", "Pablo Neruda", 1924, "Romantica", 20)
libro7 = Bibliografia_artistica("El Arte del Renacimiento", "Giorgio Vasari", 1550, "Pintura", "Oleo")

#instancia de usuarios
usuario1 = Usuario("Maria Gonzalez", "1094567890", 22, "3001234567", "Calle 10 # 5-20")
usuario2 = Usuario("Carlos Perez",   "1023456789", 30, "3109876543", "Carrera 8 # 3-15")

#instancia de empleado
empleado1 = Empleado("Laura Martinez", "1056789012", "3207654321", 2_500_000)

# ───────────────────────────────────────────
# composición: el catalogo contiene libros
# ───────────────────────────────────────────
print("\n--- Composicion: catalogo de libros ---")
catalogo = Catalogo()
catalogo.agregar_libro(libro1)
catalogo.agregar_libro(libro2)
catalogo.agregar_libro(libro3)
catalogo.agregar_libro(libro4)
catalogo.agregar_libro(libro5)
catalogo.agregar_libro(libro6)
catalogo.agregar_libro(libro7)

# ───────────────────────────────────────────
# polimorfismo: mostrar_info() diferente en cada categoria
# ───────────────────────────────────────────
print("\n--- Polimorfismo: mostrar_info() en cada tipo de libro ---")
catalogo.mostrar_catalogo()

# ───────────────────────────────────────────
# composición: gestion de empleados
# ───────────────────────────────────────────
print("\n--- Composicion: gestion de empleados ---")
gestion = GestionEmpleados()
gestion.agregar_empleado(empleado1)
gestion.mostrar_empleados()

# ───────────────────────────────────────────
# composición: prestamo une usuario con libro
# ───────────────────────────────────────────
print("\n--- Composicion: registro de prestamo ---")
libro4.prestar()
usuario1.agregar_libro_prestado(libro4)
prestamo1 = Prestamo(usuario1, libro4, "16/05/2026")
prestamo1.mostrar_info()

# ───────────────────────────────────────────
# excepciones: manejo de errores del sistema
# ───────────────────────────────────────────
print("\n--- Excepciones: manejo de errores ---")
try:
    if(not libro4.get_disponible()):
        raise LibroNoDisponibleError(f'"{libro4.get_titulo()}" ya esta prestado.')
except LibroNoDisponibleError as e:
    print(f'-> Error capturado: {e.mensaje}')

try:
    libro_buscado = catalogo.buscar_libro("Harry Potter")
    if(libro_buscado is None):
        raise LibroNoEncontradoError('"Harry Potter" no esta en el catalogo.')
except LibroNoEncontradoError as e:
    print(f'-> Error capturado: {e.mensaje}')

# ═══════════════════════════════════════════════════════════
#  PARTE 2: MENU INTERACTIVO
# ═══════════════════════════════════════════════════════════

def mostrar_menu():
    print("\n╔══════════════════════════════════════╗")
    print("║      BIBLIOTECA MUNICIPAL            ║")
    print("║      Sistema de Informacion          ║")
    print("╠══════════════════════════════════════╣")
    print("║  1. Ver catalogo de libros           ║")
    print("║  2. Buscar libro                     ║")
    print("║  3. Registrar prestamo               ║")
    print("║  4. Registrar devolucion             ║")
    print("║  5. Registrar usuario                ║")
    print("║  6. Ver info de usuario              ║")
    print("║  7. Ver empleados                    ║")
    print("║  8. Salir                            ║")
    print("╚══════════════════════════════════════╝")
    print("Elige una opcion: ", end="")

#listas del sistema
prestamos = [prestamo1]
usuarios  = [usuario1, usuario2]

opcion = ""
while(opcion != "8"):

    mostrar_menu()
    opcion = input()

    if(opcion == "1"):
        #ver catalogo completo
        catalogo.mostrar_catalogo()

    elif(opcion == "2"):
        #buscar libro por titulo
        titulo = validar_entrada("Ingrese el titulo del libro a buscar: ")
        try:
            libro_encontrado = catalogo.buscar_libro(titulo)
            if(libro_encontrado is None):
                raise LibroNoEncontradoError(f'"{titulo}" no esta en el catalogo.')
            libro_encontrado.mostrar_info()
        except LibroNoEncontradoError as e:
            print(f'-> Error: {e.mensaje}')

    elif(opcion == "3"):
        #registrar prestamo
        catalogo.mostrar_catalogo()
        titulo = validar_entrada("Ingrese el titulo del libro a prestar: ")
        try:
            libro_prestar = catalogo.buscar_libro(titulo)
            if(libro_prestar is None):
                raise LibroNoEncontradoError(f'"{titulo}" no esta en el catalogo.')
            if(not libro_prestar.get_disponible()):
                raise LibroNoDisponibleError(f'"{titulo}" no esta disponible.')
            print("\nUsuarios registrados:")
            for i, u in enumerate(usuarios):
                print(f'  {i+1}. {u.get_nombre()}')
            idx   = int(input("Elige el numero del usuario: ")) - 1
            fecha = validar_entrada("Ingrese la fecha del prestamo (dd/mm/aaaa): ")
            nuevo_prestamo = Prestamo(usuarios[idx], libro_prestar, fecha)
            usuarios[idx].agregar_libro_prestado(libro_prestar)
            libro_prestar.prestar()
            prestamos.append(nuevo_prestamo)
        except LibroNoEncontradoError as e:
            print(f'-> Error: {e.mensaje}')
        except LibroNoDisponibleError as e:
            print(f'-> Error: {e.mensaje}')

    elif(opcion == "4"):
        #registrar devolucion
        titulo = validar_entrada("Ingrese el titulo del libro a devolver: ")
        fecha  = validar_entrada("Ingrese la fecha de devolucion (dd/mm/aaaa): ")
        for prestamo in prestamos:
            if(prestamo.get_libro().get_titulo().lower() == titulo.lower()):
                prestamo.registrar_devolucion(fecha)
                prestamo.get_usuario().quitar_libro_prestado(prestamo.get_libro())
                break

    elif(opcion == "5"):
        #registrar nuevo usuario
        print("\n── Registrar nuevo usuario ──")
        nombre    = validar_entrada("Nombre completo : ")
        cedula    = validar_entrada("Cedula          : ")
        edad      = validar_edad("Edad            : ")
        telefono  = validar_entrada("Telefono        : ")
        direccion = validar_entrada("Direccion       : ")
        nuevo_usuario = Usuario(nombre, cedula, edad, telefono, direccion)
        usuarios.append(nuevo_usuario)
        print(f'Usuario "{nombre}" registrado exitosamente.')

    elif(opcion == "6"):
        #ver info de usuario
        print("\nUsuarios registrados:")
        for i, u in enumerate(usuarios):
            print(f'  {i+1}. {u.get_nombre()}')
        idx = int(input("Elige el numero del usuario: ")) - 1
        usuarios[idx].mostrar_info()

    elif(opcion == "7"):
        #ver empleados
        gestion.mostrar_empleados()

    elif(opcion == "8"):
        print("\nHasta pronto. Gracias por usar el Sistema de la Biblioteca.\n")

    else:
        print("\n-> Opcion no valida. Elige entre 1 y 8.")
        
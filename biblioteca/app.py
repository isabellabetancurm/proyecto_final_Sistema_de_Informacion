import streamlit as st
import sys
import os

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
from excepciones.excepciones import LibroNoDisponibleError, LibroNoEncontradoError
from excepciones.validaciones import validar_nombre, validar_cedula, validar_telefono, validar_edad, validar_direccion, validar_año

# ─────────────────────────────────────────
# Configuracion de la pagina
# ─────────────────────────────────────────
st.set_page_config(
    page_title="Biblioteca Municipal",
    page_icon="📚",
    layout="wide"
)

# ─────────────────────────────────────────
# Inicializar datos en session_state
# si no existen todavia
# ─────────────────────────────────────────
if "catalogo" not in st.session_state:
    catalogo = Catalogo()
    catalogo.agregar_libro(literatura_cientifica("Cosmos", "Carl Sagan", 1980, "Astronomia", "Avanzado"))
    catalogo.agregar_libro(literatura_academica("Calculo", "James Stewart", 2015, "Matematicas", "Universidad"))
    catalogo.agregar_libro(literatura_infantil("El Principito", "Antoine de Saint-Exupery", 1943, 8, True))
    catalogo.agregar_libro(Novela("Cien Anos de Soledad", "Gabriel Garcia Marquez", 1967, "Drama", 471))
    catalogo.agregar_libro(Comic("Watchmen", "Alan Moore", 1987, "DC Comics", 1))
    catalogo.agregar_libro(Poesia("Veinte Poemas de Amor", "Pablo Neruda", 1924, "Romantica", 20))
    catalogo.agregar_libro(Bibliografia_artistica("El Arte del Renacimiento", "Giorgio Vasari", 1550, "Pintura", "Oleo"))
    st.session_state.catalogo = catalogo

if "usuarios" not in st.session_state:
    st.session_state.usuarios = [
        Usuario("Maria Gonzalez", "1094567890", 22, "3001234567", "Calle 10 # 5-20"),
        Usuario("Carlos Perez",   "1023456789", 30, "3109876543", "Carrera 8 # 3-15"),
    ]

if "empleados" not in st.session_state:
    gestion = GestionEmpleados()
    gestion.agregar_empleado(Empleado("Laura Martinez", "1056789012", "3207654321", 2_500_000))
    st.session_state.gestion = gestion

if "prestamos" not in st.session_state:
    st.session_state.prestamos = []

# ─────────────────────────────────────────
# Titulo principal
# ─────────────────────────────────────────
st.title("📚 Biblioteca Municipal")
st.markdown("**Sistema de Información — Programación I**")
st.divider()

# ─────────────────────────────────────────
# Menu lateral
# ─────────────────────────────────────────
opcion = st.sidebar.selectbox(
    "📋 Menu principal",
    [
        "🏠 Inicio",
        "📖 Ver catalogo",
        "🔍 Buscar libro",
        "➕ Agregar libro",
        "🔄 Registrar prestamo",
        "↩️ Registrar devolucion",
        "📋 Ver prestamos activos",
        "👤 Registrar usuario",
        "👥 Ver usuarios",
        "👷 Ver empleados",
    ]
)

# ─────────────────────────────────────────
# INICIO
# ─────────────────────────────────────────
if opcion == "🏠 Inicio":
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("📚 Libros en catalogo", len(st.session_state.catalogo._Catalogo__libros))
    with col2:
        st.metric("👤 Usuarios registrados", len(st.session_state.usuarios))
    with col3:
        activos = [p for p in st.session_state.prestamos if p.get_fecha_devolucion() is None]
        st.metric("🔄 Prestamos activos", len(activos))
    with col4:
        disponibles = [l for l in st.session_state.catalogo._Catalogo__libros if l.get_disponible()]
        st.metric("✅ Libros disponibles", len(disponibles))

    st.markdown("### Bienvenido al Sistema de la Biblioteca Municipal")
    st.markdown("Usa el menu de la izquierda para navegar por el sistema.")

# ─────────────────────────────────────────
# VER CATALOGO
# ─────────────────────────────────────────
elif opcion == "📖 Ver catalogo":
    st.header("📖 Catalogo de Libros")
    libros = st.session_state.catalogo._Catalogo__libros
    if libros:
        data = []
        for libro in libros:
            data.append({
                "Titulo": libro.get_titulo(),
                "Autor": libro.get_autor(),
                "Año": libro.get_año(),
                "Estado": "✅ Disponible" if libro.get_disponible() else "❌ Prestado",
                "Categoria": type(libro).__name__
            })
        st.dataframe(data, use_container_width=True)
    else:
        st.info("El catalogo esta vacio.")

# ─────────────────────────────────────────
# BUSCAR LIBRO
# ─────────────────────────────────────────
elif opcion == "🔍 Buscar libro":
    st.header("🔍 Buscar Libro")
    titulo = st.text_input("Ingrese el titulo del libro:")
    if st.button("Buscar"):
        if titulo:
            libro = st.session_state.catalogo.buscar_libro(titulo)
            if libro:
                st.success(f"Libro encontrado: {libro.get_titulo()} — {libro.get_autor()} ({libro.get_año()})")
                st.write(f"Estado: {'✅ Disponible' if libro.get_disponible() else '❌ Prestado'}")
            else:
                st.error(f'El libro "{titulo}" no se encuentra en el catalogo.')

# ─────────────────────────────────────────
# AGREGAR LIBRO
# ─────────────────────────────────────────
elif opcion == "➕ Agregar libro":
    st.header("➕ Agregar Libro al Catalogo")
    categoria = st.selectbox("Categoria", [
        "Literatura Cientifica", "Literatura Academica", "Literatura Infantil",
        "Novela", "Comic", "Poesia", "Bibliografia Artistica"
    ])
    titulo = st.text_input("Titulo")
    autor  = st.text_input("Autor")
    año    = st.number_input("Año", min_value=1800, max_value=2026, value=2020)

    if categoria == "Literatura Cientifica":
        area  = st.text_input("Area de ciencia")
        nivel = st.selectbox("Nivel", ["Basico", "Intermedio", "Avanzado"])
    elif categoria == "Literatura Academica":
        materia = st.text_input("Materia")
        nivel   = st.selectbox("Nivel educativo", ["Bachillerato", "Universidad", "Posgrado"])
    elif categoria == "Literatura Infantil":
        edad_rec  = st.number_input("Edad recomendada", min_value=1, max_value=18, value=8)
        ilustrado = st.checkbox("Es ilustrado")
    elif categoria == "Novela":
        subgenero   = st.selectbox("Subgenero", ["Thriller", "Drama", "Historica", "Aventura"])
        num_paginas = st.number_input("Numero de paginas", min_value=1, value=200)
    elif categoria == "Comic":
        editorial      = st.text_input("Editorial")
        numero_edicion = st.number_input("Numero de edicion", min_value=1, value=1)
    elif categoria == "Poesia":
        estilo     = st.selectbox("Estilo", ["Clasica", "Contemporanea", "Romantica"])
        num_poemas = st.number_input("Numero de poemas", min_value=1, value=20)
    elif categoria == "Bibliografia Artistica":
        tipo_arte = st.selectbox("Tipo de arte", ["Pintura", "Fotografia", "Escultura"])
        tecnica   = st.selectbox("Tecnica", ["Acuarela", "Oleo", "Digital"])

    if st.button("Agregar libro"):
        if titulo and autor:
            if categoria == "Literatura Cientifica":
                nuevo = literatura_cientifica(titulo, autor, año, area, nivel)
            elif categoria == "Literatura Academica":
                nuevo = literatura_academica(titulo, autor, año, materia, nivel)
            elif categoria == "Literatura Infantil":
                nuevo = literatura_infantil(titulo, autor, año, edad_rec, ilustrado)
            elif categoria == "Novela":
                nuevo = Novela(titulo, autor, año, subgenero, int(num_paginas))
            elif categoria == "Comic":
                nuevo = Comic(titulo, autor, año, editorial, int(numero_edicion))
            elif categoria == "Poesia":
                nuevo = Poesia(titulo, autor, año, estilo, int(num_poemas))
            elif categoria == "Bibliografia Artistica":
                nuevo = Bibliografia_artistica(titulo, autor, año, tipo_arte, tecnica)
            st.session_state.catalogo.agregar_libro(nuevo)
            st.success(f'Libro "{titulo}" agregado al catalogo exitosamente.')
        else:
            st.warning("Por favor ingrese titulo y autor.")

# ─────────────────────────────────────────
# REGISTRAR PRESTAMO
# ─────────────────────────────────────────
elif opcion == "🔄 Registrar prestamo":
    st.header("🔄 Registrar Prestamo")
    libros_disponibles = [l for l in st.session_state.catalogo._Catalogo__libros if l.get_disponible()]
    if libros_disponibles and st.session_state.usuarios:
        libro_sel   = st.selectbox("Selecciona el libro", [l.get_titulo() for l in libros_disponibles])
        usuario_sel = st.selectbox("Selecciona el usuario", [u.get_nombre() for u in st.session_state.usuarios])
        fecha       = st.date_input("Fecha de prestamo")
        if st.button("Registrar prestamo"):
            libro   = next(l for l in libros_disponibles if l.get_titulo() == libro_sel)
            usuario = next(u for u in st.session_state.usuarios if u.get_nombre() == usuario_sel)
            libro.prestar()
            usuario.agregar_libro_prestado(libro)
            prestamo = Prestamo(usuario, libro, str(fecha))
            st.session_state.prestamos.append(prestamo)
            st.success(f'Prestamo registrado: "{libro_sel}" para {usuario_sel}.')
    else:
        st.warning("No hay libros disponibles o usuarios registrados.")

# ─────────────────────────────────────────
# REGISTRAR DEVOLUCION
# ─────────────────────────────────────────
elif opcion == "↩️ Registrar devolucion":
    st.header("↩️ Registrar Devolucion")
    activos = [p for p in st.session_state.prestamos if p.get_fecha_devolucion() is None]
    if activos:
        prestamo_sel = st.selectbox("Selecciona el prestamo", [f"{p.get_libro().get_titulo()} — {p.get_usuario().get_nombre()}" for p in activos])
        fecha_dev    = st.date_input("Fecha de devolucion")
        if st.button("Registrar devolucion"):
            for p in activos:
                if f"{p.get_libro().get_titulo()} — {p.get_usuario().get_nombre()}" == prestamo_sel:
                    p.registrar_devolucion(str(fecha_dev))
                    p.get_usuario().quitar_libro_prestado(p.get_libro())
                    st.success(f'Devolucion registrada exitosamente.')
                    break
    else:
        st.info("No hay prestamos activos.")

# ─────────────────────────────────────────
# VER PRESTAMOS ACTIVOS
# ─────────────────────────────────────────
elif opcion == "📋 Ver prestamos activos":
    st.header("📋 Prestamos Activos")
    activos = [p for p in st.session_state.prestamos if p.get_fecha_devolucion() is None]
    if activos:
        data = [{"Libro": p.get_libro().get_titulo(), "Usuario": p.get_usuario().get_nombre(), "Fecha prestamo": p.get_fecha_prestamo()} for p in activos]
        st.dataframe(data, use_container_width=True)
    else:
        st.info("No hay prestamos activos.")

# ─────────────────────────────────────────
# REGISTRAR USUARIO
# ─────────────────────────────────────────
elif opcion == "👤 Registrar usuario":
    st.header("👤 Registrar Nuevo Usuario")
    nombre    = st.text_input("Nombre completo")
    cedula    = st.text_input("Cedula (10 digitos)")
    edad      = st.number_input("Edad", min_value=1, max_value=120, value=18)
    telefono  = st.text_input("Telefono (10 digitos)")
    direccion = st.text_input("Direccion (Calle, Carrera, Avenida...)")

    if st.button("Registrar usuario"):
        errores = []
        if len(nombre.split()) < 2:
            errores.append("El nombre debe tener nombre y apellido completos.")
        if not cedula.isdigit() or len(cedula) != 10:
            errores.append("La cedula debe tener exactamente 10 digitos.")
        if not telefono.isdigit() or len(telefono) != 10:
            errores.append("El telefono debe tener exactamente 10 digitos.")
        if not any(p in direccion.lower() for p in ["calle", "carrera", "avenida", "diagonal", "transversal"]):
            errores.append("La direccion debe contener Calle, Carrera, Avenida, etc.")
        if errores:
            for error in errores:
                st.error(error)
        else:
            nuevo_usuario = Usuario(nombre, cedula, int(edad), telefono, direccion)
            st.session_state.usuarios.append(nuevo_usuario)
            st.success(f'Usuario "{nombre}" registrado exitosamente.')

# ─────────────────────────────────────────
# VER USUARIOS
# ─────────────────────────────────────────
elif opcion == "👥 Ver usuarios":
    st.header("👥 Usuarios Registrados")
    if st.session_state.usuarios:
        data = []
        for u in st.session_state.usuarios:
            data.append({
                "Nombre": u.get_nombre(),
                "Cedula": u.get_cedula(),
                "Edad": u.get_edad(),
                "Telefono": u.get_telefono(),
                "Direccion": u.get_direccion(),
                "Libros prestados": len(u.get_libros_prestados())
            })
        st.dataframe(data, use_container_width=True)
    else:
        st.info("No hay usuarios registrados.")

# ─────────────────────────────────────────
# VER EMPLEADOS
# ─────────────────────────────────────────
elif opcion == "👷 Ver empleados":
    st.header("👷 Empleados de la Biblioteca")
    empleados = st.session_state.gestion._GestionEmpleados__empleados
    if empleados:
        data = []
        for e in empleados:
            data.append({
                "Nombre": e.get_nombre(),
                "Cedula": e.get_cedula(),
                "Telefono": e.get_telefono(),
                "Salario": f"${e.get_salario():,.0f}"
            })
        st.dataframe(data, use_container_width=True)
    else:
        st.info("No hay empleados registrados.")
        

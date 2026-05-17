# 📚 Sistema de Información — Biblioteca Municipal
**Programación I**

Sistema de gestión para una biblioteca municipal desarrollado en Python, 
aplicando los conceptos de Programación Orientada a Objetos (POO).

---
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Estado](https://img.shields.io/badge/Estado-Completo-green)
![POO](https://img.shields.io/badge/POO-Aplicada-purple)
![Universidad](https://img.shields.io/badge/Universidad-Manizales-red)
![Asignatura](https://img.shields.io/badge/Materia-Programacion_I-orange)

---

## 📂 Estructura del Proyecto

```bash
proyecto_final_Sistema_de_Informacion/
│
└── biblioteca/
    ├── modelos/
    │   ├── libros/
    │   │   ├── libro.py
    │   │   ├── literatura_cientifica.py
    │   │   ├── literatura_academica.py
    │   │   ├── literatura_infantil.py
    │   │   ├── novela.py
    │   │   ├── comic.py
    │   │   ├── poesia.py
    │   │   └── bibliografia_artistica.py
    │   ├── usuario.py
    │   └── empleado.py
    │
    ├── servicios/
    │   ├── catalogo.py
    │   ├── prestamo.py
    │   └── gestion_empleados.py
    │
    ├── excepciones/
    │   ├── validaciones.py
    │   └── excepciones.py
    │
    └── main.py
```

## 🧠 Conceptos aplicados

| Concepto | Dónde se aplica |
|---|---|
| Clases y atributos | Todos los archivos de modelos |
| Método constructor | __init__ en todas las clases |
| Encapsulamiento | Atributos privados con __ en todas las clases |
| Métodos | prestar(), devolver(), mostrar_info(), etc |
| Herencia | 7 categorías de libros heredan de Libro |
| Polimorfismo | mostrar_info() diferente en cada categoría |
| Composición | Catalogo, Prestamo, GestionEmpleados |
| Excepciones | Errores personalizados en excepciones.py |
| Validaciones | Validación de datos en validaciones.py |

---
## ✨ Funcionalidades
- 📖 Gestión del catálogo de libros por categoría
- 👤 Registro y consulta de usuarios
- 🔄 Préstamo y devolución de libros
- 👷 Gestión de empleados
- ⚠️ Manejo de errores con excepciones personalizadas
- ✅ Validación de datos de entrada


 ## 🖥️ Vista del sistema
<img width="387" height="326" alt="screenshot png" src="https://github.com/user-attachments/assets/7309e6d3-528a-4f48-99a5-a75ba54b3783" />


## ▶️ Cómo ejecutar

1. Clona el repositorio
2. Abre la carpeta biblioteca en la terminal
3. Ejecuta el archivo principal:

python main.py

---
## 📝 Notas de Desarrollo
* El código sigue los estándares de la asignatura de **Programación I**.
* Se utiliza **Programación Orientada a Objetos (POO)**.
* Se cumplen todos los requisitos del proyecto final.

---
*Facultad de Ciencias e Ingeniería - Universidad de Manizales*

## 👤 Autora
**Isabella Betancur**
Ingeniería de Sistemas
Programación I — 2026

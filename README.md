# 📚 Sistema de Información — Biblioteca Municipal
**Programación I**

Sistema de gestión para una biblioteca municipal desarrollado en Python, 
aplicando los conceptos de Programación Orientada a Objetos (POO).

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

## ▶️ Cómo ejecutar

1. Clona el repositorio
2. Abre la carpeta biblioteca en la terminal
3. Ejecuta el archivo principal:

python main.py

---

## 👤 Autora
**Isabella Betancur**
Ingeniería de Sistemas
Programación I — 2026

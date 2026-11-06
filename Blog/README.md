# Blog de Patricio (consola)

## Qué hace el programa
Sistema de consola en Python para gestionar posts de un blog sobre análisis táctico
(Excel, Power BI, Wyscout, Livetag). Permite ver todos los posts, buscar por título,
filtrar por tag y validar que cada post esté bien armado.

## Cómo ejecutarlo
Desde la carpeta raíz del proyecto:

```
python main.py
```

Al iniciar pide una clave de acceso y luego muestra el menú.

## Organización de la carpeta

```
Blog/
├── blog.consola
│   ├── __init__.py
│   ├── datos.py
│   ├── menu.py
│   ├── operaciones.py
│   └── validaciones.py
├── main.py
└── README.md
```

## Responsabilidad de cada módulo
- `blog/datos.py`: estructuras base (`perfil_autor`, `estados_post`, `etiquetas_blog`, `posts`). El autor es un diccionario anidado dentro de cada post.
- `blog/menu.py`: muestra el menú, pide la opción con `input()` (con `try-except`) y la retorna.
- `blog/operaciones.py`: `listar_posts`, `buscar_por_titulo` y `filtrar_por_tag`. Reciben la lista por parámetro y las búsquedas retornan resultados.
- `blog/validaciones.py`: `validar_post`, con las reglas que debe cumplir un post.
- `main.py`: punto de entrada; conecta los módulos y contiene el bucle principal.

## Archivo a ejecutar
`main.py`
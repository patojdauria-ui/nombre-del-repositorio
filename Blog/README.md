Blog de Patricio (consola)
Qué hace el programa

Sistema de consola en Python para gestionar posts de un blog sobre análisis táctico (Excel, Power BI, Wyscout, Livetag). Permite ver todos los posts, buscar por título, filtrar por tag, crear posts nuevos, validar que cada post esté bien armado y guardar todo en un archivo posts.json para que los datos sigan disponibles la próxima vez que se ejecute el programa.

Cómo ejecutarlo

Desde la carpeta raíz del proyecto:

python main.py

Al iniciar pide una clave de acceso, carga los posts desde posts.json y muestra el menú:

--- MENU DEL BLOG ---
1. Ver todos los posts
2. Buscar por titulo
3. Filtrar por tag
4. Crear nuevo post
5. Validar posts
6. Guardar posts en JSON
7. Salir


Organización de la carpeta:

Blog
├── blog/
│   ├── __init__.py
│   ├── datos.py
│   ├── menu.py
│   ├── modelos.py
│   ├── operaciones.py
│   └── validaciones.py
├── main.py
├── posts.json
└── README.md
Clases principales (blog/modelos.py)
Clase	Responsabilidad
Autor	Representa a la persona autora: nombre, bio, especialidad y licencia.
Post	Representa una publicación: id, titulo, contenido, autor, tags y estado. El atributo autor es una instancia de Autor (composición).
Blog	Guarda la lista de objetos Post y centraliza la lógica: listar, buscar por título, filtrar por tag, crear y validar posts, y obtener todos los posts.

Los estados permitidos de un post (estados_post) también se definen en modelos.py.

Conversión entre objetos y diccionarios

JSON no puede guardar objetos propios de Python, así que cada clase sabe convertirse:

Autor.to_dict() y Post.to_dict() convierten el objeto a diccionario (el post incluye a su autor como diccionario).
Blog.posts_a_dicts() convierte toda la lista de posts en una lista de diccionarios.
Autor.desde_dict(datos) y Post.desde_dict(datos) reconstruyen los objetos a partir de un diccionario. Si el diccionario está incompleto lanzan ValueError indicando qué claves faltan.
Módulos
blog/modelos.py: las clases Autor, Post y Blog.
blog/datos.py: etiquetas_blog, el autor del blog (perfil_autor), los posts de ejemplo (posts_iniciales()) y la persistencia: cargar_blog() y guardar_blog(blog).
blog/menu.py: muestra el menú, pide la opción con input() (con try-except) y pide los textos y los datos de un post nuevo.
blog/operaciones.py: una función por cada opción del menú (mostrar_posts, buscar_posts, filtrar_posts, crear_post_desde_consola, validar_todos, guardar_posts). Reciben el Blog y llaman a sus métodos.
blog/validaciones.py: validar_post(post), con las reglas que debe cumplir un post. Retorna (True, "") si es válido o (False, motivo) si no. Blog.validar_post usa esta función.
main.py: punto de entrada (protegido con if __name__ == "__main__":). Pide la clave, carga el blog, muestra el menú y deriva cada opción a operaciones.py.
Cómo se guarda y se carga la información (posts.json)

Cargar (al iniciar): cargar_blog() lee posts.json, convierte cada diccionario en un objeto Post con Post.desde_dict() y devuelve un Blog con esa lista.

Guardar (opción 6, o al salir si hay cambios): guardar_blog(blog) convierte los posts a diccionarios con blog.posts_a_dicts() y los escribe en posts.json con el módulo json. El texto JSON se arma antes de abrir el archivo, así que si algo falla el archivo anterior no se pierde.

Si algo sale mal, el programa no se cierra:

Si posts.json no existe, está vacío o tiene contenido inválido, avisa qué pasó y arranca con los posts de ejemplo.
Si un elemento del JSON está incompleto (por ejemplo, le falta el autor), lo omite con un aviso y carga el resto.
Si hay un error al convertir o escribir el archivo, muestra un mensaje y no guarda.
Si el usuario elige una opción inválida o deja campos vacíos al crear un post, muestra un mensaje claro y vuelve al menú.

El post 3 de los datos de ejemplo es incorrecto a propósito (tags no es una lista) para poder comprobar la opción 5, "Validar posts".

Qué cambió respecto al checkpoint anterior:

Los datos dejaron de ser diccionarios sueltos: ahora hay clases Autor, Post y Blog, y los posts tienen como autor un objeto Autor.
Listar, buscar y filtrar pasaron de funciones a métodos de Blog.

Operaciones.py ahora contiene las acciones del menú que trabajan con el Blog, y validaciones.py mantiene las reglas de validación, adaptadas para validar objetos Post.
Se agregó persistencia con posts.json: carga al iniciar y guardado manual desde el menú.
El menú pasó de 5 a 7 opciones: se agregaron "Crear nuevo post" y "Guardar posts en JSON".
main.py ahora carga el blog y delega cada opción en operaciones.py, que usa los métodos de Blog.
Archivo a ejecutar

main.py

import json
from pathlib import Path

from blog.modelos import Autor, Post, Blog

# posts.json queda en la carpeta raíz del proyecto, sin importar desde dónde se ejecute
RUTA_POSTS = Path(__file__).resolve().parent.parent / "posts.json"

# Etiquetas permitidas
etiquetas_blog = {"excel", "powerbi", "wyscout", "livetag"}

# Autor del blog: objeto Autor (se reutiliza dentro de cada post)
perfil_autor = Autor(
    nombre="patricio",
    bio="analista tactico tanto en empresa y en futbol",
    especialidad="excel con power bi y en el futbol con livetag",
    licencia=["licencia_pro"],
)


def posts_iniciales():
    
    return [
        Post(
            post_id=1,
            titulo="primer uso con el excel",
            contenido="uso de excel para analizar partidos y jugadores",
            autor=perfil_autor,
            tags=["excel"],
            estado="enviado",
        ),
        Post(
            post_id=2,
            titulo="que herramienta uso en el futbol",
            contenido="uso de livetag para analizar partidos",
            autor=perfil_autor,
            tags=["livetag"],
            estado="archivado",
        ),
        Post(
            # Post incompleto a propósito: tags=None (no es una lista), así que no valida.
            post_id=3,
            titulo="que uso para analizar partidos",
            contenido="uso de wyscout para analizar partidos y jugadores",
            autor=perfil_autor,
            tags=None,
            estado="borrador",
        ),
        Post(
            post_id=4,
            titulo="que uso para graficar mediante los datos que tengo",
            contenido="uso de power bi para graficar los datos que tengo",
            autor=perfil_autor,
            tags=["powerbi"],
            estado="enviado",
        ),
    ]


def cargar_blog(ruta=RUTA_POSTS):
    
   
    ruta = Path(ruta)

    try:
        texto = ruta.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"No se encontro {ruta.name}. Se cargan los posts iniciales.")
        return Blog(posts_iniciales())
    except OSError as error:
        print(f"No se pudo leer {ruta.name} ({error}). Se cargan los posts iniciales.")
        return Blog(posts_iniciales())

    if not texto.strip():
        print(f"{ruta.name} esta vacio. Se cargan los posts iniciales.")
        return Blog(posts_iniciales())

    try:
        datos = json.loads(texto)
    except json.JSONDecodeError as error:
        print(f"{ruta.name} tiene contenido invalido ({error}). Se cargan los posts iniciales.")
        print("Si guarda los posts, se va a reemplazar ese archivo.")
        return Blog(posts_iniciales())

    if not isinstance(datos, list):
        print(f"{ruta.name} debe contener una lista de posts. Se cargan los posts iniciales.")
        print("Si guarda los posts, se va a reemplazar ese archivo.")
        return Blog(posts_iniciales())

    posts = []
    omitidos = 0
    for posicion, dato in enumerate(datos, start=1):
        try:
            posts.append(Post.desde_dict(dato))
        except ValueError as error:
            omitidos += 1
            print(f"Se omitio el elemento {posicion} de {ruta.name}: {error}.")

    if omitidos:
        print("Si guarda los posts, los elementos omitidos se van a perder del archivo.")

    return Blog(posts)


def guardar_blog(blog, ruta=RUTA_POSTS):
    """Guarda los posts del blog en posts.json. Retorna True si se guardó bien."""
    ruta = Path(ruta)

    try:
        # Primero se convierten los objetos a diccionarios y se arma el texto JSON;
        # así, si algo falla, el archivo anterior no se toca.
        texto = json.dumps(blog.posts_a_dicts(), indent=4, ensure_ascii=False)
    except (TypeError, ValueError, AttributeError) as error:
        print(f"No se pudo convertir los posts a JSON ({error}). No se guardo nada.")
        return False

    try:
        ruta.write_text(texto, encoding="utf-8")
    except OSError as error:
        print(f"No se pudo escribir {ruta.name} ({error}).")
        return False

    return True

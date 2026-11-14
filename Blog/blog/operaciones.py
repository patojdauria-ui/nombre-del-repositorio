from blog.datos import guardar_blog, perfil_autor
from blog.menu import pedir_datos_post


def pedir_texto(mensaje):
    """Pide texto por consola."""
    return input(mensaje)


def mostrar_posts(blog):
    """Opción 1: muestra todos los posts del blog."""
    blog.listar_posts()


def buscar_posts(blog):
    """Opción 2: pide un título, busca y muestra los resultados."""
    termino = pedir_texto("Ingrese el titulo a buscar: ")
    if termino is None:
        return

    resultados = blog.buscar_por_titulo(termino)
    if resultados:
        blog.listar_posts(resultados)
    else:
        print("No se encontraron posts con ese titulo.")


def filtrar_posts(blog):
    """Opción 3: pide una etiqueta, filtra y muestra los resultados."""
    tag = pedir_texto("Ingrese la etiqueta a buscar: ")
    if tag is None:
        return

    resultados = blog.filtrar_por_tag(tag)
    if resultados:
        blog.listar_posts(resultados)
    else:
        print("No se encontraron posts con esa etiqueta.")


def crear_post_desde_consola(blog):
    """Opción 4: pide los datos y crea el post. Retorna True si se agregó al blog."""
    datos = pedir_datos_post()
    if datos is None:
        return False

    try:
        post = blog.crear_post(autor=perfil_autor, **datos)
    except ValueError as error:
        print(f"No se pudo crear el post: {error}.")
        return False

    print(f"Post creado: {post}")
    return True


def validar_todos(blog):
    """Opción 5: valida cada post del blog e imprime el resultado."""
    for id_post, es_valido, motivo in blog.validar_posts():
        if es_valido:
            print(f"Post {id_post}: valido")
        else:
            print(f"Post {id_post}: INVALIDO ({motivo})")


def guardar_posts(blog):
    """Opción 6: guarda los posts en posts.json. Retorna True si se guardó bien."""
    if guardar_blog(blog):
        print("Posts guardados en posts.json")
        return True
    return False

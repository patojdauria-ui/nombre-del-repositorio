from blog.datos import cargar_blog, guardar_blog, perfil_autor
from blog.menu import mostrar_menu, pedir_datos_post, preguntar_si_no


def pedir_clave():
    """Pide la clave de acceso hasta que sea correcta."""
    while True:
        clave = input("Ingrese la clave de acceso: ")
        if clave == "patricio":
            print("Clave correcta")
            break
        print("Clave incorrecta, intente nuevamente")


def validar_todos(blog):
    """Valida cada post del blog e imprime el resultado."""
    for id_post, es_valido, motivo in blog.validar_posts():
        if es_valido:
            print(f"Post {id_post}: valido")
        else:
            print(f"Post {id_post}: INVALIDO ({motivo})")


def crear_post_desde_consola(blog):
    """Pide los datos y crea el post. Retorna True si se agregó al blog."""
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


def main():
    """Ejecuta el flujo principal de la aplicación del blog."""
    pedir_clave()
    blog = cargar_blog()
    hay_cambios = False  # True si hay posts creados que todavía no se guardaron

    def listar_posts():
        """Muestra todos los posts disponibles."""
        blog.listar_posts()

    def buscar_por_titulo():
        """Busca posts por un título y los muestra si existen."""
        termino = input("Ingrese el titulo a buscar: ")
        resultados = blog.buscar_por_titulo(termino)
        if resultados:
            blog.listar_posts(resultados)
        else:
            print("No se encontraron posts con ese titulo.")

    def filtrar_por_tag():
        """Filtra posts por una etiqueta y los muestra."""
        tag = input("Ingrese la etiqueta a buscar: ")
        resultados = blog.filtrar_por_tag(tag)
        if resultados:
            blog.listar_posts(resultados)
        else:
            print("No se encontraron posts con esa etiqueta.")

    def crear_post():
        """Crea un post nuevo desde la consola y registra cambios."""
        nonlocal hay_cambios
        if crear_post_desde_consola(blog):
            hay_cambios = True

    def validar_posts():
        """Valida cada post del blog."""
        validar_todos(blog)

    def guardar_posts():
        """Guarda los posts actuales en disco."""
        nonlocal hay_cambios
        if guardar_blog(blog):
            print("Posts guardados en posts.json")
            hay_cambios = False

    def salir():
        """Sale del programa y guarda cambios pendientes si corresponde."""
        nonlocal hay_cambios
        if hay_cambios and preguntar_si_no("Hay posts sin guardar. Guardar antes de salir?"):
            if guardar_blog(blog):
                print("Posts guardados en posts.json")
        print("¡Nos vemos la proxima!")

    opciones = {
        "1": listar_posts,
        "2": buscar_por_titulo,
        "3": filtrar_por_tag,
        "4": crear_post,
        "5": validar_posts,
        "6": guardar_posts,
        "7": salir,
    }

    while True:
        opcion = mostrar_menu()
        accion = opciones.get(opcion)
        if accion is None:
            continue
        accion()
        if opcion == "7":
            break


if __name__ == "__main__":
    main()

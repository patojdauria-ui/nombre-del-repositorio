from blog.modelos import estados_post


def mostrar_menu():
    """Muestra las opciones, pide una y retorna la opción elegida (str)."""
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Crear nuevo post")
    print("5. Validar posts")
    print("6. Guardar posts en JSON")
    print("7. Salir")

    try:
        opcion = input("Seleccione un numero: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nEntrada cancelada. Saliendo...")
        return "7"

    if opcion not in ("1", "2", "3", "4", "5", "6", "7"):
        print("Opcion invalida, intente nuevamente.")
        return ""

    return opcion


def pedir_datos_post():
    """Pide por consola los datos de un post nuevo.

    Retorna un diccionario con titulo, contenido, tags (lista) y estado,
    o None si se cancela la entrada. No valida: eso lo hace Blog.crear_post.
    """
    try:
        titulo = input("Titulo: ").strip()
        contenido = input("Contenido: ").strip()
        tags_texto = input("Tags (separados por coma): ")
        estado = input(f"Estado ({', '.join(estados_post)}) [borrador]: ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        print("\nCreacion cancelada.")
        return None

    tags = [tag.strip().lower() for tag in tags_texto.split(",") if tag.strip()]

    return {
        "titulo": titulo,
        "contenido": contenido,
        "tags": tags,
        "estado": estado or "borrador",
    }


def preguntar_si_no(pregunta):
    """Hace una pregunta de sí/no. Retorna True solo si la respuesta empieza con 's'."""
    try:
        return input(pregunta + " (s/n): ").strip().lower().startswith("s")
    except (EOFError, KeyboardInterrupt):
        return False

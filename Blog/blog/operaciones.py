"""Funciones principales del blog: listar, buscar y filtrar."""


def listar_posts(lista):
    """Muestra los datos de cada post de la lista recibida."""
    if not lista:
        print("No hay posts para mostrar.")
        return

    for post in lista:
        print("\nTitulo:", post.get("titulo", "(sin titulo)"))
        print("Contenido:", post.get("contenido", "(sin contenido)"))
        print("Autor:", post.get("autor", {}).get("nombre", "(sin autor)"))
        print("Tags:", post.get("tags", "(sin tags)"))
        print("Estado:", post.get("estado", "(sin estado)"))


def buscar_por_titulo(lista, termino):
    """Retorna los posts cuyo título contiene el término (sin importar mayúsculas)."""
    termino = termino.strip().lower()
    resultados = []
    for post in lista:
        if termino in post.get("titulo", "").lower():
            resultados.append(post)
    return resultados


def filtrar_por_tag(lista, tag):
    """Retorna los posts que tienen la etiqueta indicada."""
    tag = tag.strip().lower()
    resultados = []
    for post in lista:
        tags = post.get("tags", [])
        if tag in [t.lower() for t in tags]:
            resultados.append(post)
    return resultados
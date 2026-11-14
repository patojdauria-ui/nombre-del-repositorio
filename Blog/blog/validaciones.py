from blog.modelos import Autor, Post, estados_post


def validar_post(post):
    """Valida un post. Retorna (True, "") si es válido o (False, motivo) si no."""
    if not isinstance(post, Post):
        return False, "el post no es una instancia de Post"

    if post.id is None:
        return False, "falta el id"

    if not isinstance(post.titulo, str) or not post.titulo.strip():
        return False, "el titulo esta vacio"

    if not isinstance(post.contenido, str) or not post.contenido.strip():
        return False, "el contenido esta vacio"

    if not isinstance(post.autor, Autor):
        return False, "el autor no es una instancia de Autor"

    if not post.autor.nombre:
        return False, "el autor no tiene nombre"

    if not isinstance(post.tags, list):
        return False, "los tags no estan guardados como lista"

    if post.estado not in estados_post:
        return False, "el estado no es valido"

    return True, ""

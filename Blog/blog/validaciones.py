
try:
    from .datos import estados_post
except ImportError:  # pragma: no cover - soporte para ejecución directa
    from datos import estados_post

CLAVES_NECESARIAS = ("id", "titulo", "contenido", "autor", "tags", "estado")


def validar_post(post):
    """Valida un post. Retorna (True, "") si es válido o (False, motivo) si no."""
    if not isinstance(post, dict):
        return False, "el post no es un diccionario"

    for clave in CLAVES_NECESARIAS:
        if clave not in post:
            return False, f"falta la clave '{clave}'"

    if not post["titulo"].strip():
        return False, "el titulo esta vacio"

    if not post["contenido"].strip():
        return False, "el contenido esta vacio"

    autor = post["autor"]
    if not isinstance(autor, dict):
        return False, "el autor no es un diccionario"

    if not autor.get("nombre"):
        return False, "el autor no tiene nombre"

    if not isinstance(post["tags"], list):
        return False, "los tags no estan guardados como lista"

    if post["estado"] not in estados_post:
        return False, "el estado no es valido"

    return True, ""
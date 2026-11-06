"""Programa de gestión de posts de Patricio. Archivo a ejecutar: python main.py"""

from blog.datos import posts
from blog.menu import mostrar_menu
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_post


def pedir_clave():
    """Pide la clave de acceso hasta que sea correcta."""
    while True:
        clave = input("Ingrese la clave de acceso: ")
        if clave == "patricio":
            print("Clave correcta")
            break
        print("Clave incorrecta, intente nuevamente")


def validar_todos(lista):
    """Valida cada post e imprime el resultado."""
    for post in lista:
        es_valido, motivo = validar_post(post)
        id_post = post.get("id", "?") if isinstance(post, dict) else "?"
        if es_valido:
            print(f"Post {id_post}: valido")
        else:
            print(f"Post {id_post}: INVALIDO ({motivo})")


def main():
    pedir_clave()

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            listar_posts(posts)
        elif opcion == "2":
            termino = input("Ingrese el titulo a buscar: ")
            resultados = buscar_por_titulo(posts, termino)
            if resultados:
                listar_posts(resultados)
            else:
                print("No se encontraron posts con ese titulo.")
        elif opcion == "3":
            tag = input("Ingrese la etiqueta a buscar: ")
            resultados = filtrar_por_tag(posts, tag)
            if resultados:
                listar_posts(resultados)
            else:
                print("No se encontraron posts con esa etiqueta.")
        elif opcion == "4":
            validar_todos(posts)
        elif opcion == "5":
            print("Hasta luego")
            break


if __name__ == "__main__":
    main()
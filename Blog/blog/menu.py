"""Menú de la consola y manejo de input()."""


def mostrar_menu():
    """Muestra las opciones, pide una y retorna la opción elegida (str)."""
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")

    try:
        opcion = input("Seleccione un numero: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nEntrada cancelada. Saliendo...")
        return "5"

    if opcion not in ("1", "2", "3", "4", "5"):
        print("Opcion invalida, intente nuevamente.")
        return ""

    return opcion
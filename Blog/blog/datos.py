
# Estados permitidos para un post
estados_post = ("borrador", "enviado", "archivado")

# Etiquetas permitidas
etiquetas_blog = {"excel", "powerbi", "wyscout", "livetag"}

# Autor como diccionario (se reutiliza dentro de cada post: diccionario anidado)
perfil_autor = {
    "nombre": "patricio",
    "bio": "analista tactico tanto en empresa y en futbol",
    "especialidad": "excel con power bi y en el futbol con livetag",
    "licencia": ["licencia_pro"],
}

posts = [
    {
        "id": 1,
        "titulo": "primer uso con el excel",
        "contenido": "uso de excel para analizar partidos y jugadores",
        "autor": perfil_autor,
        "tags": ["excel"],
        "estado": "enviado",
    },
    {
        "id": 2,
        "titulo": "que herramienta uso en el futbol",
        "contenido": "uso de livetag para analizar partidos",
        "autor": perfil_autor,
        "tags": ["livetag"],
        "estado": "archivado",
    },
    {
        # Post incompleto a propósito: NO tiene la clave "tags".
        "id": 3,
        "titulo": "que uso para analizar partidos",
        "contenido": "uso de wyscout para analizar partidos y jugadores",
        "autor": perfil_autor,
        "estado": "borrador",
    },
    {
        "id": 4,
        "titulo": "que uso para graficar mediante los datos que tengo",
        "contenido": "uso de power bi para graficar los datos que tengo",
        "autor": perfil_autor,
        "tags": ["powerbi"],
        "estado": "enviado",
    },
]
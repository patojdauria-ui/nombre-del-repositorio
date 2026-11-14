
estados_post = ("borrador", "enviado", "archivado")


class Autor:
    """Persona autora del blog."""

    def __init__(self, nombre, bio, especialidad="", licencia=None):
        self.nombre = nombre
        self.bio = bio
        self.especialidad = especialidad
        self.licencia = licencia if licencia is not None else []

    def to_dict(self):
        """Devuelve una representación sencilla del autor."""
        return {
            "nombre": self.nombre,
            "bio": self.bio,
            "especialidad": self.especialidad,
            "licencia": self.licencia,
        }

    @classmethod
    def desde_dict(cls, datos):
        
        if not isinstance(datos, dict):
            raise ValueError("el autor no es un diccionario")

        faltantes = [clave for clave in ("nombre", "bio") if clave not in datos]
        if faltantes:
            raise ValueError(f"al autor le faltan las claves: {', '.join(faltantes)}")

        return cls(
            datos["nombre"],
            datos["bio"],
            datos.get("especialidad", ""),
            datos.get("licencia"),
        )

    def __str__(self):
        return self.nombre


class Post:

    def __init__(self, post_id, titulo, contenido, autor, tags, estado="borrador"):
        self.id = post_id
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.tags = tags
        self.estado = estado

    def to_dict(self):
       
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.to_dict() if isinstance(self.autor, Autor) else self.autor,
            "tags": self.tags,
            "estado": self.estado,
        }

    @classmethod
    def desde_dict(cls, datos):
       
        if not isinstance(datos, dict):
            raise ValueError("el post no es un diccionario")

        claves = ("id", "titulo", "contenido", "autor", "tags", "estado")
        faltantes = [clave for clave in claves if clave not in datos]
        if faltantes:
            raise ValueError(f"al post le faltan las claves: {', '.join(faltantes)}")

        autor = Autor.desde_dict(datos["autor"])
        return cls(
            datos["id"],
            datos["titulo"],
            datos["contenido"],
            autor,
            datos["tags"],
            datos["estado"],
        )

    def __str__(self):
        return f"[{self.id}] {self.titulo} ({self.estado})"


class Blog:
   

    def __init__(self, posts=None):
        self.posts = posts if posts is not None else []

    def obtener_posts(self):
      
        return list(self.posts)

    def posts_a_dicts(self):
       
        return [post.to_dict() for post in self.posts]

    def listar_posts(self, lista=None):
       
        if lista is None:
            lista = self.posts

        if not lista:
            print("No hay posts para mostrar.")
            return

        for post in lista:
            if isinstance(post.autor, Autor):
                nombre_autor = post.autor.nombre
            else:
                nombre_autor = "(sin autor)"

            print("\nTitulo:", post.titulo)
            print("Contenido:", post.contenido)
            print("Autor:", nombre_autor)
            print("Tags:", post.tags)
            print("Estado:", post.estado)

    def buscar_por_titulo(self, termino):
       
        termino = termino.strip().lower()
        resultados = []
        for post in self.posts:
            if termino in str(post.titulo).lower():
                resultados.append(post)
        return resultados

    def filtrar_por_tag(self, tag):
      
        tag = tag.strip().lower()
        resultados = []
        for post in self.posts:
            tags = post.tags if isinstance(post.tags, list) else []
            if tag in [t.lower() for t in tags]:
                resultados.append(post)
        return resultados

    def validar_post(self, post):
       
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

    def validar_posts(self):
     
        resultados = []
        for post in self.posts:
            es_valido, motivo = self.validar_post(post)
            resultados.append((post.id, es_valido, motivo))
        return resultados

    def crear_post(self, titulo, contenido, autor, tags=None, estado="borrador"):
        
        ids = [post.id for post in self.posts if isinstance(post.id, int)]
        nuevo_id = max(ids) + 1 if ids else 1

        if tags is None:
            tags = []

        post = Post(nuevo_id, titulo, contenido, autor, tags, estado)
        es_valido, motivo = self.validar_post(post)
        if not es_valido:
            raise ValueError(motivo)

        self.posts.append(post)
        return post

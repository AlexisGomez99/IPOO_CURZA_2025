from Autor import Autor


class Libro:
    def __init__(self, titulo, autor:Autor, anio):

        if not isinstance(autor, Autor):
             raise TypeError("El atributo 'autor' debe ser una instancia de la clase Autor.")
        if not titulo:
            raise ValueError("El título del libro no puede estar vacío.")
        if anio <= 0:
            raise ValueError("El año de publicación debe ser un valor positivo.")
        
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def to_dict(self):
        return {
            'titulo': self.titulo,
            'anio': self.anio,
            'autor': self.autor.to_dict() 
        }

    def __str__(self):
        return f"titulo: {self.titulo},anio: {self.anio} ,autor: {self.autor}"
    def __repr__(self):
        return self.__str__()


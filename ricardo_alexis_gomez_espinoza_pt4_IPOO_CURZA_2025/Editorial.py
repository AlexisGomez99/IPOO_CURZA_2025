from Libro import Libro 

class Editorial:
    def __init__(self, nombre, pais, libros_publicados):
        self.nombre = nombre
        self.pais = pais
        if not libros_publicados:
            self.libros_publicados = []
        else:
            self.libros_publicados = libros_publicados

    def agregar_libro(self,libro):
        self.libros_publicados.append(libro)

    def to_dict(self):
        libros_dicts = [libro.to_dict() for libro in self.libros_publicados]
        return {
            'nombre': self.nombre,
            'pais': self.pais,
            'libros_publicados': libros_dicts
        }
    
    def __str__(self):
        return f"nombre: {self.nombre},pais: {self.pais} ,\nlib ros publicados:\n {self.libros_publicados}"
    def __repr__(self):
        return self.__str__()
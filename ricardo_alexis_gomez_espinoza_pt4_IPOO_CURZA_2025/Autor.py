


class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
    
    def to_dict(self):
        return {
            'nombre': self.nombre,
            'nacionalidad': self.nacionalidad
        }
    
    def __str__(self):
        return f"nombre: {self.nombre}, nacionalidad: {self.nacionalidad}\n"
    def __repr__(self):
        return self.__str__()
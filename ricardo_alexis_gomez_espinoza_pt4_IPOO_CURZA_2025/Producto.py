

class Producto:
    def __init__(self, nombre, precio, categoria):
        if not nombre:
            raise ValueError("El nombre del producto no puede estar vacío.") 
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'precio': self.precio,
            'categoria': self.categoria
        }


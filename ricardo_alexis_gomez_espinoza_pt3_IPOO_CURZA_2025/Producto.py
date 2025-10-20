


class Producto:
    iva = 0.21

    def __init__(self, nombre, precio):
        self.nombre = nombre  
        self.precio = precio  

    @classmethod  
    def actualizar_iva(cls, nuevo_valor):
        cls.iva = nuevo_valor 
        print(f"IVA actualizado globalmente a {cls.iva}")

    @staticmethod  
    def calcular_precio_final(precio_base):
        precio_final = precio_base * (1 + Producto.iva) 
        return precio_final


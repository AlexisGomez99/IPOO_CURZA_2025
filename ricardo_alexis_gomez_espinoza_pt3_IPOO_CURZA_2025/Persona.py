


class Persona:
    contador = 0 

    def __init__(self, nombre="Desconocido"):
        Persona.contador += 1 
        self.nombre = nombre

    @classmethod 
    def mostrar_total(cls):
        print(f"Total de personas creadas: {cls.contador}")

    @staticmethod
    def es_mayor_de_edad(edad):
        return edad >= 18

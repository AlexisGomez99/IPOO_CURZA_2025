

class Jugador:

    def __init__(self, nombre, fechaDeNacimiento, equipo, altura, dni, puntosTotales):
        self.dni = dni
        self.nombre = nombre
        self.fechaDeNacimiento = fechaDeNacimiento
        self.altura = altura
        self.equipo = equipo
        self.puntosTotales = puntosTotales
    
    def __str__(self):
        return f"Jugador(nombre={self.nombre}, fecha_nacimiento={self.fechaDeNacimiento}, equipo={self.equipo}, altura={self.altura}, DNI={self.dni}, puntos={self.puntosTotales})"

    def __repr__(self):
        return self.__str__()
    
    

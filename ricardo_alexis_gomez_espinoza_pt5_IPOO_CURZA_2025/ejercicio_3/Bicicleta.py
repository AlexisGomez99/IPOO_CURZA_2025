from Transporte import Transporte

class Bicicleta(Transporte):
    def __init__(self, velocidad_maxima, capacidad):
        super().__init__(velocidad_maxima, capacidad)

    def mover(self, distancia):
        print(f"Bicicleta: Recorrido de {distancia}km completado")
        return True

    def esta_operativo(self):
        return True
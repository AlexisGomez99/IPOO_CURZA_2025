from Transporte import Transporte
from Combustible import Combustible

class Avion(Transporte, Combustible):
    def __init__(self, velocidad_maxima, capacidad, consumo_km):
        super().__init__(velocidad_maxima, capacidad)
        self._litros_disponibles = 0.0 
        self._consumo_km = consumo_km

    def cargar_combustible(self, litros):
        if litros > 0:
            self._litros_disponibles += litros
            print(f"Avión: Se cargaron {litros}L. Total disponible: {self._litros_disponibles}L.")

    def consumo_por_km(self):
        return self._consumo_km

    def mover(self, distancia):
        litros_necesarios = distancia * self.consumo_por_km()
        
        if litros_necesarios <= self._litros_disponibles:
            self._litros_disponibles -= litros_necesarios 
            print(f"Avión: Vuelo de {distancia}km completado. Consumo: {litros_necesarios}L. Combustible restante: {self._litros_disponibles}L.")
            return True
        else:
            print(f"Avión: No se puede completar el vuelo de {distancia}km. Faltan {(litros_necesarios - self._litros_disponibles)}L de combustible.")
            return False

    def esta_operativo(self):
        return self._litros_disponibles > 0
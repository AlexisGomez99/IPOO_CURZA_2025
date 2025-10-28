from Animal import Animal
from Domesticable import Domesticable

class Perro(Animal, Domesticable):
    def hacer_sonido(self):
        return "Guau"

    def entrenar(self):
        if self._energia >= self.ENERGIA_ENTRENAR:
            print(f"{self.nombre} está siendo entrenado. -{self.ENERGIA_ENTRENAR} energía.")
            self._energia -= self.ENERGIA_ENTRENAR
        else:
            print(f"{self.nombre} no tiene suficiente energía para entrenar (Energía: {self._energia}).")
from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, velocidad_maxima, capacidad):
        self._velocidad_maxima = velocidad_maxima
        self._capacidad = capacidad

    @abstractmethod
    def mover(self, distancia):
        pass

    @abstractmethod
    def esta_operativo(self):
        pass
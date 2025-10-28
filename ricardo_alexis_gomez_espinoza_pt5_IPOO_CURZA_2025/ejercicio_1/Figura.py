from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self, color):
        self._color = color

    def cambiar_color(self, nuevo_color):
        self._color = nuevo_color
        print(f"El color de la figura ha cambiado a {self._color}.")

    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

    
from ricardo_alexis_gomez_espinoza_pt5_IPOO_CURZA_2025.ejercicio_1.Figura import Figura
import math

class Circulo(Figura):

    def __init__(self, radio, color):
        super().__init__(color)
        self._radio = self._validar_positivo(radio, "radio")

    def _validar_positivo(self, valor, nombre_attr):
        if valor <= 0:
            raise ValueError(f"Error: El {nombre_attr} debe ser un valor positivo.")
        return valor
    
    def calcular_area(self):
        return math.pi * (self._radio ** 2)
    
    def calcular_perimetro(self):
        return 2 * math.pi * self._radio
    
    def __str__(self):
        return f"Círculo (Color: {self._color}, Radio: {self._radio})"
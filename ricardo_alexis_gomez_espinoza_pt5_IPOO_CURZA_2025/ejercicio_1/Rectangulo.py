from ricardo_alexis_gomez_espinoza_pt5_IPOO_CURZA_2025.ejercicio_1.Figura import Figura

class Rectangulo(Figura):

    def __init__(self, base, altura, color):
        super().__init__(color)
        self._base = self._validar_positivo(base, "base")
        self._altura = self._validar_positivo(altura, "altura")

    def _validar_positivo(self, valor, nombre_attr):
        if valor <= 0:
            raise ValueError(f"Error: El {nombre_attr} debe ser un valor positivo.")
        return valor
    
    def calcular_area(self):
        return self._base * self._altura
    
    def calcular_perimetro(self):
        return 2 * (self._base + self._altura)

    def __str__(self):
        return f"Rectángulo (Color: {self._color}, Largo: {self._base}, Ancho: {self._altura})"
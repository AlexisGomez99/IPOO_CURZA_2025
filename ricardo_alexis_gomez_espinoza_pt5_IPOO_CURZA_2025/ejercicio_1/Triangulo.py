from ricardo_alexis_gomez_espinoza_pt5_IPOO_CURZA_2025.ejercicio_1.Figura import Figura

class Triangulo(Figura):
    def __init__(self, base, altura, lado2, lado3, color):
        super().__init__(color)
        self._base = self._validar_positivo(base, "base")
        self._altura = self._validar_positivo(altura, "altura")
        self._lado2 = self._validar_positivo(lado2, "lado 2")
        self._lado3 = self._validar_positivo(lado3, "lado 3")

    def _validar_positivo(self, valor, nombre_attr):
        if valor <= 0:
            raise ValueError(f"Error: El {nombre_attr} debe ser un valor positivo.")
        return valor

    def calcular_area(self):
        return (self._base * self._altura) / 2

    def calcular_perimetro(self):
        return self._base + self._lado2 + self._lado3

    def __str__(self):
        return f"Triángulo (Color: {self._color}, Base: {self._base}, Altura: {self._altura})"
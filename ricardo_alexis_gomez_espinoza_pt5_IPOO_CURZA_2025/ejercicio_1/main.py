from ricardo_alexis_gomez_espinoza_pt5_IPOO_CURZA_2025.ejercicio_1.Circulo import Circulo
from ricardo_alexis_gomez_espinoza_pt5_IPOO_CURZA_2025.ejercicio_1.Triangulo import Triangulo
from ricardo_alexis_gomez_espinoza_pt5_IPOO_CURZA_2025.ejercicio_1.Rectangulo import Rectangulo


def figura_con_mayor_area(lista_figuras):
        if not lista_figuras:
            return "La lista de figuras está vacía."

        max_area = -1
        figura_mayor = None

        for figura in lista_figuras:
            area_actual = figura.calcular_area()
            if area_actual > max_area:
                max_area = area_actual
                figura_mayor = figura

        print("\n--- Figura con Mayor Área ---")
        print(f"La figura con mayor área es: {figura_mayor}")
        print(f"Área: {max_area}")
        return figura_mayor


try:
    circulo1 = Circulo(radio=5, color="azul")
    rectangulo1 = Rectangulo(base=4, altura=10, color="rojo")
    triangulo1 = Triangulo(base=6, altura=8, lado2=10, lado3=8, color="verde") 

    figuras = [circulo1, rectangulo1, triangulo1]

    for fig in figuras:
        print(f"\n{fig}")
        print(f"Área: {fig.calcular_area()}")
        print(f"Perímetro: {fig.calcular_perimetro()}")
        if fig == circulo1:
            fig.cambiar_color("amarillo")
    figura_con_mayor_area(figuras)

except ValueError as e:
    print(e)
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
from Arma import Arma
class Espada (Arma):
    def __init__(self, tipo, puntos_fuerza, puntos_resistencia, usa_mana, ventajas_sobre):
        super().__init__(tipo, puntos_fuerza, puntos_resistencia, usa_mana, ventajas_sobre)
        self.__gemas = []

    def set_gemas(self,gemas):
        self.__gemas = gemas

    def nueva_gema(self, gema):
        self.__gemas.append(gema)
    def eliminar_gema(self,gema):
        self.__gemas.remove(gema)

    def get_gemas(self):
        return self.__gemas
    
    def __str__(self):
        return f"\nClase: Espada\n{super().__str__()}\nGemas: {self.__gemas} "
    def __repr__(self):
        return self.__str__()
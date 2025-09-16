from Arma import Arma

class Arco (Arma):
    def __init__(self, tipo, puntos_fuerza, puntos_resistencia, usa_mana, ventajas_sobre, cantidad_flechas):
        super().__init__(tipo, puntos_fuerza, puntos_resistencia, usa_mana, ventajas_sobre)
        self.__cantidad_flechas = cantidad_flechas

    def set_cantidad_flechas(self, cantidad_flechas):
        self.__cantidad_flechas = cantidad_flechas

    def get_cantidad_flechas(self):
        return self.__cantidad_flechas
    
    def __str__(self):
        return f"\nClase: Arco\nNombre: {self._Arma__nombre}\nTipo: {self._Arma__tipo}\nPuntos de fuerza: {self._Arma__puntos_fuerza}\nPuntos de resistencia: {self._Arma__puntos_resistencia}\nUsa mana: {self._Arma__usa_mana}\nVentajas sobre: {self._Arma__ventajas_sobre}\nCantidad de flechas: {self.__cantidad_flechas} "
    
    def __repr__(self):
        return self.__str__()
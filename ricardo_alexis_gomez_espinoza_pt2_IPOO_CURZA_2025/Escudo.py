from Arma import Arma

class Escudo (Arma):
    def __init__(self, tipo, puntos_fuerza, puntos_resistencia, usa_mana, ventajas_sobre,aumento_resistencia):
        super().__init__(tipo, puntos_fuerza, puntos_resistencia, usa_mana, ventajas_sobre)
        self.__aumento_resistencia = aumento_resistencia

    def set_aumento_resistencia(self, aumento_resistencia):
        self.__aumento_resistencia = aumento_resistencia

    def get_aumento_resistencia(self):
        self.__aumento_resistencia

    def __str__(self):
        return f"\nClase: Escudo\nNombre: {self._Arma__nombre}\nTipo: {self._Arma__tipo}\nPuntos de fuerza: {self._Arma__puntos_fuerza}\nPuntos de resistencia: {self._Arma__puntos_resistencia}\nUsa mana: {self._Arma__usa_mana}\nVentajas sobre: {self._Arma__ventajas_sobre}\nAumento de resistencia: {self.__aumento_resistencia} "
    
    def __repr__(self):
        return self.__str__()


from Personaje import Personaje


class Elfo (Personaje):
    def __init__ (self, nombre, puntos_vida, puntos_ataque, puntos_defensa, elemento:str = "Sin elemento"):
        super().__init__(nombre, puntos_vida, puntos_ataque, puntos_defensa,elemento)
        self.mana = 0
        self.puntos_regeneracion = 0 
    
    def set_mana(self,mana):
        self.mana = mana
    def set_puntos_regeneracion(self, puntos_regeneracion):
        self.puntos_regeneracion = puntos_regeneracion

    def get_mana(self):
        return self.mana
    def get_puntos_regeneracion(self):
        return self.puntos_regeneracion 



    def __str__(self):
        return f"\nPersonaje: Elfo. \n{super().__str__()}\nMana: {self.mana}\nPuntos de Regeneracion: {self.puntos_regeneracion}\n"
    def __repr__(self):
        return self.__str__()
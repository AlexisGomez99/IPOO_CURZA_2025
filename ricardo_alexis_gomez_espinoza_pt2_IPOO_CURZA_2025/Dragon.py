

from Personaje import Personaje


class Dragon (Personaje):
    def __init__ (self, nombre, puntos_vida, puntos_ataque, puntos_defensa, elemento:str = "Fuego"):
        super().__init__(nombre, puntos_vida, puntos_ataque, puntos_defensa,elemento)
        self.mana = 0

    def set_mana(self,mana):
        self.mana = mana

    def get_mana(self):
        return self.mana
        

    def __str__(self):
        return f"\nPersonaje: Dragon. \n{super().__str__()}\nMana: {self.mana}"
    def __repr__(self):
        return self.__str__()
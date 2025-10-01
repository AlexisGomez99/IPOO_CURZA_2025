from Personaje import Personaje


class Guerrero (Personaje):
    def __init__ (self, nombre, puntos_vida, puntos_ataque, puntos_defensa, elemento:str = "Sin elemento"):
        super().__init__(nombre, puntos_vida, puntos_ataque, puntos_defensa, elemento)
        self.armadura = 0

    def set_armadura(self,armadura):
        self.armadura = armadura
    def get_armadura(self):
        return self.armadura



    def __str__(self):
        return f"\nPersonaje: Guerrero. \n{super().__str__()}\nElemento: {self.elemento}\nArmadura: {self.armadura}"
    def __repr__(self):
        return self.__str__()
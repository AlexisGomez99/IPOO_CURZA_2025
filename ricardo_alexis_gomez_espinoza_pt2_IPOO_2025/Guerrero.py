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
        return f"\nPersonaje: Guerrero. \nNombre: {self.nombre} \nPuntos de Vida: {self.puntos_vida}\nPuntos de Ataque: {self.puntos_ataque}\nElemento: {self.elemento}\nPuntos de Defensa: {self.puntos_defensa}\nArmadura: {self.armadura}\nHabilidades: {self.habilidades}\nDebilidades: {self.debilidades}"

    def __repr__(self):
        return self.__str__()
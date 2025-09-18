

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
        return f"\nPersonaje: Dragon. \nNombre: {self.nombre} \nPuntos de Vida: {self.puntos_vida}\nPuntos de Ataque: {self.puntos_ataque}\nPuntos de Defensa: {self.puntos_defensa}\nMana: {self.mana}\nHabilidades: {self.habilidades}\nDebilidades: {self.debilidades}"

    def __repr__(self):
        return self.__str__()
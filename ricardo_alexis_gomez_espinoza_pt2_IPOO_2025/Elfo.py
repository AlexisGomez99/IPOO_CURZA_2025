

from Personaje import Personaje


class Elfo (Personaje):
    def __init__ (self, nombre, puntos_vida, puntos_ataque, puntos_defensa, elemento:str = "Sin elemento"):
        super().__init__(nombre, puntos_vida, puntos_ataque, puntos_defensa,elemento)
        self.mana = 0
    
    def set_mana(self,mana):
        self.mana = mana
    def set_puntos_regeneracion(self, puntos_regeneracion):
        self.puntos_regeneracion = puntos_regeneracion

    def get_mana(self):
        return self.mana
    def get_puntos_regeneracion(self):
        return self.puntos_regeneracion 



    def __str__(self):
        return f"\nPersonaje: Elfo. \nNombre: {self.nombre} \nPuntos de Vida: {self.puntos_vida}\nPuntos de Ataque: {self.puntos_ataque}\nPuntos de Defensa: {self.puntos_defensa}\nMana: {self.mana}\nPuntos de Regeneracion: {self.puntos_regeneracion}\nHabilidades: {self.habilidades}\nDebilidades: {self.debilidades}"

    def __repr__(self):
        return self.__str__()
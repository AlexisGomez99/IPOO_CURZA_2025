

class Personaje:
    
    
    def __init__(self, nombre, puntos_vida, puntos_ataque, puntos_defensa, elemento):
        self.nombre = nombre
        self.puntos_ataque = puntos_ataque
        self.puntos_defensa = puntos_defensa
        self.puntos_vida = puntos_vida
        self.elemento = elemento
        self.habilidades = []
        self.debilidades = []
        

    def set_elemento(self,elemento):
        self.elemento = elemento
    def set_puntos_ataque(self, ataque):
        self.puntos_ataque = ataque
    def set_puntos_vida(self, puntos_vida):
        self.puntos_vida = puntos_vida
    def set_puntos_defensa(self, puntos_defensa):
        self.puntos_defensa = puntos_defensa
    def set_nombre(self, nombre):
        self.nombre = nombre
    def nueva_habilidad(self,habilidad)->str:
        self.habilidades.append(habilidad)
    def nueva_debilidad(self,debilidad)->str:
        self.debilidades.append(debilidad)

    def eliminar_habilidad(self,habilidad):
        self.habilidades.remove(habilidad)
    def eliminar_debilidad(self,debilidad):
        self.debilidades.remove(debilidad)

    def get_habilidades(self):
        return self.habilidades
    def get_debilidades(self):
        return self.debilidades
    def get_elemento(self):
        return self.elemento
    def get_puntos_ataque(self):
        return self.puntos_ataque
    def get_puntos_vida(self)->str:
        return self.puntos_vida
    def get_puntos_defensa(self)->str:
        return self.puntos_defensa
    def get_nombre(self)->str:
        return self.nombre 

    def atacar(self):
        return self.puntos_ataque
    
    def defensa(self, daño):
        sigue_vivo= False

        if self.puntos_vida > 1:
            self.puntos_vida = self.puntos_vida - daño
            sigue_vivo= True

        return sigue_vivo
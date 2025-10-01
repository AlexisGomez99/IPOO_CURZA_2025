from Arma import Arma
from ManejadorDeArma import ManejadorDeArma

class Personaje:
    
    
    def __init__(self, nombre, puntos_vida, puntos_ataque, puntos_defensa, elemento):
        self.nombre = nombre
        self.puntos_ataque = puntos_ataque
        self.puntos_defensa = puntos_defensa
        self.puntos_vida = puntos_vida
        self.elemento = elemento
        self.habilidades = []
        self.debilidades = []
        self.arsenal:Arma = []
        

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
    def set_arsenal(self, arsenal):
        self.arsenal = arsenal

    def agregar_arma(self, arma:Arma):
        if len(self.arsenal) < 5:
            if all(a.get_nombre() != arma.get_nombre() for a in self.arsenal):
                self.arsenal.append(arma)
            else:
                print(f"El arma {arma.get_nombre()} ya está en el arsenal.")
        else:
            print("Arsenal lleno.")
            
    def agregar_habilidad(self,habilidad):
        self.habilidades.append(habilidad)
    def agregar_debilidad(self,debilidad):
        self.debilidades.append(debilidad)

    def eliminar_arma(self, arma):
        self.arsenal.remove(arma) ## se debe establecer un compareTo
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
    def get_puntos_vida(self):
        return self.puntos_vida
    def get_puntos_defensa(self):
        return self.puntos_defensa
    def get_nombre(self):
        return self.nombre 
    def get_arsenal(self):
        return self.arsenal
    def atacar(self):
        daño_realizado = self.puntos_ataque
        for arma in  self.arsenal:
            if arma.get_tipo() == "OFENSIVO":
                daño_realizado += arma.atacar()
        return daño_realizado
    
    def defensa(self, daño):
        sigue_vivo= False

        if self.puntos_vida > 1:
            for arma in self.arsenal:
                if arma.get_tipo() == "DEFENSIVO":
                    self.puntos_defensa += arma.atacar() #Consultar
                    self.puntos_vida = self.puntos_vida - daño
                    sigue_vivo= True

        return sigue_vivo
    
    def __str__(self):
        return f"\nNombre: {self.nombre} \nPuntos de Vida: {self.puntos_vida}\nPuntos de Ataque: {self.puntos_ataque}\nPuntos de Defensa: {self.puntos_defensa}\Habilidades: {self.habilidades}\nDebilidades: {self.debilidades}\nArmas: {self.arsenal}"
    def __repr__(self):
        return self.__str__()
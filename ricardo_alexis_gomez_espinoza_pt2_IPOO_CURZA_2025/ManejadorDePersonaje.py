from Personaje import Personaje
from ManejadorDeArma import ManejadorDeArma

class ManejadorDePersonaje:
    cantidad_de_personajes = 10
    cantidad_armas = 5
    def __init__(self):
        self.lista_de_personajes = []
        self.manejador_de_armas = ManejadorDeArma()

    
    def crear_personaje_aleatorio(self)-> Personaje:
        pass

    def configurar_arsenal(self):
        for p in self.lista_de_personajes:
            self.manejador_de_armas.crear_armas()
            p.set_arsenal(self.manejador_de_armas.lista_de_armas)
            self.manejador_de_armas.vaciar_arsenal()
        

    def crear_personajes(self):
        while len(self.lista_de_personajes) <=10:
            personaje = self.crear_personaje_aleatorio()
            if all(p.get_nombre() != personaje.get_nombre() for p in self.lista_de_personajes):
                self.lista_de_personajes.append(personaje)
            else:
                print(f"El Personaje {personaje.get_nombre()} ya está creado.")
    
    def listar_personajes(self):
        return self.lista_de_personajes
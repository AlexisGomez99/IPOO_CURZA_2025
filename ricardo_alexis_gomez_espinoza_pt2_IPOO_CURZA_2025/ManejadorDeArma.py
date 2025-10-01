from Arma import Arma
from Espada import Espada
from Escudo import Escudo
from Arco import Arco
from LectorCSV import LectorCSV
import random
import re

class ManejadorDeArma:
    cantidad_armas = 5
    def __init__(self):
        self.lista_de_armas = []
        self.lector_csv = LectorCSV()

    def crear_arma_aleatoria(self)-> Arma: # Crear Arma aleatoria
        tipo = random.randint(1,3)
        lista_prefijo = self.lector_csv.CSV_to_list("./prefijos.csv")
        lista_base = self.lector_csv.CSV_to_list("./base.csv")

        nombre = str(random.choice(lista_prefijo))+" "+ str(random.choice(lista_base))
        nombre = nombre.replace("[", "")
        nombre = nombre.replace("]", "")
        nombre = nombre.replace("'", "")

        match tipo:
            case 1:
                espada = Espada("OFENSIVO",10,0,"No","Dragon")
                espada.set_nombre(nombre)
                return espada
            case 2:
                arco = Arco("OFENSIVO",5,0,"No","Dragon", 100)
                arco.set_nombre(nombre)
                return arco
            case _: 
                escudo = Escudo("DEFENSIVO",15,100,"No","Elfo", 1)
                escudo.set_nombre(nombre)
                return escudo


    def listar_armas(self):
        return self.lista_de_armas
    
    def crear_armas(self):
        while len(self.lista_de_armas) <= 5:
            self.lista_de_armas.append(self.crear_arma_aleatoria())
        
    def vaciar_arsenal(self):
        self.lista_de_armas.clear()
        
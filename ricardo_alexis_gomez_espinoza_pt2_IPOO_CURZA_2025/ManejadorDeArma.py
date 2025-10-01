from Arma import Arma

class ManejadorDeArma:
    cantidad_armas = 5
    def __init__(self):
        self.lista_de_armas = []

    def crear_arma_aleatoria():
        pass

    def listar_armas(self):
        return self.lista_de_armas
    
    def crear_armas(self):
        while len(self.lista_de_armas) <= 5:
            self.lista_de_armas.append(self.crear_arma_aleatoria())
        
    def vaciar_arsenal(self):
        self.lista_de_armas.clear()
        
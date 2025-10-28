from abc import ABC, abstractmethod

class Combustible(ABC):
    
    @abstractmethod
    def cargar_combustible(self, litros):
        pass
    
    @abstractmethod
    def consumo_por_km(self):
        pass
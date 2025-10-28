from abc import ABC, abstractmethod

class Bonificable(ABC):
    @abstractmethod
    def calcular_bono(self):
        pass


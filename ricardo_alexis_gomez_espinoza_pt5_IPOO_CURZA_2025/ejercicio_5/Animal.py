from abc import ABC, abstractmethod

class Animal(ABC):
    ENERGIA_ENTRENAR = 10
    ENERGIA_ALIMENTAR = 20

    def __init__(self, nombre, edad, energia=50):
        self._nombre = nombre
        self._edad = edad
        self._energia = energia

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def energia(self):
        return self._energia

    def alimentar(self):
        print(f"{self.nombre} está siendo alimentado. Energía antes: {self._energia}")
        self._energia += self.ENERGIA_ALIMENTAR
        print(f"Energía después: {self._energia}")

    @abstractmethod
    def hacer_sonido(self):
        pass
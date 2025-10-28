from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, dni):
        self._nombre = nombre
        self._dni = dni

    @property
    def nombre(self):
        return self._nombre
    
    @abstractmethod
    def calcular_sueldo(self):
        pass
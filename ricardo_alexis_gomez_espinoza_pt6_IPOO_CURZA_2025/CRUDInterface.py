from abc import ABC, abstractmethod

class CRUDInterface(ABC):
    
    @abstractmethod
    def crear(self):
        pass

    @staticmethod
    @abstractmethod
    def leer(self):
        pass

    @staticmethod
    @abstractmethod
    def leer_uno(id:int):
        pass

    @abstractmethod
    def actualizar(self):
        pass

    @staticmethod
    @abstractmethod
    def eliminar(id:int):
        pass
from abc import ABC, abstractmethod

class Comprobante(ABC):
    def __init__(self, detalles_compra, monto_final):
        self._detalles_compra = detalles_compra
        self._monto_final = monto_final

    @abstractmethod
    def generar_comprobante(self):
        pass
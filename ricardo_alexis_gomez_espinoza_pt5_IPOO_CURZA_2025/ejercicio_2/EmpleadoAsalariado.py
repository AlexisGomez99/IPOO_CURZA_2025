from Empleado import Empleado
from Bonificable import Bonificable


class EmpleadoAsalariado(Empleado, Bonificable):
    
    def __init__(self, nombre, dni, sueldo_fijo):
        super().__init__(nombre, dni)
        self._sueldo_fijo = sueldo_fijo

    def calcular_sueldo(self):
        return self._sueldo_fijo

    def calcular_bono(self):
        return self._sueldo_fijo * 0.10
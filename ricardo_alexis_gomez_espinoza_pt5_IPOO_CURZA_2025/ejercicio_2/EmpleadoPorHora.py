from Empleado import Empleado
from Bonificable import Bonificable

class EmpleadoPorHora(Empleado, Bonificable):
    BONO_HORAS_MIN = 160
    BONO_PORCENTAJE = 0.05
    
    def __init__(self, nombre, dni, valor_hora, horas_trabajadas):
        super().__init__(nombre, dni)
        self._valor_hora = valor_hora
        self._horas_trabajadas = horas_trabajadas

    def calcular_sueldo(self):
        return self._valor_hora * self._horas_trabajadas
    
    def calcular_bono(self):
        if self._horas_trabajadas > self.BONO_HORAS_MIN:
            return self.calcular_sueldo() * self.BONO_PORCENTAJE
        return 0.0
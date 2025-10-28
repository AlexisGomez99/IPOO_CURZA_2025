from MetodoPago import MetodoPago

class PagoCripto(MetodoPago):
    COMISION_FIJA = 2.0
    def procesar_pago(self, monto):
        if not self._validar_monto(monto):
            return None, False
        monto_final = monto + self.COMISION_FIJA
        comision = self.COMISION_FIJA
        return monto_final, True

    def _validar_monto(self, monto):
        if monto <= 0:
            print("ERROR: El monto a pagar debe ser positivo.")
            return False
        return True

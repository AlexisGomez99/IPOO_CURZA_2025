from MetodoPago import MetodoPago

class PagoTarjeta(MetodoPago):
    RECARGO = 0.05
    def procesar_pago(self, monto):
        if not self._validar_monto(monto):
            return None, False
        monto_final = monto * (1 + self.RECARGO)
        recargo = monto_final - monto
        return monto_final, True

    def _validar_monto(self, monto):
        if monto <= 0:
            print("ERROR: El monto a pagar debe ser positivo.")
            return False
        return True
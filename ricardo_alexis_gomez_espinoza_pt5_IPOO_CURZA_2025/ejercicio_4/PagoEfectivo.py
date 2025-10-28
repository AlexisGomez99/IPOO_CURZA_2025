from MetodoPago import MetodoPago

class PagoEfectivo(MetodoPago):
    DESCUENTO = 0.10
    def procesar_pago(self, monto):
        if not self._validar_monto(monto):
            return None, False
        monto_final = monto * (1 - self.DESCUENTO)
        descuento = monto - monto_final
        return monto_final, True

    def _validar_monto(self, monto):
        if monto <= 0:
            print("ERROR: El monto a pagar debe ser positivo.")
            return False
        return True
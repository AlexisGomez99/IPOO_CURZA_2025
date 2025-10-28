from Comprobante import Comprobante


class Recibo(Comprobante):
    def generar_comprobante(self):
        print("\n--- RECIBO GENERADO ---")
        print("Tipo: Comprobante de Ingreso")
        print(f"Detalle de Compra: {self._detalles_compra}")
        print(f"Monto Total Recibido: {self._monto_final:.2f} UM")
        print("Documento no válido como crédito fiscal.")
        print("------------------------")
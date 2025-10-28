from Comprobante import Comprobante

class Factura(Comprobante):
    def generar_comprobante(self):
        print("\n--- FACTURA GENERADA ---")
        print("Tipo: Venta de Bienes/Servicios")
        print(f"Detalle de Compra: {self._detalles_compra}")
        print(f"Total a Pagar (Final): {self._monto_final:.2f} UM")
        print("IVA discriminado al 21%")
        print("------------------------")
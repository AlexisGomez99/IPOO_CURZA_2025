from PagoCripto import PagoCripto
from PagoEfectivo import PagoEfectivo
from PagoTarjeta import PagoTarjeta
from Factura import Factura
from Recibo import Recibo

monto_base_compra1 = 100.0
monto_base_compra2 = 50.0
monto_base_compra3 = 200.0


pago_tarjeta = PagoTarjeta()
pago_efectivo = PagoEfectivo()
pago_cripto = PagoCripto()

print(f"\nCompra 1: Monto Base ${monto_base_compra1} - Pago con Tarjeta")
monto_final1, exito1 = pago_tarjeta.procesar_pago(monto_base_compra1)
if exito1:
    print(f"Total Final (con 5% Recargo): ${monto_final1:.2f}")
    comprobante1 = Factura("Productos electrónicos", monto_final1)
    comprobante1.generar_comprobante()

print(f"\nCompra 2: Monto Base ${monto_base_compra2:.2f} - Pago en Efectivo")
monto_final2, exito2 = pago_efectivo.procesar_pago(monto_base_compra2)
if exito2:
    print(f"Total Final (con 10% Descuento): ${monto_final2:.2f}")
    comprobante2 = Recibo("Libros y papelería", monto_final2)
    comprobante2.generar_comprobante()

print(f"\nCompra 3: Monto Base ${monto_base_compra3} - Pago con Cripto")
monto_final3, exito3 = pago_cripto.procesar_pago(monto_base_compra3)
if exito3:
    print(f"Total Final (con $2.0 Comisión): ${monto_final3}")
    comprobante3 = Factura("Suscripción de software", monto_final3)
    comprobante3.generar_comprobante()

print("\n--- Validación de Monto ---")
pago_efectivo.procesar_pago(0)
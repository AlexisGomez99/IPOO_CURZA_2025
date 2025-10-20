from Persona import Persona
from ConversorTemperatura import ConversorTemperatura
from Producto import Producto
from UtilidadesFecha import UtilidadesFecha
from Usuario import Usuario
from Empleado import Empleado

# Pruebas Persona
p1 = Persona("Ana")
p2 = Persona("Luis")
p3 = Persona("Carlos")

Persona.mostrar_total()

print(f"¿Ana es mayor de edad (25)? {Persona.es_mayor_de_edad(25)}")
print(f"¿Pedro es mayor de edad (16)? {Persona.es_mayor_de_edad(16)}") 

# Pruebas ConversorTemperatura
celsius = 25
fahrenheit = ConversorTemperatura.celsius_a_fahrenheit(celsius)
print(f"{celsius}°C son {fahrenheit:.2f}°F")

fahrenheit_test = 212
celsius_convertido = ConversorTemperatura.fahrenheit_a_celsius(fahrenheit_test)
print(f"{fahrenheit_test}°F son {celsius_convertido:.2f}°C")

# Pruebas Producto
producto_base = 100
precio_1 = Producto.calcular_precio_final(producto_base)
print(f"Precio con IVA (0.21) de {producto_base}: {precio_1:.2f}") 

Producto.actualizar_iva(0.10) 

precio_2 = Producto.calcular_precio_final(producto_base)
print(f"Precio con nuevo IVA (0.10) de {producto_base}: {precio_2:.2f}") 

# Pruebas UtilidadesFecha
print(f"Fecha actual: {UtilidadesFecha.fecha_actual()}")

print(f"¿2024 es bisiesto? {UtilidadesFecha.es_bisiesto(2024)}")
print(f"¿1900 es bisiesto? {UtilidadesFecha.es_bisiesto(1900)}") 
print(f"¿2000 es bisiesto? {UtilidadesFecha.es_bisiesto(2000)}")

# Pruebas Usuario
Usuario.registrar_usuario("Elena", "elena@ejemplo.com") 
Usuario.registrar_usuario("Juan", "juan.ejemplo.com") 
Usuario.registrar_usuario("Maria", "maria@test.net") 

Usuario.mostrar_usuarios()

#Pruebas Empleado
empleado1 = Empleado("Ricardo Gomez", "Desarrollador Senior", 75000)  # cite: 51

print("Datos antes de atributo dinámico:")
empleado1.mostrar_datos()

empleado1.bono = 5000  

print("Datos después de atributo dinámico:")
empleado1.mostrar_datos()  


tiene_bono_instancia = hasattr(empleado1, 'bono')
tiene_bono_clase = hasattr(Empleado, 'bono') 

print(f"\nVerificación con hasattr():")
print(f"¿La instancia 'empleado1' tiene el atributo 'bono'? {tiene_bono_instancia}") 
print(f"¿La CLASE 'Empleado' tiene el atributo 'bono'? {tiene_bono_clase}") 
from Auto import Auto
from Avion import Avion
from Bicicleta import Bicicleta
import random

auto1 = Auto(velocidad_maxima=180, capacidad=5, consumo_km=0.1)  
avion1 = Avion(velocidad_maxima=900, capacidad=300, consumo_km=10.0) 
bici1 = Bicicleta(velocidad_maxima=30, capacidad=1)

transportes = [auto1, avion1, bici1]

print("\n--- Carga Inicial ---")
auto1.cargar_combustible(20)
avion1.cargar_combustible(1000)

print("\n--- Simulación de Movimiento ---")
for t in transportes:
    distancia = random.randint(10, 250)
    print(f"\nSimulando movimiento para {t.__class__.__name__} por {distancia}km...")
    
    if t.esta_operativo():
        t.mover(distancia)
    else:
        print(f"{t.__class__.__name__} no está operativo (sin combustible o en estado desconocido).")
        

print("\n--- Verificación Operativa ---")
auto1.mover(300) 
print(f"¿Avión operativo?: {avion1.esta_operativo()}")
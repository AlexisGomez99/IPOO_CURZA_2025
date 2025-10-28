from Gato import Gato
from Perro import Perro
from Leon import Leon
from Domesticable import Domesticable

def animal_con_mayor_energia(lista_animales):
    if not lista_animales:
        return "La lista de animales está vacía."

    max_energia = -1
    animal_mayor = None

    for animal in lista_animales:
        if animal.energia > max_energia:
            max_energia = animal.energia
            animal_mayor = animal
    
    print("\n--- Animal con Mayor Energía ---")
    print(f"El animal con mayor energía es: {animal_mayor.nombre} (Energía: {animal_mayor.energia})")
    return animal_mayor


print("\n--- EJERCICIO 5: Sistema de Animales en un Zoológico ---")

perro1 = Perro("Fido", 3, 60)
gato1 = Gato("Mishi", 5, 20)
leon1 = Leon("Simba", 7, 80)
perro2 = Perro("Toby", 2, 40)

animales = [perro1, gato1, leon1, perro2]

print("\n--- Sonidos y Entrenamiento ---")
for animal in animales:
    print(f"\n{animal.nombre} ({animal.__class__.__name__}): {animal.hacer_sonido()}")
    

    if isinstance(animal, Domesticable):
        animal.entrenar()
    else:
        print(f"{animal.nombre} no es domesticable y no puede ser entrenado.")
        
print("\n--- Simulación de Alimentación ---")
perro1.alimentar()
gato1.alimentar()
leon1.alimentar() 

print("\n--- Segundo Intento de Entrenamiento ---")
gato1.entrenar()

animal_con_mayor_energia(animales)
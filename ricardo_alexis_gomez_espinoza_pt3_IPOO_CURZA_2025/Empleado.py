


class Empleado:
    empresa = "TechGlobal"

    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario 

   
    def mostrar_datos(self):  
        print("\n--- Datos del Empleado ---")
        print(f"Nombre: {self.nombre}")
        print(f"Puesto: {self.puesto}")
        print(f"Salario: {self.salario}")
        print(f"Empresa: {Empleado.empresa}")
        
        
        if hasattr(self, 'bono'):
            print(f"Bono (Atributo Dinámico): {self.bono}") 
        print("--------------------------")


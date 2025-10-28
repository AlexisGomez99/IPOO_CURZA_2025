from EmpleadoAsalariado import EmpleadoAsalariado 
from EmpleadoPorHora import EmpleadoPorHora

def calcular_costo_total_sueldos(lista_empleados):
    costo_total = 0
    for emp in lista_empleados:
        sueldo_base = emp.calcular_sueldo()
        bono = emp.calcular_bono()
        total_a_cobrar = sueldo_base + bono
        costo_total += total_a_cobrar
    return costo_total

emp_asalariado1 = EmpleadoAsalariado("Ana Torres", "12345678A", 50000)
emp_asalariado2 = EmpleadoAsalariado("Luis Gómez", "87654321B", 65000)
emp_porhora1 = EmpleadoPorHora("Marta Ríos", "11223344C", 250, 180) 
emp_porhora2 = EmpleadoPorHora("Pedro Díaz", "44332211D", 250, 150)

empleados = [emp_asalariado1, emp_asalariado2, emp_porhora1, emp_porhora2]

for emp in empleados:
    sueldo_base = emp.calcular_sueldo()
    bono = emp.calcular_bono()
    total_a_cobrar = sueldo_base + bono
    
    print(f"\nEmpleado: {emp.nombre}")
    print(f"  Sueldo Base: ${sueldo_base}")
    print(f"  Bono: ${bono}")
    print(f"  Total a Cobrar: ${total_a_cobrar}")

costo_total = calcular_costo_total_sueldos(empleados)
print(f"\nCosto Total de Sueldos de la Empresa: ${costo_total}")
from Producto import Producto
import csv

def _leer_csv_productos(ruta_csv="./productos.csv"):
    datos_productos = []
    
    try:
        with open(ruta_csv, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file, delimiter=',')
            next(csv_reader) 
            
            for fila in csv_reader:
                if len(fila) < 4:
                    print(f"Fila omitida (datos incompletos): {fila}")
                    continue
                    
                try:
                    nombre = fila[0].strip()
                    descripcion = fila[1].strip()
                    precio = float(fila[2].strip().replace(',', '.')) 
                    stock = int(fila[3].strip())
                    
                    datos_productos.append((nombre, descripcion, precio, stock))
                        
                except ValueError as ve:
                    print(f"Error de conversión de tipo en la fila: {fila}. Error: {ve}")

        return datos_productos

    except FileNotFoundError:
        print(f"Error: Archivo CSV no encontrado en la ruta: {ruta_csv}")
        return []
    except Exception as e:
        print(f"Error general al leer el CSV: {e}")
        return []

def menu_carga_masiva():
    datos_para_insertar = _leer_csv_productos()
    
    if not datos_para_insertar:
        print("No se encontraron datos válidos para la carga.")
        return

    registros_cargados = 0

    for nombre, descripcion, precio, stock in datos_para_insertar:
        nuevo_producto = Producto(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock
        )
        if nuevo_producto.crear():
            registros_cargados += 1
    print(f"Se agregaron {registros_cargados} productos.")

def menu_actualizar_producto():
    try:
        id_actualizar = int(input("Ingrese el ID del producto a actualizar: "))
        producto = Producto.leer_uno(id_actualizar)
        
        if producto:
            print("\nProducto actual:", producto)
            print("Ingrese los nuevos valores (deje vacío para mantener el actual):")
            
            nombre_nuevo = input(f"Nuevo Nombre ({producto.nombre}): ")
            descripcion_nueva = input(f"Nueva Descripción ({producto.descripcion}): ")
            precio_nuevo = input(f"Nuevo Precio ({producto.precio}): ")
            stock_nuevo = input(f"Nuevo Stock ({producto.stock}): ")

            if nombre_nuevo:
                producto.nombre = nombre_nuevo
            if descripcion_nueva:
                producto.descripcion = descripcion_nueva
            if precio_nuevo:
                producto.precio = float(precio_nuevo)
            if stock_nuevo:
                producto.stock = int(stock_nuevo)
            producto.actualizar()

    except ValueError:
        print("Error: El ID, Precio o Stock deben ser números válidos.")
    except Exception as e:
        print(f"Ocurrió un error al actualizar: {e}")

def menu_eliminar_producto():
    try:
        id_eliminar = int(input("Ingrese el ID del producto a ELIMINAR: "))
        Producto.eliminar(id_eliminar)
    except ValueError:
        print("El ID debe ser un número entero.")
    except Exception as e:
        print(f"Ocurrió un error al eliminar: {e}")

def menu_leer_todos():
    print("\n--- Listado de Todos los Productos ---")
    productos = Producto.leer()
    
    if productos:
        for p in productos:
            print(f"{ p.id},{p.nombre}, {p.precio}, {p.stock}, {p.created_at.strftime('%Y-%m-%d %H:%M')}")
    else:
        print("No hay productos para mostrar.")

def menu_crear_producto():
    print("\n--- Crear Nuevo Producto ---")
    try:
        nombre = input("Nombre: ")
        descripcion = input("Descripción: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))

        nuevo_producto = Producto(nombre, descripcion, precio, stock)
        nuevo_producto.crear()

    except ValueError:
        print("Error: Asegúrese de ingresar números válidos para Precio y Stock.")
    except Exception as e:
        print(f"Ocurrió un error al crear el producto: {e}")

def menu_leer_uno():
    try:
        id_buscar = int(input("Ingrese el ID del producto a buscar: "))
        producto = Producto.leer_uno(id_buscar)
        
        if producto:
            print("\n--- DETALLE DEL PRODUCTO ---")
            print(producto)
            print("---------------------------")
        
    except ValueError:
        print("Error: El ID debe ser un número entero.")

def menu_principal():
    while True:
        print("\n====================================")
        print("  SISTEMA DE GESTIÓN DE PRODUCTOS")
        print("====================================")
        print("1. Crear Producto")
        print("2. Leer Todos los Productos")
        print("3. Leer Producto por ID")
        print("4. Actualizar Producto")
        print("5. Eliminar Producto")
        print("6. Ingreso masivo de productos")
        print("0. Salir")
        print("------------------------------------")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            menu_crear_producto()
        elif opcion == '2':
            menu_leer_todos()
        elif opcion == '3':
            menu_leer_uno()
        elif opcion == '4':
            menu_actualizar_producto()
        elif opcion == '5':
            menu_eliminar_producto()
        elif opcion == '6':
            menu_carga_masiva()  # No recuerdo si la carga masiva se hace uno por uno, o con una query se insertan los 30
        elif opcion == '0':
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()
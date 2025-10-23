import json
from Producto import Producto 
from Autor import Autor
from Libro import Libro
from Editorial import Editorial


# Ejercicio 1
producto1 = Producto("Laptop", 1200.50, "Electrónica")
producto2 = Producto("T-shirt", 25.00, "Ropa")
producto3 = Producto("Coffee Maker", 45.99, "Hogar")

productos = [producto1.to_dict(), producto2.to_dict(), producto3.to_dict()]
productos_json = json.dumps(productos, indent=4, ensure_ascii=False)

print("Contenido de productos_json:")
print(productos_json)

# Ejercicio 2
datos_productos = [
    {'nombre': 'Mouse Pad', 'precio': 10.50, 'categoria': 'Accesorios'}, 
    {'nombre': '', 'precio': 5.00, 'categoria': 'Test'}, 
    {'nombre': 'Monitor', 'precio': 250.00, 'categoria': 'Electrónica'}, 
    {'nombre': 'Cable USB', 'precio': 0, 'categoria': 'Accesorios'}, 
    {'nombre': 'Webcam', 'precio': 45.00, 'categoria': 'Electrónica'} 
]

productos_validos = []

for dato in datos_productos:
    try:
        producto = Producto(dato['nombre'], dato['precio'], dato['categoria'])
        productos_validos.append(producto)
        print(f"Creado: {producto.nombre}")
    except ValueError as e:
        print(f"Error al crear el producto ' {e}")


if productos_validos:
    productos_dict_validos = [p.to_dict() for p in productos_validos]
    productos_json_validado = json.dumps(productos_dict_validos, indent=4, ensure_ascii=False)
else:
    productos_json_validado = "[]"



# Ejercicio 3
# Los autores estan aca para que funcione el ejercicio 5 :D
autor1 = Autor("Gabriel García Márquez", "Colombiana")
autor2 = Autor("José Saramago", "Portuguesa")
autor3 = Autor("Isabel Allende", "Chilena")

libros_list = [
    Libro("Cien años de soledad", autor1, 1967),
    Libro("1984", autor2, 1949),
    Libro("Don Quijote de la Mancha", autor3, 1605)
]


biblioteca_dicts = [l.to_dict() for l in libros_list]
biblioteca_json = json.dumps(biblioteca_dicts, indent=4, ensure_ascii=False)

print("Contenido de biblioteca_json:")
print(biblioteca_json)


# Ejercicio 4
datos_libros = [
    {'titulo': 'El señor de los anillos','autor': {
            'nombre': 'J.R.R. Tolkien',
            'nacionalidad': 'Uruguay'
        }, 'anio': 1954}, 
    {'titulo': '', 'autor': {
            'nombre': 'autor test',
            'nacionalidad': 'Narnia'
        }, 'anio': 2000}, 
    {'titulo': 'Orgullo y prejuicio', 'autor': {
            'nombre': 'autor test 2',
            'nacionalidad': 'Narnia y un poco mas alla'
        },  'anio': 1813}, 
    {'titulo': 'El Hobbit', 'autor': {
            'nombre': 'autor test3',
            'nacionalidad': 'La plata'
        }, 'anio': -10}, 
]

libros_validos = []
print("Intentando crear objetos LibroValidado:")
for dato in datos_libros:
    try:
        autor = Autor(dato['autor']['nombre'],dato['autor']['nacionalidad'])
        libro = Libro(dato['titulo'], autor, dato['anio'])
        libros_validos.append(libro)
        print(f"Creado: {libro.titulo}")
    except ValueError as e:
        print(f"Error al crear el libro ' {e}")


biblioteca_dicts = [l.to_dict() for l in libros_validos]
biblioteca_json = json.dumps(biblioteca_dicts, indent=4, ensure_ascii=False)


print("\nResultado serializado (biblioteca_json):")
print(biblioteca_json)

#Ejercicio 5

libro1 = Libro("caperucita",autor1, 1967)
libro2 = Libro("libro 2", autor2,1995)
libro3 = Libro("encapuchada", autor3,1982)

libros = [libro1, libro2, libro3]

libros_con_autores_dicts = [l.to_dict() for l in libros]
libros_con_autores_json = json.dumps(libros_con_autores_dicts, indent=4, ensure_ascii=False)

print("Contenido de libros_con_autores_json:")
print(libros_con_autores_json)

# ejercicio 6
editorial_sudamericana = Editorial("Sudamericana", "Argentina",None)
editorial_sudamericana.agregar_libro(libro1)
editorial_sudamericana.agregar_libro(libro2)

editorial_dict = editorial_sudamericana.to_dict()
editorial_json = json.dumps(editorial_dict, indent=4, ensure_ascii=False)

print("Editorial json: "+editorial_json)

data_editorial = json.loads(editorial_json)
libros_validos = []
for dato in data_editorial['libros_publicados']:
    try:
        autor = Autor(dato['autor']['nombre'],dato['autor']['nacionalidad'])
        libro = Libro(dato['titulo'], autor, dato['anio'])
        libros_validos.append(libro)
        print(f"Creado: {libro.titulo}")
    except ValueError as e:
        print(f"Error al crear el libro ' {e}")

editorial_reconstruida = Editorial(data_editorial['nombre'],data_editorial['pais'],libros_validos )

print(editorial_reconstruida)
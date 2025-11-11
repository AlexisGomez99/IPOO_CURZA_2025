from Model import Model
from CRUDInterface import CRUDInterface
from ConexionPostgres import ConexionPostgres
from datetime import datetime

class Producto(Model, CRUDInterface):


    def __init__(self, nombre, descripcion, precio, stock, created_at=None, updated_at=None, id:int = 0):
        super().__init__( created_at, updated_at, id)
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock


    def crear(self):
        sql_query = "INSERT INTO productos (nombre, descripcion, precio, stock, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id, created_at; "
        values = (self.nombre,self.descripcion,self.precio,self.stock,datetime.now(), self.updated_at)
        try:
            with ConexionPostgres() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(sql_query, values)
                    resultado = cursor.fetchone()
                    if resultado:
                        self.id = resultado[0]
                        self.created_at = resultado[1]
                        print(f"Producto '{self.nombre}' creado exitosamente con ID: {self.id}")
                        return True
        except Exception as e:
            print(f" Error al crear el producto: {e}")
            return False
        
    @staticmethod
    def leer():
        sql_query = "SELECT id, nombre, descripcion, precio, stock, created_at, updated_at FROM productos ORDER BY id;"
        lista_productos = []
        try:
            with ConexionPostgres() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(sql_query, (id,))
                    registros = cursor.fetchall()
                    
                    if registros:
                        for registro in registros:
                            (prod_id, nombre, descripcion, precio, stock, created_at, updated_at) = registro
                            producto = Producto(nombre=nombre,descripcion=descripcion,precio=precio,stock=stock,id=prod_id,created_at=created_at,updated_at=updated_at)
                            lista_productos.append(producto)
                        return lista_productos
                    else:
                        print(f"Producto con ID {id} no encontrado.")
                        return None
            
        except Exception as e:
            print(f"Error al leer el producto: {e}")
            return None
    

    @staticmethod
    def leer_uno(id):
        sql_query = "SELECT id, nombre, descripcion, precio, stock, created_at, updated_at FROM productos WHERE id = %s;"
        try:
            with ConexionPostgres() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(sql_query, (id,))
                    registro = cursor.fetchone()
                    
                    if registro:
                        (prod_id, nombre, descripcion, precio, stock, created_at, updated_at) = registro
                        producto_encontrado = Producto(nombre=nombre,descripcion=descripcion,precio=precio,stock=stock,id=prod_id,created_at=created_at,updated_at=updated_at)
                        print(f"Producto con ID {id} encontrado.")
                        return producto_encontrado
                    else:
                        print(f"Producto con ID {id} no encontrado.")
                        return None
            
        except Exception as e:
            print(f"Error al leer el producto: {e}")
            return None

    def actualizar(self):
        if self.id is None:
            print("No se puede actualizar un producto sin ID. Primero debe ser creado.")
            return False
        self.updated_at = datetime.now()
        sql_query = "UPDATE productos SET nombre = %s, descripcion = %s, precio = %s, stock = %s, updated_at = %s WHERE id = %s;"
        values = (self.nombre, self.descripcion, self.precio, self.stock, self.updated_at,self.id)
        
        try:
            with ConexionPostgres() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(sql_query, values)
                    if cursor.rowcount == 1:
                        print(f"Producto con ID {self.id} actualizado exitosamente.")
                        return True
                    else:
                        print(f"No se encontró el producto con ID {self.id} para actualizar.")
                        return False

        except Exception as e:
            print(f"Error al actualizar el producto: {e}")
            return False

    @staticmethod
    def eliminar(id):
        
        if Producto.leer_uno(id):
            sql_query = "DELETE FROM productos WHERE id = %s;"
            
            try:
                with ConexionPostgres() as conn:
                    with conn.cursor() as cursor:
                        cursor.execute(sql_query, (id,))
                        if cursor.rowcount == 1:
                            print(f"Producto con ID {id} eliminado exitosamente.")
                            return True
                        else:
                            print(f"No se encontró el producto con ID {id} para eliminar.")
                            return False

            except Exception as e:
                print(f"Error al eliminar el producto: {e}")
                return False
        else:
            print("El producto no existe.")
            return False


    def __str__(self):
        return f"{super().__str__()}\nNombre: {self.nombre}\nDescripcion: {self.descripcion}\nPrecio: {self.precio}\nStock: {self.stock}"

    def __repr__(self):
        return self.__str__()
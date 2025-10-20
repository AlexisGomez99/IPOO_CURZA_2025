class Usuario:
    
    usuarios_registrados = [] 

    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    @staticmethod
    def validar_email(email):
        return '@' in email and '.' in email 

    @classmethod
    def registrar_usuario(cls, nombre, email):
        if not cls.validar_email(email):  
            print(f"ERROR: Email '{email}' no válido. Registro fallido.")
            return

        nuevo_usuario = cls(nombre, email) 
        cls.usuarios_registrados.append(nuevo_usuario)  
        print(f"Usuario '{nombre}' registrado con éxito.")

    @classmethod  
    def mostrar_usuarios(cls):
        print("\n--- Usuarios Registrados ---")
        if not cls.usuarios_registrados:
            print("No hay usuarios registrados.")
            return

        for user in cls.usuarios_registrados:
            print(f"Nombre: {user.nombre}, Email: {user.email}")  


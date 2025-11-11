import psycopg2
from _data import DB_CONFIG

class ConexionPostgres:
    def __init__(self):
        self.connection = None

    def __enter__(self):
        try:
            self.conn = psycopg2.connect(**DB_CONFIG)
            return self.conn
        except Exception as e:
            print(f"Error al conectar a PostgreSQL: {e}")
            raise

    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            if exc_type is None:
                self.conn.commit()
            else:
                self.conn.rollback()
                print("Transacción revertida debido a un error.")
            
            self.conn.close()
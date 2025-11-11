from datetime import datetime
from abc import ABC

class Model(ABC):
    def __init__(self,created_at:str, updated_at:str=None,  id:int= 0):
        self.id = id
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = updated_at

    

    def __str__(self):
        return f"ID: {self.id}\nCreacion: {self.created_at}\nActualizacion: {self.updated_at}"

    def __repr__(self):
        return self.__str__()
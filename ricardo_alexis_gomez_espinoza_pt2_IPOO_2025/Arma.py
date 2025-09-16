

class Arma:
    def __init__(self,tipo:str, puntos_fuerza:int, puntos_resistencia:int, usa_mana:bool, ventajas_sobre:str):
        self.__nombre = ""
        self.__tipo = tipo
        self.__puntos_fuerza = puntos_fuerza
        self.__puntos_resistencia = puntos_resistencia
        self.__usa_mana = usa_mana
        self.__ventajas_sobre = ventajas_sobre

    def set_nombre(self,nombre):
        self.__nombre = nombre
    def set_tipo(self,tipo):
        self.__tipo = tipo
    def set_puntos_fuerza(self,puntos_fuerza):
        self.__puntos_fuerza = puntos_fuerza
    def set_puntos_resistencia(self, puntos_resistencia):
        self.__puntos_resistencia = puntos_resistencia
    def set_usa_mana(self, mana):
        self.__usa_mana = mana
    def set_ventajas_sobre(self, ventajas_sobre):
        self.__ventajas_sobre = ventajas_sobre
    
    def get_nombre(self):
        return self.__nombre
    def get_tipo(self):
        return self.__tipo
    
    
    def get_puntos_resistencia(self):
        return self.__puntos_resistencia
    def get_usa_mana(self):
        return self.__usa_mana
    def get_ventajas_sobre(self):
        return self.__ventajas_sobre
    

    def atacar(self):
        return self.__puntos_fuerza
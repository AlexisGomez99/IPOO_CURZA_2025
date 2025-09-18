

import random
import string


class PasswordAnalizer:
    def __init__(self, numeros:int = 2, mayusculas:int = 2, longitudMaxima:int = 8):
        self.numeros = numeros
        self.mayusculas = mayusculas
        self.longitudMaxima = longitudMaxima
    
    def esClaveFuerte(self,clave):
        claveSinEspacios = clave.replace(" ", "")

        numeros = sum(1 for c in claveSinEspacios if c.isdigit())
        mayusculas = sum(1 for c in claveSinEspacios if c.isupper())
        longitud = len(claveSinEspacios)

        resultado= ""
        if numeros >= self.numeros:
            if(mayusculas >= self.mayusculas):
                if longitud == self.longitudMaxima:
                    resultado= "Clave fuerte"
                elif longitud >self.longitudMaxima:
                    resultado= "Excedio la longitud maxima"
                else:
                    resultado= "Faltan caracteres para la longitud maxima"
            else:
                resultado= "Faltan mayusculas. "
                if longitud == self.longitudMaxima:
                    resultado+= "Clave fuerte"
                elif longitud >self.longitudMaxima:
                    resultado+= "Excedio la longitud maxima"
                else:
                    resultado+= "Faltan caracteres para la longitud maxima"
        else:
            resultado= "Faltan numeros. " 
            if(mayusculas >= self.mayusculas):
                if longitud == self.longitudMaxima:
                    resultado*= "Clave media"
                elif longitud >self.longitudMaxima:
                    resultado+= "Excedio la longitud maxima"
                else:
                    resultado+= "Faltan caracteres para la longitud maxima"
            else:
                resultado+= "Faltan mayusculas. "
                if longitud == self.longitudMaxima:
                    resultado+= "Clave debil"
                elif longitud >self.longitudMaxima:
                    resultado+= "Excedio la longitud maxima"
                else:
                    resultado+= "Faltan caracteres para la longitud maxima. Clave horribleeeee"     
        return resultado
    
    def generarClave(self):
        clave = []

        clave += random.choices(string.digits, k=self.numeros)

        clave += random.choices(string.ascii_uppercase, k=self.mayusculas)

        faltante = self.longitudMaxima - len(clave)
        if faltante > 0:
            clave += random.choices(string.ascii_letters + string.digits, k=faltante)

        random.shuffle(clave)
        return "".join(clave)

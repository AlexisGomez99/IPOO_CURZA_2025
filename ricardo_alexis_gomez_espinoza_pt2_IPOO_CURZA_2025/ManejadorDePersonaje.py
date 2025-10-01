from Personaje import Personaje
from Guerrero import Guerrero
from Elfo import Elfo
from Dragon import Dragon
import random
from LectorCSV import LectorCSV
from ManejadorDeArma import ManejadorDeArma

class ManejadorDePersonaje:
    cantidad_de_personajes = 10
    cantidad_armas = 5
    def __init__(self):
        self.lista_de_personajes = []
        self.manejador_de_armas = ManejadorDeArma()
        self.lector_csv = LectorCSV()

    
    def crear_personaje_aleatorio(self)-> Personaje: # Crear personaje Aleatorio
        # ["Tipo personaje", "nombre", "genero", "articulo"]
        #  tipo, nombre -> nombres_personaje, m/f -> adjetivos_personaje, articulo-> nombres_personaje
        # setear el Personaje, elijiendo dentro de un if dependiendo el tipo, le pasas el nombre
        # retornar personaje
        tipo = random.randint(1,3)
        lista_nombre = self.lector_csv.CSV_to_list("./nombres_personajes.csv")
        del lista_nombre [0]
        lista_adjetivos = self.lector_csv.CSV_to_list("./adjetivos_personajes.csv")
        del lista_adjetivos [0]

        fila_nombre = random.choice(lista_nombre)
        nombre_raw = fila_nombre[0]    # nombre
        genero = fila_nombre[1].lower()  # m o f
        articulo = fila_nombre[2].lower()  # el / la

        adjetivo = random.choice(lista_adjetivos)

        if genero.lower() == "f":
            adjetivo_final = adjetivo[1]
        else:
            adjetivo_final = adjetivo[0]

        nombre = f"{nombre_raw} {articulo} {adjetivo_final}"
        match tipo:
            case 1:
                guerrero = Guerrero(nombre,10,10,5)
                guerrero.set_armadura(10)
                guerrero.agregar_habilidad("usar dos armas")
                guerrero.agregar_habilidad("ataque doble")
                guerrero.agregar_habilidad("esquivo")
                guerrero.agregar_debilidad("Magia")
                guerrero.agregar_debilidad("Dragon")
                return guerrero
            case 2:
                elfo = Elfo(nombre, 30,5,10)
                elfo.set_mana(10)
                elfo.set_puntos_regeneracion(1)
                elfo.agregar_debilidad("Dragone")
                elfo.agregar_debilidad("Oscuridad")
                elfo.agregar_habilidad("Ataque rapido")
                elfo.agregar_habilidad("Doble rafaga")
                return elfo
            case _: 
                dragon = Dragon(nombre,75,25,25,25)
                dragon.set_mana(25)
                dragon.agregar_habilidad("Invocacion Oscura")
                dragon.agregar_habilidad("Embestida Mortal")
                dragon.agregar_debilidad("Magia")
                dragon.agregar_debilidad("Luz")
                return dragon
        pass

    def configurar_arsenal(self):
        for p in self.lista_de_personajes:
            self.manejador_de_armas.crear_armas()
            p.set_arsenal(self.manejador_de_armas.listar_armas())
            self.manejador_de_armas.vaciar_arsenal()
        

    def crear_personajes(self):
        while len(self.lista_de_personajes) <=10:
            personaje = self.crear_personaje_aleatorio()
            if all(p.get_nombre() != personaje.get_nombre() for p in self.lista_de_personajes):
                self.lista_de_personajes.append(personaje)
            else:
                print(f"El Personaje {personaje.get_nombre()} ya está creado.")
    
    def listar_personajes(self):
        return self.lista_de_personajes
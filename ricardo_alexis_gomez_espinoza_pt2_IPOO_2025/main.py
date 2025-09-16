from Guerrero import Guerrero
from Elfo import Elfo
from Dragon import Dragon
from Espada import Espada
from Arco import Arco
from Escudo import Escudo

guerrero = Guerrero("Dorito", 10,10,5)
guerrero.set_armadura(10)
guerrero.nueva_habilidad("usar dos armas")
guerrero.nueva_habilidad("ataque doble")
guerrero.nueva_habilidad("esquivo")
guerrero.nueva_habilidad("Magia")
guerrero.nueva_habilidad("Dragon")
print(guerrero.__str__)

elfo = Elfo("Papita", 30,5,10)
elfo.set_mana(10)
elfo.set_puntos_regeneracion(1)
elfo.nueva_debilidad("Dragone")
elfo.nueva_debilidad("Oscuridad")
elfo.nueva_habilidad("Ataque rapido")
elfo.nueva_habilidad("Doble rafaga")
print(elfo.__str__)

dragon = Dragon("Chimuelo",75,25,25,25)
dragon.set_mana(25)
dragon.nueva_debilidad("Invocacion Oscura")
dragon.nueva_habilidad("Embestida Mortal")
dragon.nueva_debilidad("Magia")
dragon.nueva_debilidad("Luz")
print(dragon.__str__)

espada = Espada("Ofensivo", 10, 0,False, "Dragon")
espada.set_nombre("Odisea")
espada.nueva_gema("Gema de Daño")
espada.nueva_gema("Gema de Fuerza")
print(espada.__str__)

arco = Arco("Ofensivo", 5, 0,False, "Dragon",0)
arco.set_nombre("Bow")
arco.set_cantidad_flechas(10)
print(arco.__str__)

escudo = Escudo("Defensivo", 15, 100,False, "Elfo",0)
escudo.set_nombre("Escudito")
escudo.set_aumento_resistencia(2)
print(escudo.__str__)

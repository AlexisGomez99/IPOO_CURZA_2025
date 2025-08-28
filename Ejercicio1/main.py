from Jugador import Jugador
from Equipo import Equipo


def jugadoresMasAltos(jugadores):
    if not jugadores:
        return []
   
    alturaMax = jugadores[0].altura
   
    for j in jugadores:
        if j.altura > alturaMax:
            alturaMax = j.altura

    masAltos = []
    for j in jugadores:
        if j.altura == alturaMax:
            masAltos.append(j.nombre)

    return masAltos
        
            
    
def equiposMasGanadores(equipos): 
    if not equipos:
        return []
    
    maximoPartidosGanados = max(e.partidosGanados for e in equipos)

    equiposGanadores= [e for e in equipos if e.partidosGanados == maximoPartidosGanados]

    return equiposGanadores

def jugadoresConMasPuntos(jugadores): 
    if not jugadores:
        return []
    
    maximoPuntos = max(j.puntosTotales for j in jugadores)

    jugadoresConMasAnotaciones= [j for j in jugadores if j.puntosTotales == maximoPuntos]

    return jugadoresConMasAnotaciones

def alturaPromedio(equipos, jugadores):
    cantJugador=0
    altura=0
    listaPromedios = []
    for e in equipos:
        for j in jugadores:
            if e.nombre == j.equipo:
                cantJugador+=1
                altura = altura + j.altura
        promedio= float(altura/cantJugador)
        listaPromedios.append(f"{e.nombre} promedio de altura: {promedio}" )
    
    return listaPromedios

def jugadoresMasPuntosPeorEquipo(equipos, jugadores):
    puntosMaximos = 0
    resultado = dict()
    for e in equipos:
        puntosMaximos = max(j.puntosTotales for j in jugadores if j.equipo == e.nombre)
        listaJugadorPorEquipo = [j for j in jugadores if j.puntosTotales == puntosMaximos]
        resultado[e] = listaJugadorPorEquipo

    return resultado

jugador1 = Jugador("Alexis Gómez","27-12-1999", "Los Angeles Lakers",1.88, 42456256 ,1000)
jugador2 = Jugador("LeBron James","1984-12-30","Los Angeles Lakers",2.06,1234567890,1090)
jugador3 = Jugador("Stephen Curry","1988-03-14","Golden State Warriors",1.91,2345678901,980)
jugador4 = Jugador("Giannis Antetokounmpo","1994-12-06","Milwaukee Bucks",2.11,3456789012,1155)
jugador5 = Jugador("Kevin Durant","1988-09-29","Phoenix Suns",2.06,4567890123,970)
jugador6 = Jugador("Ja Morant","1999-08-10","Memphis Grizzlies",1.91,8901234567,950)
equipo1 = Equipo("Los Angeles Lakers", "Los Ãngeles", 82, 43)
equipo2 = Equipo("Golden State Warriors", "San Francisco", 82, 44)
equipo3 = Equipo("Milwaukee Bucks", "Milwaukee", 82, 58)
equipo4 = Equipo("Phoenix Suns", "Phoenix", 82, 48)
equipo5 = Equipo("Memphis Grizzlies", "Memphis", 82, 51)
jugadores = []
equipos = []

jugadores.extend([jugador1, jugador2, jugador3, jugador4, jugador5, jugador6])
equipos.extend([equipo1,equipo2,equipo3,equipo4,equipo5])

print(jugadoresMasAltos(jugadores))
print(equiposMasGanadores(equipos))
print(jugadoresConMasPuntos(jugadores))
print(alturaPromedio(equipos,jugadores))
print(jugadoresMasPuntosPeorEquipo(equipos,jugadores))
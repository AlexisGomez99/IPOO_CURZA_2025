from Jugador import Jugador
from Equipo import Equipo
import csv

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
    if not equipos:
        return {'equipos': [], 'jugadores': []}

    # 1. Encontrar derrotas máximas
    derrotasMaximas = max(e.partidosJugados - e.partidosGanados for e in equipos)
    peoresEquipos = [e for e in equipos if (e.partidosJugados - e.partidosGanados) == derrotasMaximas]

    # 2. Tomar los jugadores cuyo equipo (str) coincide con el nombre de esos equipos
    nombresPeores = {e.nombre for e in peoresEquipos}
    jugadoresEnPeores = [j for j in jugadores if j.equipo in nombresPeores]

    if not jugadoresEnPeores:
        return {'equipos': peoresEquipos, 'jugadores': []}

    # 3. Buscar los máximos puntos
    puntosMaximos = max(j.puntosTotales for j in jugadoresEnPeores)
    jugadoresConMasPuntos = [j for j in jugadoresEnPeores if j.puntosTotales == puntosMaximos]

    ### tengo problemas con la comparacion de nombres de equipo y el nombre no toma bien los str quizas no son parecidos y por eso no trae los jugadores.
    return {
        'equipos': peoresEquipos,
        'jugadores': jugadoresConMasPuntos
    }


def normalizarFila(row, esperadas):
    if not row:
        return []

    cols = row[0].split(",") if len(row) == 1 else row
    cols = [c.strip() for c in cols if c is not None]

    if len(cols) >= esperadas:
        return cols[:esperadas]
    return []  


def leerEquipos(path):
    equipos = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.reader(f, skipinitialspace=True)
        for row in reader:
            cols = normalizarFila(row, esperadas=4)
            if not cols:
                continue
            nombre, ciudad, pj, pg = cols
            equipos.append(Equipo(nombre, ciudad, int(pj), int(pg)))
    return equipos


def leerJugadores(path):
    jugadores = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.reader(f, skipinitialspace=True)
        for row in reader:
            cols = normalizarFila(row, esperadas=6)
            if not cols:
                continue
            nombre, fechaNac, equipo, altura, dni, puntos = cols
            jugadores.append(Jugador(nombre, fechaNac, equipo, float(altura), int(dni), int(puntos)))
    return jugadores




jugadores = leerJugadores("../2025-TR-jugadores.csv")
equipos = leerEquipos("../2025-TR-equipos.csv")



print(jugadoresMasAltos(jugadores))
print(equiposMasGanadores(equipos))
print(jugadoresConMasPuntos(jugadores))
print(alturaPromedio(equipos,jugadores))
print(jugadoresMasPuntosPeorEquipo(equipos,jugadores))
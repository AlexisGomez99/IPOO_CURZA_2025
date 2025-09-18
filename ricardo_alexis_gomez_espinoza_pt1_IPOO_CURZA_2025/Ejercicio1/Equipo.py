


class Equipo:
    def __init__(self,nombre,ciudad, partidosJugados, partidosGanados):
        self.nombre= nombre
        self.ciudad= ciudad
        self.partidosJugados= partidosJugados
        self.partidosGanados= partidosGanados

    def __str__(self):
        return f"Equipo(nombre={self.nombre}, ciudad={self.ciudad}, partidos jugados={self.partidosJugados}, partidos ganados={self.partidosGanados}"

    def __repr__(self):
        return self.__str__()
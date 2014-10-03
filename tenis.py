# -*- coding: utf-8 -*-


class Jugador(object):

    INCREMENTO_CUANDO_GANA = 1

    puntos_partida = [0, 15, 30, 40, 50, 60]

    def __init__(self, nombre='Anónimo'):
        self.indice_puntos = 0
        self.nombre = nombre

    @property
    def puntos(self):
        return self.puntos_partida[self.indice_puntos]

    def ganar_punto(self):
        if self.indice_puntos in range(len(self.puntos_partida)):
            self.indice_puntos += self.INCREMENTO_CUANDO_GANA
        return self.puntos

    def __str__(self):
        return self.nombre


class Partida(object):

    DIFERENCIA_DE_PUNTOS_PARA_GANAR = 2
    INDICE_DE_CUARENTA_PUNTOS = 3
    INDICE_DE_VENTAJA = 4

    def __init__(self, jugador_1, jugador_2):
        self.jugador_1 = jugador_1
        self.jugador_2 = jugador_2
        self.ganador = None

    def _ganar_punto_jugador(self, jugador_1, jugador_2):
        if jugador_1.indice_puntos == self.INDICE_DE_CUARENTA_PUNTOS and jugador_2.indice_puntos == self.INDICE_DE_VENTAJA:
            jugador_2.indice_puntos -= 1
        else:
            jugador_1.ganar_punto()

        if jugador_1.indice_puntos > self.INDICE_DE_CUARENTA_PUNTOS and jugador_1.indice_puntos - jugador_2.indice_puntos >= self.DIFERENCIA_DE_PUNTOS_PARA_GANAR:
            self.ganador = jugador_1
            return True

        return False

    def ganar_punto_jugador_1(self):
        return self._ganar_punto_jugador(self.jugador_1, self.jugador_2)

    def ganar_punto_jugador_2(self):
        return self._ganar_punto_jugador(self.jugador_2, self.jugador_1)

    @property
    def puntuacion_jugador_1(self):
        return self._puntos_jugador(self.jugador_1)

    @property
    def puntuacion_jugador_2(self):
        return self._puntos_jugador(self.jugador_2)

    def _puntos_jugador(self, jugador):
        if jugador.indice_puntos <= self.INDICE_DE_CUARENTA_PUNTOS:
            return str(jugador.puntos)
        return 'Ventaja'

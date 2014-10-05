# -*- coding: utf-8 -*-


class Jugador(object):

    INCREMENTO_CUANDO_GANA = 1

    puntos_partida = [CERO, QUINCE, TREINTA, CUATENTA, VENTAJA, JUEGO] = range(6)

    puntos_partida_texto = {
        CERO: '0',
        QUINCE: '15',
        TREINTA: '30',
        CUATENTA: '40',
        VENTAJA: 'Ventaja',
        JUEGO: 'Juego',
    }

    def __init__(self, nombre='Anónimo'):
        self.indice_puntos = Jugador.CERO
        self.nombre = nombre

    @property
    def puntos(self):
        return self.puntos_partida_texto[self.indice_puntos]

    def ganar_punto(self):
        if self.indice_puntos in range(len(self.puntos_partida)):
            self.indice_puntos += self.INCREMENTO_CUANDO_GANA
        return self.puntos

    def __str__(self):
        return self.nombre


class Partida(object):

    DIFERENCIA_DE_PUNTOS_PARA_GANAR = 2

    def __init__(self, jugador_1, jugador_2):
        self.jugador_1 = jugador_1
        self.jugador_2 = jugador_2
        self.ganador = None

    def _ganar_punto_jugador(self, jugador_1, jugador_2):
        if jugador_1.indice_puntos == Jugador.CUATENTA and jugador_2.indice_puntos == Jugador.VENTAJA:
            jugador_2.indice_puntos = Jugador.CUATENTA
        else:
            jugador_1.ganar_punto()

        if jugador_1.indice_puntos > Jugador.CUATENTA and jugador_1.indice_puntos - jugador_2.indice_puntos >= self.DIFERENCIA_DE_PUNTOS_PARA_GANAR:
            self.ganador = jugador_1

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
        return jugador.puntos

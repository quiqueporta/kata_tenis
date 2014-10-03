# -*- coding: utf-8 -*-

from tenis import Jugador, Partida

if __name__ == '__main__':
        jugador_1 = Jugador('Rafa Nadal')
        jugador_2 = Jugador('Roger Federer')
        partida = Partida(jugador_1, jugador_2)

        fin_partida = False

        while not partida.ganador:
            print "Partida: %s (%s) %s (%s)" % (jugador_1.nombre,
                                                partida.puntuacion_jugador_1,
                                                jugador_2.nombre,
                                                partida.puntuacion_jugador_2)
            print ">>>"
            jugador = raw_input("¿Quien ganó el punto? (1) %s / (2) %s: " %
                                (jugador_1.nombre, jugador_2.nombre))
            if jugador == '1':
                partida.ganar_punto_jugador_1()
            if jugador == '2':
                partida.ganar_punto_jugador_2()

        print ">>>"
        print ">>>"
        print "Ha ganado " + partida.ganador.nombre
        print ">>>"

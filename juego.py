# -*- coding: utf-8 -*-

from tenis import Jugador, Partida

if __name__ == '__main__':
        jugador_1 = Jugador('Rafa Nadal')
        jugador_2 = Jugador('Roger Federer')
        partida = Partida(jugador_1, jugador_2)

        fin_partida = False

        while not partida.ganador:
            print("Partida: {0} ({1}) {2} ({3})".format(jugador_1.nombre,
                                                        partida.puntuacion_jugador_1,
                                                        jugador_2.nombre,
                                                        partida.puntuacion_jugador_2)
                  )
            print(">>>")
            jugador = input("¿Quien ganó el punto? (1) {0} / (2) {1}: ".format(
                jugador_1.nombre, jugador_2.nombre))
            if jugador == '1':
                partida.ganar_punto_jugador_1()
            elif jugador == '2':
                partida.ganar_punto_jugador_2()

        print(">>>")
        print(">>>")
        print("Ha ganado {0}".format(partida.ganador.nombre))
        print(">>>")

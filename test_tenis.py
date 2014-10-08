import unittest

from tenis import Jugador, Partida


class TestTenis(unittest.TestCase):

    def setUp(self):
        self.jugador_1 = Jugador()
        self.jugador_2 = Jugador()
        self.partida = Partida(self.jugador_1, self.jugador_2)

    def test_jugador_empieza_con_0_puntos(self):
        self.assertEqual(self.jugador_1.indice_puntos, 0)
        self.assertEqual(self.jugador_1.puntos, '0')

    def test_jugador_gana_puntos(self):
        self.assertTrue(hasattr(self.jugador_1, 'ganar_punto'))

        self.assertEqual(self.jugador_1.ganar_punto(), '15')
        self.assertEqual(self.jugador_1.puntos, '15')

        self.assertEqual(self.jugador_1.ganar_punto(), '30')
        self.assertEqual(self.jugador_1.puntos, '30')

        self.assertEqual(self.jugador_1.ganar_punto(), '40')
        self.assertEqual(self.jugador_1.puntos, '40')

        self.assertEqual(self.jugador_1.ganar_punto(), 'Ventaja')
        self.assertEqual(self.jugador_1.puntos, 'Ventaja')

        self.assertEqual(self.jugador_1.ganar_punto(), 'Juego')
        self.assertEqual(self.jugador_1.puntos, 'Juego')

    def test_ganar_partida_jugador_1_40_a_0(self):

        self.partida.ganar_punto_jugador_1()
        self.assertEqual(self.partida.jugador_1.puntos, '15')

        self.partida.ganar_punto_jugador_1()
        self.assertEqual(self.partida.jugador_1.puntos, '30')

        self.partida.ganar_punto_jugador_1()
        self.assertEqual(self.partida.jugador_1.puntos, '40')

        self.partida.ganar_punto_jugador_1()
        self.assertEqual(self.partida.ganador, self.jugador_1)

    def test_ganar_partida_jugador_2_40_a_0(self):

        self.partida.ganar_punto_jugador_2()
        self.assertEqual(self.partida.jugador_2.puntos, '15')

        self.partida.ganar_punto_jugador_2()
        self.assertEqual(self.partida.jugador_2.puntos, '30')

        self.partida.ganar_punto_jugador_2()
        self.assertEqual(self.partida.jugador_2.puntos, '40')

        self.partida.ganar_punto_jugador_2()
        self.assertEqual(self.partida.ganador, self.jugador_2)

    def test_ganar_por_diferencia_de_dos(self):

        self.partida.ganar_punto_jugador_2()
        self.partida.ganar_punto_jugador_2()
        self.partida.ganar_punto_jugador_2()

        self.partida.ganar_punto_jugador_1()
        self.partida.ganar_punto_jugador_1()
        self.partida.ganar_punto_jugador_1()

        self.assertFalse(self.partida.ganar_punto_jugador_1())

        self.partida.ganar_punto_jugador_1()
        self.assertEqual(self.partida.ganador, self.jugador_1)

    def test_ir_con_ventaja_perder_e_ir_a_iguales(self):

        self.partida.ganar_punto_jugador_2()
        self.partida.ganar_punto_jugador_2()
        self.partida.ganar_punto_jugador_2()

        self.partida.ganar_punto_jugador_1()
        self.partida.ganar_punto_jugador_1()
        self.partida.ganar_punto_jugador_1()

        self.partida.ganar_punto_jugador_1()

        self.partida.ganar_punto_jugador_2()

        self.assertEqual(self.jugador_1.puntos, '40')
        self.assertEqual(self.jugador_2.puntos, '40')

        self.partida.ganar_punto_jugador_2()
        self.partida.ganar_punto_jugador_1()

        self.assertEqual(self.jugador_1.puntos, '40')
        self.assertEqual(self.jugador_2.puntos, '40')

    def test_ir_a_ventaja_y_ganar_el_juego(self):

        self.partida.ganar_punto_jugador_2()
        self.partida.ganar_punto_jugador_2()
        self.partida.ganar_punto_jugador_2()

        self.partida.ganar_punto_jugador_1()
        self.partida.ganar_punto_jugador_1()
        self.partida.ganar_punto_jugador_1()

        self.partida.ganar_punto_jugador_1()

        self.partida.ganar_punto_jugador_1()

        self.assertEqual(self.partida.ganador, self.jugador_1)

    def test_obtener_puntuacion_jugador_1(self):

        self.assertEqual(self.partida.puntuacion_jugador_1, '0')
        self.partida.ganar_punto_jugador_1()
        self.partida.ganar_punto_jugador_1()
        self.assertEqual(self.partida.puntuacion_jugador_1, '30')
        self.partida.ganar_punto_jugador_1()
        self.assertEqual(self.partida.puntuacion_jugador_1, '40')
        self.partida.ganar_punto_jugador_1()
        self.assertEqual(self.partida.puntuacion_jugador_1, 'Ventaja')

    def test_obtener_puntuacion_jugador_2(self):

        self.partida.ganar_punto_jugador_2()
        self.assertEqual(self.partida.puntuacion_jugador_2, '15')
        self.partida.ganar_punto_jugador_2()
        self.assertEqual(self.partida.puntuacion_jugador_2, '30')
        self.partida.ganar_punto_jugador_2()
        self.assertEqual(self.partida.puntuacion_jugador_2, '40')
        self.partida.ganar_punto_jugador_2()
        self.assertEqual(self.partida.puntuacion_jugador_2, 'Ventaja')

    def test_no_puntua_mas_de_juego(self):

        self.partida.ganar_punto_jugador_1()
        self.partida.ganar_punto_jugador_1()
        self.partida.ganar_punto_jugador_1()
        self.partida.ganar_punto_jugador_1()
        self.partida.ganar_punto_jugador_1()
        self.assertEqual(self.partida.puntuacion_jugador_1, 'Juego')

    def test_obtener_ganador_jugador_1(self):

        self.assertEqual(self.partida.ganador, None)

        self.partida.ganar_punto_jugador_1()
        self.assertEqual(self.partida.ganador, None)
        self.partida.ganar_punto_jugador_1()
        self.assertEqual(self.partida.ganador, None)
        self.partida.ganar_punto_jugador_1()
        self.assertEqual(self.partida.ganador, None)
        self.partida.ganar_punto_jugador_1()
        self.assertEqual(self.partida.ganador, self.jugador_1)

    def test_obtener_ganador_jugador_2(self):

        self.assertEqual(self.partida.ganador, None)

        self.partida.ganar_punto_jugador_2()
        self.assertEqual(self.partida.ganador, None)
        self.partida.ganar_punto_jugador_2()
        self.assertEqual(self.partida.ganador, None)
        self.partida.ganar_punto_jugador_2()
        self.assertEqual(self.partida.ganador, None)
        self.partida.ganar_punto_jugador_2()
        self.assertEqual(self.partida.ganador, self.jugador_2)

    def test_obtener_nombre_jugadores(self):
        jugador_1 = Jugador('Rafa')
        jugador_2 = Jugador('Federer')

        self.assertEqual(str(jugador_1), 'Rafa')
        self.assertEqual(str(jugador_2), 'Federer')
        self.assertEqual(jugador_1.nombre, 'Rafa')
        self.assertEqual(jugador_2.nombre, 'Federer')

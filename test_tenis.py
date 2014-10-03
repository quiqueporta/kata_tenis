import unittest

from tenis import Jugador, Partida


class TestTenis(unittest.TestCase):

    def test_jugador_empieza_con_0_puntos(self):
        jugador_1 = Jugador()
        self.assertEqual(jugador_1.puntos, 0)

    def test_jugador_gana_puntos(self):
        jugador = Jugador()
        self.assertTrue(hasattr(jugador, 'ganar_punto'))

        jugador.ganar_punto()
        self.assertEqual(jugador.puntos, 15)

        jugador.ganar_punto()
        self.assertEqual(jugador.puntos, 30)

        jugador.ganar_punto()
        self.assertEqual(jugador.puntos, 40)

    def test_ganar_partida_jugador_1_40_a_0(self):
        jugador_1 = Jugador()
        jugador_2 = Jugador()
        partida = Partida(jugador_1, jugador_2)

        partida.ganar_punto_jugador_1()
        self.assertEqual(partida.jugador_1.puntos, 15)

        partida.ganar_punto_jugador_1()
        self.assertEqual(partida.jugador_1.puntos, 30)

        partida.ganar_punto_jugador_1()
        self.assertEqual(partida.jugador_1.puntos, 40)

        self.assertTrue(partida.ganar_punto_jugador_1())

    def test_ganar_partida_jugador_2_40_a_0(self):
        jugador_1 = Jugador()
        jugador_2 = Jugador()
        partida = Partida(jugador_1, jugador_2)

        partida.ganar_punto_jugador_2()
        self.assertEqual(partida.jugador_2.puntos, 15)

        partida.ganar_punto_jugador_2()
        self.assertEqual(partida.jugador_2.puntos, 30)

        partida.ganar_punto_jugador_2()
        self.assertEqual(partida.jugador_2.puntos, 40)

        self.assertTrue(partida.ganar_punto_jugador_2())

    def test_ganar_por_diferencia_de_dos(self):

        jugador_1 = Jugador()
        jugador_2 = Jugador()
        partida = Partida(jugador_1, jugador_2)

        partida.ganar_punto_jugador_2()
        partida.ganar_punto_jugador_2()
        partida.ganar_punto_jugador_2()

        partida.ganar_punto_jugador_1()
        partida.ganar_punto_jugador_1()
        partida.ganar_punto_jugador_1()

        self.assertFalse(partida.ganar_punto_jugador_1())

        self.assertTrue(partida.ganar_punto_jugador_1())

    def test_ir_con_ventaja_perder_e_ir_a_iguales(self):

        jugador_1 = Jugador()
        jugador_2 = Jugador()
        partida = Partida(jugador_1, jugador_2)

        partida.ganar_punto_jugador_2()
        partida.ganar_punto_jugador_2()
        partida.ganar_punto_jugador_2()

        partida.ganar_punto_jugador_1()
        partida.ganar_punto_jugador_1()
        partida.ganar_punto_jugador_1()

        partida.ganar_punto_jugador_1()

        partida.ganar_punto_jugador_2()

        self.assertEqual(jugador_1.puntos, 40)
        self.assertEqual(jugador_2.puntos, 40)

        partida.ganar_punto_jugador_2()
        partida.ganar_punto_jugador_1()

        self.assertEqual(jugador_1.puntos, 40)
        self.assertEqual(jugador_2.puntos, 40)

    def test_ir_a_ventaja_y_ganar_el_juego(self):
        jugador_1 = Jugador()
        jugador_2 = Jugador()
        partida = Partida(jugador_1, jugador_2)

        partida.ganar_punto_jugador_2()
        partida.ganar_punto_jugador_2()
        partida.ganar_punto_jugador_2()

        partida.ganar_punto_jugador_1()
        partida.ganar_punto_jugador_1()
        partida.ganar_punto_jugador_1()

        partida.ganar_punto_jugador_1()

        self.assertTrue(partida.ganar_punto_jugador_1())

    def test_obtener_puntuacion_jugador_1(self):
        jugador_1 = Jugador()
        jugador_2 = Jugador()
        partida = Partida(jugador_1, jugador_2)

        partida.ganar_punto_jugador_1()
        self.assertEqual(partida.puntuacion_jugador_1, '15')
        partida.ganar_punto_jugador_1()
        self.assertEqual(partida.puntuacion_jugador_1, '30')
        partida.ganar_punto_jugador_1()
        self.assertEqual(partida.puntuacion_jugador_1, '40')
        partida.ganar_punto_jugador_1()
        self.assertEqual(partida.puntuacion_jugador_1, 'Ventaja')

    def test_obtener_puntuacion_jugador_2(self):
        jugador_1 = Jugador()
        jugador_2 = Jugador()
        partida = Partida(jugador_1, jugador_2)

        partida.ganar_punto_jugador_2()
        self.assertEqual(partida.puntuacion_jugador_2, '15')
        partida.ganar_punto_jugador_2()
        self.assertEqual(partida.puntuacion_jugador_2, '30')
        partida.ganar_punto_jugador_2()
        self.assertEqual(partida.puntuacion_jugador_2, '40')
        partida.ganar_punto_jugador_2()
        self.assertEqual(partida.puntuacion_jugador_2, 'Ventaja')

    def test_no_puntua_mas_de_ventaja(self):
        jugador_1 = Jugador()
        jugador_2 = Jugador()
        partida = Partida(jugador_1, jugador_2)

        partida.ganar_punto_jugador_1()
        partida.ganar_punto_jugador_1()
        partida.ganar_punto_jugador_1()
        partida.ganar_punto_jugador_1()
        partida.ganar_punto_jugador_1()
        self.assertEqual(partida.puntuacion_jugador_1, 'Ventaja')

    def test_obtener_ganador_jugador_1(self):
        jugador_1 = Jugador()
        jugador_2 = Jugador()
        partida = Partida(jugador_1, jugador_2)

        self.assertEqual(partida.ganador, None)

        partida.ganar_punto_jugador_1()
        self.assertEqual(partida.ganador, None)
        partida.ganar_punto_jugador_1()
        self.assertEqual(partida.ganador, None)
        partida.ganar_punto_jugador_1()
        self.assertEqual(partida.ganador, None)
        partida.ganar_punto_jugador_1()
        self.assertEqual(partida.ganador, jugador_1)

    def test_obtener_ganador_jugador_2(self):
        jugador_1 = Jugador()
        jugador_2 = Jugador()
        partida = Partida(jugador_1, jugador_2)

        self.assertEqual(partida.ganador, None)

        partida.ganar_punto_jugador_2()
        self.assertEqual(partida.ganador, None)
        partida.ganar_punto_jugador_2()
        self.assertEqual(partida.ganador, None)
        partida.ganar_punto_jugador_2()
        self.assertEqual(partida.ganador, None)
        partida.ganar_punto_jugador_2()
        self.assertEqual(partida.ganador, jugador_2)

    def test_obtener_nombre_jugadores(self):
        jugador_1 = Jugador('Rafa')
        jugador_2 = Jugador('Federer')

        self.assertEqual(str(jugador_1), 'Rafa')
        self.assertEqual(str(jugador_2), 'Federer')
        self.assertEqual(jugador_1.nombre, 'Rafa')
        self.assertEqual(jugador_2.nombre, 'Federer')

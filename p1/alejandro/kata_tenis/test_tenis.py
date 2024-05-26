import unittest
from tenis import Tenis

class TestTenis(unittest.TestCase):
    
    # Tests de errores
    def test_error_jugador1_negativo(self):
        tenis = Tenis()
        tenis.jugador1 = -1
        tenis.jugador2 = 0
        with self.assertRaises(ValueError):
            tenis.obtener_resultado()
    
    def test_error_puntuacion_string(self):
        tenis = Tenis()
        tenis.jugador1 = 'a'
        tenis.jugador2 = 0
        with self.assertRaises(ValueError):
            tenis.obtener_resultado()

    
    # Tests de resultados
    def test_resultado_juego_0_0(self):
        tenis = Tenis()
        tenis.jugador1 = 0
        tenis.jugador2 = 0
        self.assertEqual('Love-Love', tenis.obtener_resultado())

    def test_resultado_juego_1_0(self):
        tenis = Tenis()
        tenis.jugador1 = 1
        tenis.jugador2 = 0
        self.assertEqual('Fifteen-Love', tenis.obtener_resultado())
    
    def test_resultado_juego_0_1(self):
        tenis = Tenis()
        tenis.jugador1 = 0
        tenis.jugador2 = 1
        self.assertEqual('Love-Fifteen', tenis.obtener_resultado())

    def test_resultado_juego_2_1(self):
        tenis = Tenis()
        tenis.jugador1 = 2
        tenis.jugador2 = 1
        self.assertEqual('Thirty-Fifteen', tenis.obtener_resultado())
    
    def test_resultado_juego_1_3(self):
        tenis = Tenis()
        tenis.jugador1 = 1
        tenis.jugador2 = 3
        self.assertEqual('Fifteen-Forty', tenis.obtener_resultado())
    
    def test_resultado_juego_empate_1_1(self):
        tenis = Tenis()
        tenis.jugador1 = 1
        tenis.jugador2 = 1
        self.assertEqual('Fifteen-Fifteen', tenis.obtener_resultado())
    
    def test_resultado_juego_ganador_4_0(self):
        tenis = Tenis()
        tenis.jugador1 = 4
        tenis.jugador2 = 0
        self.assertEqual('Game jugador 1', tenis.obtener_resultado())
    
    def test_resultado_juego_ganador_2_4(self):
        tenis = Tenis()
        tenis.jugador1 = 2
        tenis.jugador2 = 4
        self.assertEqual('Game jugador 2', tenis.obtener_resultado())
    
    def test_resultado_deuce(self):
        tenis = Tenis()
        tenis.jugador1 = 3
        tenis.jugador2 = 3
        self.assertEqual('Deuce', tenis.obtener_resultado())

    def test_resultado_ventaja_jugador1(self):
        tenis = Tenis()
        tenis.jugador1 = 4
        tenis.jugador2 = 3
        self.assertEqual('Advantage jugador 1', tenis.obtener_resultado())
    
    def test_resultado_ventaja_jugador2(self):
        tenis = Tenis()
        tenis.jugador1 = 4
        tenis.jugador2 = 5
        self.assertEqual('Advantage jugador 2', tenis.obtener_resultado())
    
    # Tests resultados incorrectos
    def test_resultado_incorrecto_6_1(self):
        tenis = Tenis()
        tenis.jugador1 = 6
        tenis.jugador2 = 1
        with self.assertRaises(ValueError):
            tenis.obtener_resultado()

if __name__ == '__main__':
    unittest.main()
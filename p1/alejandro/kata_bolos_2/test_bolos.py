import unittest
from partida import Partida

class TestBolos(unittest.TestCase):

    # TESTS de creacion de partidas

    def test_crear_partida_a_cero(self):
        partida = Partida()
        partida.crear_partida([(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)])
        assert partida.rondas == [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]

    def test_crear_partida_mas_10_rondas(self):
        partida = Partida()
        rondas = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        rondas.append((0, 0))
        with self.assertRaises(ValueError):
            partida.crear_partida(rondas)
    
    def test_partida_menos_10_rondas(self):
        partida = Partida()
        rondas = [(0, 0), (0, 0)]
        with self.assertRaises(ValueError):
            partida.crear_partida(rondas)

    def test_lanzamiento_no_entero(self):
        partida = Partida()
        rondas = [("1", 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        with self.assertRaises(ValueError):
            partida.crear_partida(rondas)

    def test_ronda_derribando_mas_10_bolos(self):
        partida = Partida()
        rondas = [(7, 6), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        with self.assertRaises(ValueError):
            partida.crear_partida(rondas)    

    def test_lanzamiento_vacio_sin_strike(self):
        partida = Partida()
        rondas = [(4, ), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        with self.assertRaises(ValueError):
            partida.crear_partida(rondas)
    
    
    # TESTS de puntuaciones
    
    def test_puntuacion_partida_a_cero(self):
        partida = Partida()
        rondas = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        partida.crear_partida(rondas)
        self.assertEqual(partida.obtener_puntuacion(), 0)
    
    def test_puntuacion_partido_todo_unos(self):
        partida = Partida()
        rondas = [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]
        partida.crear_partida(rondas)
        self.assertEqual(partida.obtener_puntuacion(), 20)

    def test_puntuacion_partida_open_frames(self):
        partida = Partida()
        rondas = [(7, 1), (1, 4), (5, 2), (3, 6), (2, 0), (8, 0), (0, 5), (2, 1), (3, 6), (4, 4)]
        partida.crear_partida(rondas)
        self.assertEqual(partida.obtener_puntuacion(), 64)

    def test_partida_un_strike(self):
        partida = Partida()
        rondas = [(10, ), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]
        partida.crear_partida(rondas)
        self.assertEqual(partida.obtener_puntuacion(), 30)
    
    def test_partida_dos_strikes(self):
        partida = Partida()
        rondas = [(10, ), (1, 1), (10, ), (5, 0), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]
        partida.crear_partida(rondas)
        self.assertEqual(partida.obtener_puntuacion(), 46)
    
    def test_partida_un_spare(self):
        partida = Partida()
        rondas = [(1, 1), (0, 0), (6, 4), (4, 2), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (1, 0)]
        partida.crear_partida(rondas)
        self.assertEqual(partida.obtener_puntuacion(), 23)
    
    def test_partida_dos_spares(self):
        partida = Partida()
        rondas = [(1, 1), (0, 0), (6, 4), (4, 2), (0, 0), (2, 8), (3, 0), (0, 0), (0, 0), (1, 0)]
        partida.crear_partida(rondas)
        self.assertEqual(partida.obtener_puntuacion(), 39)

    def test_partida_strike_ultima_ronda(self):
        partida = Partida()
        rondas = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (10, 1, 1)]
        partida.crear_partida(rondas)
        self.assertEqual(partida.obtener_puntuacion(), 14)

    def test_partida_spare_ultima_ronda(self):
        partida = Partida()
        rondas = [(0, 0), (2, 2), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (6, 4, 7)]
        partida.crear_partida(rondas)
        self.assertEqual(partida.obtener_puntuacion(), 28)
    
    def test_partida_perfecta(self):
        partida = Partida()
        rondas = [(10, ), (10, ), (10, ), (10, ), (10, ), (10, ), (10, ), (10, ), (10, ), (10, 10, 10)]
        partida.crear_partida(rondas)
        self.assertEqual(partida.obtener_puntuacion(), 300) 

    def test_partida_strike_penultima_spare_ultima_ronda(self):
        partida = Partida()
        rondas = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (10, ), (6, 4, 7)]
        partida.crear_partida(rondas)
        self.assertEqual(partida.obtener_puntuacion(), 37)
               
if __name__ == '__main__':
    unittest.main()

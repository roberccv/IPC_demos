import unittest
import partida

class TestBolos(unittest.TestCase):

    def test_primera_partida_cero_bolos(self):
        p = partida.Partida()
        for i in range(0, 10):
            p.jugar_ronda(0, 0)
        self.assertEqual(p.obtener_puntuacion(),0)

    def test_tirar_mas_de_10_bolos(self):
        p = partida.Partida()
        with self.assertRaises(ValueError):
            p.jugar_ronda(12, 0)
    
    def test_crear_partida_10_rondas(self):
        p = partida.Partida()  
        p.crear_partida()      
        self.assertEqual(len(p.rondas), 10)
    
    def test_jugar_ronda_con_dos_tiradas(self):
        p = partida.Partida()  
        p.crear_partida()
        p.jugar_ronda(1, 1)
        self.assertEqual(p.obtener_puntuacion(), 2)

    def test_jugar_ronda_mas_10_bolos(self):
        p = partida.Partida()  
        p.crear_partida()
        with self.assertRaises(ValueError):
            p.jugar_ronda(6, 6)
    
    def test_jugar_partida_un_strike(self):
        p = partida.Partida()
        p.crear_partida()
        p.jugar_ronda(1, 1)
        p.jugar_ronda(10, 0)
        p.jugar_ronda(2, 2)
        p.jugar_ronda(0, 0)
        p.jugar_ronda(0, 0)
        p.jugar_ronda(0, 0)
        p.jugar_ronda(0, 0)
        p.jugar_ronda(0, 0)
        p.jugar_ronda(0, 0)
        self.assertEqual(p.obtener_puntuacion(),20)

if __name__ == '__main__':
    unittest.main()
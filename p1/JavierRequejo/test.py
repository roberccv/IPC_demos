import unittest
import kata

class ServerClientTest(unittest.TestCase):

    def test_0(self):
        tiros = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        score = kata.Partida.puntuacion(tiros)
        self.assertEqual(score, 0)
    def test_1(self):
        tiros = [[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[1,0],[0,0]]
        score = kata.Partida.puntuacion(tiros)
        self.assertEqual(score, 10)
    def test_11(self):
        tiros = [[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[0,0]]
        score = kata.Partida.puntuacion(tiros)
        self.assertEqual(score, 20)
    def test_spare(self):
        tiros = [[0,"/"],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        score = kata.Partida.puntuacion(tiros)
        self.assertEqual(score, 10)
    def test_spare2(self):
        tiros = [[4,"/"],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        score = kata.Partida.puntuacion(tiros)
        self.assertEqual(score, 10)
    
    def test_spare3(self):
        tiros = [[4,"/"],[2,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        score = kata.Partida.puntuacion(tiros)
        self.assertEqual(score, 14)
    
    def test_strike(self):
        tiros = [["X",0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        score = kata.Partida.puntuacion(tiros)
        self.assertEqual(score, 10)
    
if __name__ == '__main__':
    unittest.main()


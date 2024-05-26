import unittest
import bolos

class TestExample(unittest.TestCase):
    def test_PRValida(self):
        b = bolos.Bolos()
        i = 0
        for puntuacion in b.puntuacionRonda:
            self.assertIsInstance(puntuacion, int)
            self.assertLessEqual(puntuacion,10)
            i = i + 1
        self.assertLessEqual(i,3)
    #la lista de puntuaciones no puede tener mas de 3 elementos (las tres tiradas), y ls puntuaciones deben ser numéricas   
    ## Los test solo pueden tener un assert por test, si se quiere hacer mas de un assert, se debe hacer un test por cada assert
    ## Nombrar bien los Tests!!!!!! 
    

    def test_PP(self):
        b = bolos.Bolos()
        i = 0
        for puntuacion in b.puntuacionPartida:
            self.assertIsInstance(puntuacion, int)
            #self.assertLessEqual(puntuacion,30)
            i = i + 1
        self.assertLessEqual(i,10)

    def test_Marcador(self):
        b = bolos.Bolos()
        self.assertEqual(b.marcador , b.puntuacionPartida.sum())
        
    #No tiene que jugar a los bolos -> tiene que calcular la puntuación de la partida 

if __name__ == '__main__':
    unittest.main()

import unittest
import bolos

class TestPartida(unittest.TestCase):
    def test_puntuacionesNormales(self):
        b = bolos.bolos()
        a = b.calculadora([3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3])
        self.assertEqual(a, 60)
    
    def test_plenoEnMedio(self):
        b = bolos.bolos()
        a = b.calculadora([3,3,3,3,3,3,3,3,3,3,3,10,3,3,3,3,3,3,3])
        self.assertEqual(a, 70)
    
    def test_tamañoCorrecto(self):
        b = bolos.bolos()
        a = b.tamañoCorrecto([3,10,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3])
        self.assertEqual(a, "no bonus")
    
    def test_variosPlenosMedios(self):
        b = bolos.bolos()
        a = b.calculadora([3,3,3,3,3,3,3,3,3,3,3,10,3,3,3,10,3,3])
        self.assertEqual(a, 80)
    
    def test_dosPlenosSeguidos(self):
        b = bolos.bolos()
        a = b.calculadora([3,3,3,3,3,3,3,3,3,3,10,10,3,3,3,3,3,3])
        self.assertEqual(a, 87)
    
    def test_plenoUltimaRonda(self):
        b = bolos.bolos()
        a = b.calculadora([3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,10,3,3])
        self.assertEqual(a, 70)
    
    def test_noSpar(self):
        b = bolos.bolos()
        a = b.contieneSpare([3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,10,3,3])
        self.assertEqual(a , None)
    
    def test_3plenosFinales(self):
        b = bolos.bolos()
        a = b.calculadora([3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,10,10,10])
        self.assertEqual(a, 84)


    def test_4plenosFinales(self):
        b = bolos.bolos()
        a = b.calculadora([3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,10,10,10,10])
        self.assertEqual(a, 108)
    
    def test_todoPlenos(self):
        b = bolos.bolos()
        a = b.calculadora([10,10,10,10,10,10,10,10,10,10,10,10])
        self.assertEqual(a, 300)

    def test_pocasBolas(self):
        b = bolos.bolos()
        with self.assertRaises(Exception):
            b.calculadora([3,3,3,3,3,3,3,3,3])
        
    
    def test_letras(self):
        b = bolos.bolos()
        with self.assertRaises(Exception):
            b.calculadora(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",3,3,3,3,3,3,3,3,3,3])
        
    
    def test_puntuacionesErroneas(self):
        b = bolos.bolos()
        with self.assertRaises(Exception):
            b.calculadora([3,3,3,3,3,3,3,3,3,3,3,3,3,3,12,3,3,3,3,3])
        
    def test_puntuacionesErroneas2(self):
        b = bolos.bolos()
        with self.assertRaises(Exception):
            b.calculadora([3,3,3,3,3,3,3,3,3,3,3,3,3,3,-9,3,3,3,3,3])

    def test_tupla(self):
        b = bolos.bolos()
        with self.assertRaises(Exception):
            b.calculadora((3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3))
        #Tuplas no
    
    def test_spareNormal(self):
        b = bolos.bolos()
        a = b.contieneSpare([3,3,3,3,3,3,8,2,3,3,3,3,3,3,3,3,3,3,3,3])
        self.assertEqual(a, True)
    
    def test_detectaSpare(self):
        b = bolos.bolos()
        a = b.contieneSpare([3,3,3,3,3,3,7,1,3,3,3,3,3,3,3,3,3,3,3,3])
        self.assertEqual(a, None)
    
    def test_spareNormal2(self):
        b = bolos.bolos()
        a = b.calculadora([3,3,3,3,3,3,8,2,3,3,3,3,3,3,3,3,3,3,3,3])
        self.assertEqual(a, 67)
    
    def test_2sparesMedios(self):
        b = bolos.bolos()
        a = b.calculadora([3,3,3,3,3,7,8,2,3,3,3,3,3,3,3,3,3,3,3,3])
        self.assertEqual(a, 79)
    #No se puede hacer tirada que sume más de 10 !!!!!+
    def test_sparFinal(self):
        b = bolos.bolos()
        a = b.calculadora([3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,7,3])
        self.assertEqual(a, 67)

    def test_sparYStrike(self):
        b = bolos.bolos()
        a = b.calculadora([3,3,3,3,3,7,8,2,3,3,3,3,10,3,3,3,3,3,3])
        self.assertEqual(a, 89)
    
    def test_sparYStrikeFinal(self):
        b =bolos.bolos()
        a = b.calculadora([3,3,3,3,3,7,8,2,3,3,3,3,10,3,3,3,3,10,3,3])
        self.assertEqual(a, 99)

    def test_3pleYSpar(self):
        b = bolos.bolos()
        a = b.calculadora([3,3,3,3,3,7,8,2,3,3,3,3,10,3,3,3,3,10,10,10])
        self.assertEqual(a,113)
    
    def test_2bleYSpar(self):
        b = bolos.bolos()
        a = b.calculadora([3,3,3,3,3,7,8,2,3,3,3,3,10,3,3,3,3,10,10,3])
        self.assertEqual(a,106)

    def test_2blePlenoFinal(self):
        b = bolos.bolos()
        a = b.calculadora([3,3,3,3,3,3,3,3,3,3,3,3,10,3,3,3,3,10,10,3])
        self.assertEqual(a,87)
    
    def test_2blePlenoFinal2(self):
        b = bolos.bolos()
        a = b.calculadora([3,3,3,3,3,3,3,3,3,3,3,3,10,3,3,3,3,10,3,10])
        self.assertEqual(a,87)
    
    def test_SparFinalYPlenoMedio(self):
        b = bolos.bolos()
        a = b.calculadora([3,3,3,3,3,3,3,3,3,3,10,3,3,3,3,3,3,3,7,3])
        self.assertEqual(a, 77)
    
    def test_SparYPleno(self):
        b = bolos.bolos()
        a = b.calculadora([3,3,3,3,10,3,3,3,3,3,3,8,2,3,3,3,3,3,3])
        self.assertEqual(a, 77)
    
    def test_todoPlenos(self):
        b = bolos.bolos()
        a = b.calculadora([10,10,10,10,10,10,10,10,10,10,10,10])
        self.assertEqual(a , 300)

    def test_pruebaRara(self):
        b = bolos.bolos()
        a = b.calculadora([10,3,7,10,10,3,7,10,10,10,10,10,10,10])
        self.assertEqual(a, 253)

if __name__ == '__main__':
    unittest.main()

import unittest
from romanos import Romanos

class TestRomanos(unittest.TestCase):

    # Tests para el método convertir

    def test_numero_1(self):
        romanos = Romanos()
        self.assertEqual("I", romanos.convertir(1))
    
    def test_numero_2(self):
        romanos = Romanos()
        self.assertEqual("II", romanos.convertir(2))

    def test_numero_5(self):
        romanos = Romanos()
        self.assertEqual("V", romanos.convertir(5))
    
    def test_numero_6(self):
        romanos = Romanos()
        self.assertEqual("VI", romanos.convertir(6))
    
    def test_numero_10(self):
        romanos = Romanos()
        self.assertEqual("X", romanos.convertir(10))
    
    def test_numero_11(self):
        romanos = Romanos()
        self.assertEqual("XI", romanos.convertir(11))
    
    def test_numero_15(self):
        romanos = Romanos()
        self.assertEqual("XV", romanos.convertir(15))
    
    def test_numero_18(self):
        romanos = Romanos()
        self.assertEqual("XVIII", romanos.convertir(18))
    
    def test_numero_37(self):
        romanos = Romanos()
        self.assertEqual("XXXVII", romanos.convertir(37))

    def test_numero_4(self):
        romanos = Romanos()
        self.assertEqual("IV", romanos.convertir(4))
    
    def test_numero_14(self):
        romanos = Romanos()
        self.assertEqual("XIV", romanos.convertir(14))
    
    def test_numero_24(self):
        romanos = Romanos()
        self.assertEqual("XXIV", romanos.convertir(24))
    
    def test_numero_9(self):
        romanos = Romanos()
        self.assertEqual("IX", romanos.convertir(9))
    
    def test_numero_39(self):
        romanos = Romanos()
        self.assertEqual("XXXIX", romanos.convertir(39))
    
    def test_numero_50(self):
        romanos = Romanos()
        self.assertEqual("L", romanos.convertir(50))
    
    def test_numero_77(self):
        romanos = Romanos()
        self.assertEqual("LXXVII", romanos.convertir(77))
    
    def test_numero_40(self):
        romanos = Romanos()
        self.assertEqual("XL", romanos.convertir(40))
    
    def test_numero_49(self):
        romanos = Romanos()
        self.assertEqual("XLIX", romanos.convertir(49))

    def test_numero_100(self):
        romanos = Romanos()
        self.assertEqual("C", romanos.convertir(100))
    
    def test_numero_186(self):
        romanos = Romanos()
        self.assertEqual("CLXXXVI", romanos.convertir(186))
    
    def test_numero_99(self):
        romanos = Romanos()
        self.assertEqual("XCIX", romanos.convertir(99))
    
    def test_numero_294(self):
        romanos = Romanos()
        self.assertEqual("CCXCIV", romanos.convertir(294))
    
    def test_numero_249(self):
        romanos = Romanos()
        self.assertEqual("CCXLIX", romanos.convertir(249))
    
    def test_numero_500(self):
        romanos = Romanos()
        self.assertEqual("D", romanos.convertir(500))
    
    def test_numero_777(self):
        romanos = Romanos()
        self.assertEqual("DCCLXXVII", romanos.convertir(777))
    
    def test_numero_400(self):
        romanos = Romanos()
        self.assertEqual("CD", romanos.convertir(400))
    
    def test_numero_499(self):
        romanos = Romanos()
        self.assertEqual("CDXCIX", romanos.convertir(499))
    
    def test_numero_1000(self):
        romanos = Romanos()
        self.assertEqual("M", romanos.convertir(1000))
    
    def test_numero_1865(self):
        romanos = Romanos()
        self.assertEqual("MDCCCLXV", romanos.convertir(1865))
    
    def test_numero_2024(self):
        romanos = Romanos()
        self.assertEqual("MMXXIV", romanos.convertir(2024))
    
    def test_numero_999(self):
        romanos = Romanos()
        self.assertEqual("CMXCIX", romanos.convertir(999))
    
    def test_numero_3999(self):
        romanos = Romanos()
        self.assertEqual("MMMCMXCIX", romanos.convertir(3999))
    
    # Tests excepciones
    def test_pasar_numero_negativo(self):
        romanos = Romanos()
        with self.assertRaises(ValueError):
            romanos.convertir(-7)
    
    def test_pasar_tipo_dato_erroneo(self):
        romanos = Romanos()
        with self.assertRaises(ValueError):
            romanos.convertir("8")
        

if __name__ == '__main__':
    unittest.main()
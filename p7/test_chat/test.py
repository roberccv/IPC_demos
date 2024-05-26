import unittest
from serv7 import Servidor

class TestServidor(unittest.TestCase):
    
    
    def test_verificación_usuario_registrado(self):
        servidor = Servidor()
        servidor.añadir_usuario_no_registrado('usuario1', b'1234')
        #Lo registro
        passKey = servidor.comprobar_contraseña_es_correcta('usuario1', b'1234')
        #pruebo que la contraseña coincide con la ya registrada para el usuario
        self.assertEqual(passKey, b'ok')

    def test_verificación_usuario_registrado_mal(self):
        servidor = Servidor()
        servidor.añadir_usuario_no_registrado('usuario1', b'1234')
        #Lo registro
        passKey = servidor.comprobar_contraseña_es_correcta('usuario1', b'124')
        #pruebo que la contraseña coincide con la ya registrada para el usuario
        self.assertEqual(passKey, b'incorrecto')

    def test_verificación_usuario_no_registrado(self):
        servidor = Servidor()
        servidor.gestionar_usuario('usuario1', b'1234')
        self.assertIn('usuario1', servidor.obtener_usuarios())
        

if __name__ == '__main__':
    unittest.main()
import unittest
from cli7 import Cliente

class TestCliente(unittest.TestCase):
    
    
    def test_conexion_usuario_unica(self):
        cliente = Cliente()
        s = cliente.crear_y_conectar_socket()
        confirmacion = cliente.enviar_nombre_usuario(s, "usuario_test_1")
        self.assertEqual(confirmacion, b'unico')
        s.close()
    
    def test_conexion_usuario_existente(self):
        cliente = Cliente()
        s = cliente.crear_y_conectar_socket()
        cliente.enviar_nombre_usuario(s, "usuario_test_2")
        cliente.enviar_contraseña(s, "contrasena_test_2")

        cliente2 = Cliente() 
        s2 = cliente2.crear_y_conectar_socket()
        confirmacion = cliente2.enviar_nombre_usuario(s2, "usuario_test_2")
        self.assertEqual(confirmacion, b'rechazado')
        s2.close()
        s.close()
     
    def test_conexion_con_contraseña_nuevo(self):
        cliente = Cliente()
        s = cliente.crear_y_conectar_socket()
        cliente.enviar_nombre_usuario(s, "usuario_test_3")
        confirmacion = cliente.enviar_contraseña(s, "contrasena_test_3")
        self.assertEqual(confirmacion, b'correcto')
        s.close()

    def test_conexion_con_contraseña_existente(self):
        cliente = Cliente()
        s = cliente.crear_y_conectar_socket()
        cliente.enviar_nombre_usuario(s, "usuario_test_4")
        cliente.enviar_contraseña(s, "contrasena_test_4")
        s.close()
        s = cliente.crear_y_conectar_socket()
        cliente.enviar_nombre_usuario(s, "usuario_test_4")
        confirmacion = cliente.enviar_contraseña(s, "contrasena_test_4")
        self.assertEqual(confirmacion, b'correcto')
        s.close()
        
        

    




if __name__ == '__main__':
    unittest.main()
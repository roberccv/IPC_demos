import unittest
import subprocess
import cliserv2

class TestPipes(unittest.TestCase):
    
    def test_crear_proceso_serv2(self):
        c = cliserv2.cliserv2()
        c.crear_procesos()
        self.assertIn('serv2', subprocess.check_output(['ps', '-e']).decode())

    def test_crear_proceso_cli2(self):
        c = cliserv2.cliserv2()
        c.crear_procesos()
        self.assertIn('cli2', subprocess.check_output(['ps', '-e']).decode())
        

if __name__ == '__main__':
    unittest.main()

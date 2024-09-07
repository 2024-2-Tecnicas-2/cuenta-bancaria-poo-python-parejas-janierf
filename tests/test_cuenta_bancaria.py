import unittest

class TestCuentaBancaria(unittest.TestCase):
    
    def setUp(self):
      
        self.cuenta = cuenta_bancaria("Juan Perez", "123456789", 1000)

  
    def test_getTitular(self):
        valor_esperado = "Juan Perez"
        valor_actual = self.cuenta.getTitular()
        self.assertEqual(valor_esperado, valor_actual)

    def test_getSaldo_inicial(self):
        valor_esperado = 1000
        valor_actual = self.cuenta.getSaldo()
        self.assertEqual(valor_esperado, valor_actual)
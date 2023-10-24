import unittest

class TestFunciones(unittest.TestCase):
    def test_calcular_monto_total(self):
        self.assertEqual(calcular_monto_total(100, 1000), 1650.0)

    def test_descontar_comision(self):
        self.assertEqual(descontar_comision(1000, 10), 900.0)

    def test_calcular_monto_plazo_fijo(self):
        self.assertEqual(calcular_monto_plazo_fijo(1000, 5), 1050.0)

if __name__ == "__main":
    unittest.main()

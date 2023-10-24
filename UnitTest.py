import unittest

class TestFunciones(unittest.TestCase):
    def test_calcular_monto_total(self):
        self.assertEqual(calcular_monto_total(1000), 1600.0)

    def test_descontar_comision(self):
        self.assertEqual(descontar_comision(1000, 10), (900.0, 100.0))

    def test_calcular_monto_plazo_fijo(self):
        self.assertEqual(calcular_monto_plazo_fijo(1000, 5), 1050.0)

if __name__ == "__main":
    unittest.main()


def calcular_monto_total(monto):
    impuesto_pais = 0.25  # Impuesto 25%
    ganancias = 0.35  # Impuesto 35%
    monto_total = monto + (monto * impuesto_pais) + (monto * ganancias)
    return monto_total

def descontar_comision(monto, comision_porcentaje):
    comision = monto * (comision_porcentaje / 100)
    monto_descontado = monto - comision
    return monto_descontado , comision

def calcular_monto_plazo_fijo(monto, interes):
    monto_final = monto + (monto * (interes / 100))
    return monto_final

print(calcular_monto_total(1000))
print(descontar_comision(50000, 1))
print(calcular_monto_plazo_fijo(50000, 10))

test = TestFunciones()
test.test_calcular_monto_plazo_fijo()
test.test_calcular_monto_total()
test.test_descontar_comision()
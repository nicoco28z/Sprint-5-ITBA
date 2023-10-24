class Cuenta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

#Metodos genericos Cuenta
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return f"Depósito de ${cantidad} realizado. Saldo actual: ${self.saldo}"
        else:
            return "La cantidad a depositar debe ser mayor que cero."

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            return f"Retiro de ${cantidad} realizado. Saldo actual: ${self.saldo}"
        else:
            return "Fondos insuficientes o cantidad inválida."

    def consultar_saldo(self):
        return f"Saldo actual: ${self.saldo}"

#Variantes de cuenta
class CajaAhorroPeso(Cuenta):
    def __init__(self, titular, saldo=0):
        super().__init__(titular, saldo)


class CajaAhorroDolar(Cuenta):
    def __init__(self, titular, saldo=0):
        super().__init__(titular, saldo)


class CuentaCorrientePeso(Cuenta):
    def __init__(self, titular, saldo=0):
        super().__init__(titular, saldo)

class CuentaCorrienteDolar(Cuenta):
    def __init__(self, titular, saldo=0):
        super().__init__(titular, saldo)

class CuentaInversion(Cuenta):
    def __init__(self, titular, saldo=0, interes=0.15):
        super().__init__(titular, saldo)
        self.interes = interes

    def aplicar_interes(self):
        self.saldo += self.saldo * self.interes
        return f"Intereses aplicados. Saldo actual: ${self.saldo}"
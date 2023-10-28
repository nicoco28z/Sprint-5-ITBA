class Tipo_Classic:
    def __init__(self):
        self.tarjeta_debito = 1
        self.chequera = 0

    def cuentas(self):
        return {"caja_de_ahorro": 1,
                "cuenta_corriente": 0,
                "cuenta_inversion": False}
    def retiros(self):
        return {"limite_de_retiro": True,
                "cantidad_limite_retiro": 5,
                "monto_limite_retiro": 10000}
    def tarjeta_credito(self):
        return False

class Tipo_Gold(Tipo_Classic):
    def __init__(self):
        super().__init__()
        self.chequera = 1
    def cuentas(self):
        return {"caja_de_ahorro": 2,
                "cuenta_corriente": 1,
                "cuenta_inversion": True}
    def retiros(self):
        return {"limite_de_retiro": False,
                "monto_limite_retiro": 20000}
    def tarjeta_credito(self):
        return {"cantidad_tarjeta_credito": 2,
                "tarjetas_disponibles":["Visa", "Mastercard"],
                "limite_extenciones": 5,
                "limite_un_pago":150000,
                "limite_en_cuotas":100000}

class Tipo_Black(Tipo_Gold):
    def __init__(self):
        super().__init__()
        self.tarjeta_debito = 5
        self.chequera = 2
    def cuentas(self):
        return {"caja_de_ahorro": 5,
                "cuenta_corriente": 3,
                "cuenta_inversion": True}
    def retiros(self):
        return {"limite_de_retiro": False,
                "monto_limite_retiro": 100000}
    def tarjeta_credito(self):
        # Diccionario con propiedades de tarjetas de Credito
        return {"cantidad_tarjeta_credito": 3,
                "tarjetas_disponibles":["Visa", "Mastercard", "American Express"],
                "limite_extenciones": 10,
                "limite_un_pago":500000,
                "limite_en_cuotas":600000}


#Caja de ahorro ejemplo
class Caja_de_Ahorro:
    def __init__(self):
        self.monto = 500000
    def retiro_efectivo(self, cantidad):
        self.monto -= cantidad
    def mostar_saldo(self):
        print(self.monto)

class Tipo_Classic:
    def __init__(self):
        self.tarjeta_debito = 1
        self.retiros_realizados = 0
        self.chequera = 0
        self.tipo = "Classic"

    def cuentas(self):
        return {
                "caja_de_ahorro": 1,
                "cargo_mensual" : 10, #Cargo que se le aplica al abrir una cuenta en dolares
                "cuenta_corriente": 0,
                "cuenta_inversion": False
                }
    def retiros(self):
        return {
                "cantidad_limite_retiro_cajero": 5,
                "comision_retiro" : 10, #Cargo que se aplica cuando quiere retirar más de las veces que tiene eprmitido
                "monto_limite_retiro": 10000
                }


    #Este cliente no tiene habilitadas las tarjetas de crédito
    def tarjeta_credito(self):
        return False

class Tipo_Gold(Tipo_Classic):
    def __init__(self):
        super().__init__()
        self.chequera = 1

    def cuentas(self):
        return {
                "caja_de_ahorro": 2,
                "cargo_mensual" : 10, #Cargo que se le aplica al abrir una cuenta en dolares
                "cuenta_corriente": 1,
                "cuenta_inversion": True
                }

    def retiros(self):
        return {
                "monto_limite_retiro": 20000
                }

    def tarjeta_credito(self):
        return {
                "cantidad_tarjeta_credito": 2,
                "tarjetas_disponibles":["Visa", "Mastercard"],
                "limite_extenciones": 5,
                "limite_un_pago":150000,
                "limite_en_cuotas":100000
                }

class Tipo_Black(Tipo_Gold):
    def __init__(self):
        super().__init__()
        self.tarjeta_debito = 5
        self.chequera = 2

    def cuentas(self):
        return {
                "caja_de_ahorro": 5,
                "cuenta_corriente": 3,
                "cuenta_inversion": True
                }

    def retiros(self):
        return {
                "monto_limite_retiro": 100000
                }

    def tarjeta_credito(self):
        # Diccionario con propiedades de tarjetas de Credito
        return {
                "cantidad_tarjeta_credito": 3,
                "tarjetas_disponibles":["Visa", "Mastercard", "American Express"],
                "limite_extenciones": 10,
                "limite_un_pago":500000,
                "limite_en_cuotas":600000
                }


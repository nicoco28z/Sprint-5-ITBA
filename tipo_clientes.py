class Tipo_Classic:
    def __init__(self):
        self.tarjeta_debito = 1
        self.caja_de_ahorro = 1
        self.cuenta_corriente = 0
        self.cuenta_inversion = 0
        self.limite_de_retiro = 5
        self.monto_limite_retiro = 10000

        self.tarjeta_credito = 0

class Tipo_Gold(Tipo_Classic):
    def __init__(self):
        super().__init__()
        # Cuentas
        self.caja_de_ahorro = 2
        self.cuenta_corriente = 1
        self.cuenta_inversion = True
        self.chequera = "capaz 1"
    def tarjeta_credito(self):
        return {"cantidad_tarjeta_credito": 2,
                "limite_extenciones": 5,
                "limite_un_pago":150000,
                "limite_en_cuotas":100000}

class Tipo_Black(Tipo_Gold):
    def __init__(self):
        super().__init__()

        self.caja_de_ahorro = 5
        self.cuenta_corriente = 3
        self.cuenta_inversion = True
        self.chequera = "capaz 2"
    def tarjeta_credito(self):
        return {"cantidad_tarjeta_credito": 3,
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

#Cliente Modelo para seguir
class Cliente():
    def __init__(self):
        self.tipo_cuenta = Tipo_Classic()
        self.tipo_cuenta_str = "classic"
        self.info_tarjetas = self.tipo_cuenta.tarjeta_credito()
        self.cuentas = [Caja_de_Ahorro()]
    def upgradear(self):
        if self.tipo_cuenta_str == "classic":
            self.tipo_cuenta = Tipo_Gold()
            self.tipo_cuenta_str = "gold"
    def __str__(self) -> str:
        return self.tipo_cuenta_str
    def crear_cuenta(self):
        if len(self.cuentas) < self.tipo_cuenta.caja_de_ahorro:
            print("Cuenta Creada")
            self.cuentas.append(Caja_de_Ahorro())
        else:
            print("No capo, no podes crear mas")
    def retirar_dinero(self, monto):
        if monto <= self.tipo_cuenta.monto_limite_retiro:
            print("Retiro exitoso")
            self.cuentas[0].retiro_efectivo(monto)
        else:
            print("No capo tu limite es:", self.tipo_cuenta.monto_limite_retiro)
    def consultar_saldo(self):
        self.cuentas[0].mostar_saldo()


cliente1 = Cliente()
cliente1.consultar_saldo()
cliente1.retirar_dinero(15000)
cliente1.retirar_dinero(10000)
cliente1.consultar_saldo()
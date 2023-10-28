class Tipo_Classic:
    def __init__(self):
        self.tarjeta_debito = 1
        self.chequera = False
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

#Cliente Modelo para seguir
class Cliente():
    def __init__(self):
        self._tipo_cuenta = Tipo_Classic()
        self._tipo_cuenta_str = "classic"
        self._cuentas = [Caja_de_Ahorro()]
        self._name = name
        self._surname = surname
        self._dni = dni
        self._idCliente = idCliente 
        self._ingresos = ingresos
        self._tarjetas = []

    

    #Getters
    def getName(self):
        return self._name

    def getSurname(self):
        return self._surname

    def getDni(self):
        return self._dni

    def getIdCliente(self):
        return self._idCliente

    def getIngresos(self):
        return self._ingresos

    def getTipoCuenta(self):
        return self._tipoCuenta

    def getTarjetas(self):
        return self._tarjetas

    #Setters
    def editName(self, a): 
        if( a.__len__() < 3): 
            print("El nombre debe tener al menos 3 caracteres")
            return
        self._name = a

    def editSurname(self, a): 
        if( a.__len__() < 3): 
            print("El apelido debe tener al menos 3 caracteres")
            return
        self._surname = a

    def editDni(self, d): 
        #Extender para validar que sean numeros
        if( d.__len__() != 8): 
            print("El DNI debe tener 8 caracteres")
            return
        self._dni = d

    def editIdCliente(self, i): 
        #Validacion cualquiera
        #Hay que validar que los id's no se repitan, no se si corresponde igual hacer eso
        if( i < 1): 
            print("El Id del Cliente no debe ser menor que 1")
            return
        self._idCliente = i

    def editIngresos(self, i): 
        if( i < 50): 
            print("Debe tener ingresos superiores a $50 pesos mensuales")
            return
        self._ingresos = i

    def editTipoCuenta(self, n): 
        if( n != "gold" and n != "black" and n != "classic"): 
            print("No debería poder cambiar asi xq si nomas jeje")
            return
        self._tipoCuenta = n


    def upgradear(self):
        if self._tipo_cuenta_str == "classic":
            self.tipo_cuenta = Tipo_Gold()
            self._tipo_cuenta_str = "gold"

    def __str__(self) -> str:
        return self._tipo_cuenta_str
    def crear_cuenta(self):
        if len(self._cuentas) < self._tipo_cuenta.caja_de_ahorro:
            print("Cuenta Creada")
            self._cuentas.append(Caja_de_Ahorro())
        else:
            print("No capo, no podes crear mas")
    def retirar_dinero(self, monto):
        if monto <= self._tipo_cuenta.monto_limite_retiro:
            print("Retiro exitoso")
            self._cuentas[0].retiro_efectivo(monto)
        else:
            print("No capo tu limite es:", self.tipo_cuenta.monto_limite_retiro)
    def consultar_saldo(self):
        self._cuentas[0].mostar_saldo()
    def alta_caja_de_ahorro_pesos(self):
        self._cuentas.append()


cliente1 = Cliente()
cliente1.consultar_saldo()
cliente1.retirar_dinero(15000)
cliente1.retirar_dinero(10000)
cliente1.consultar_saldo()

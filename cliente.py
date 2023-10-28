from cuentas import *
from tipo_clientes import *
from tarjetas import Tarjeta

class Cliente():
    def __init__(self, name, apellido, dni, idCliente, sueldo):
        self._tipo_cuenta = Tipo_Classic()
        self._cuentas = [CajaAhorroPeso(name + " " + apellido, 0)]
        self._name = name
        self._apellido = apellido
        self._dni = dni
        self._idCliente = idCliente 
        self._sueldo = sueldo
        self._tarjetas = []

    #Getters
    def getNombre(self):
        return self._name

    def getApellido(self):
        return self._apellido

    def getDni(self):
        return self._dni

    def getIdCliente(self):
        return self._idCliente

    def getSueldo(self):
        return self._sueldo

    def getTipoCuenta(self):
        return self._tipo_cuenta.tipo

    def getTarjetas(self):
        return self._tarjetas


    #Setters
    def editName(self, a): 
        if( a.__len__() < 3): 
            print("El nombre debe tener al menos 3 caracteres")
            return
        self._name = a

    def editApellido(self, a): 
        if( a.__len__() < 3): 
            print("El apelido debe tener al menos 3 caracteres")
            return
        self._apellido = a

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

    def editSueldo(self, i): 
        if( i < 50): 
            print("Debe tener sueldo superior a $50 pesos mensuales")
            return
        self._sueldo = i


    def mejorar_cliente(self):
        if self._tipo_cuenta.tipo == "classic":
            self.tipo_cuenta = Tipo_Gold()

    def __str__(self) -> str:
        return self._tipo_cuenta.tipo

    def crear_cuenta_cajaAhorro(self, moneda):
        if len(self._cuentas) < self._tipo_cuenta.cuentas()["caja_de_ahorro"]:
            if(moneda in ["dolar", "peso"]):
              self._cuentas.append(CajaAhorroPeso(name + " " + apellido, 0)) if moneda == "peso" else self._cuentas.append(CajaAhorroDolar(name + " " + apellido, 0))
              print("Cuenta Creada")
            else: print("La moneda ingresada es incorrecta")
        else:
            print("No capo, no podes crear mas")

    def retirar_dinero_cajero(self, monto):
        if monto <= self._tipo_cuenta.retiros()["monto_limite_retiro_cajero"]:
            print(self._cuentas[0].retirar(monto))
        else:
            print("Su limite de retiro por cajero es de: ", self._tipo_cuenta.retiros()["monto_limite_retiro_cajero"])

    def retirar_dinero(self, monto):
        print(self._cuentas[0].retirar(monto))

    def consultar_saldo(self):
        print(self._cuentas[0].consultar_saldo())

    def depositar(self, monto):
        print(self._cuentas[0].depositar(monto))

  #REVISAR
    def alta_caja_de_ahorro_pesos(self):
        self._cuentas.append()


c1 = Cliente("Aldo", "Andres", "44614368", 1, 30000)
print(c1.getNombre() + " " + c1.getApellido())
c1.consultar_saldo()
c1.retirar_dinero(15000)
c1.depositar(20000)
c1.retirar_dinero(10000)
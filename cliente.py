from cuentas import *
from tipo_clientes import *
from tarjetas import *
from chequera import Chequera
from datetime import datetime

class Cliente():
    def __init__(self, name, apellido, dni, idCliente, sueldo):
        self._tipo_cuenta = Tipo_Classic()
        self._cuentas = [CajaAhorroPeso(name + " " + apellido, 0)]
        self._name = name
        self._apellido = apellido
        self._dni = dni
        self._idCliente = idCliente 
        self._sueldo = sueldo
        self.chequeras = []
        self.movimientos = []
        self._tarjetas_credito = []
        self._tarjeta_debito = []


    #Getters
    def getNombre(self):
        return self._name

    def getApellido(self):
        return self._apellido

    def getDni(self):
        return self._dni

    def getIdCliente(self):
        return self._idCliente

    def getIngresos(self):
        return self._ingresos

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

    def editIngresos(self, i): 
        if( i < 50): 
            print("Debe tener ingresos superiores a $50 pesos mensuales")
            return
        self._ingresos = i


    def upgradear(self):
        if (self._tipo_cuenta.tipo == "Classic"):
            self._tipo_cuenta = Tipo_Gold()
            print(f"Cuenta mejorada a {self._tipo_cuenta.tipo}")
        elif (self._tipo_cuenta.tipo == "Gold"):
            self._tipo_cuenta = Tipo_Black()
            print(f"Cuenta mejorada a {self._tipo_cuenta.tipo}")
        elif (self._tipo_cuenta.tipo == "Black"):
            print("Su cuenta ya tiene el mejor rango posible.")

    def __str__(self):
        return self._tipo_cuenta.tipo

    def crear_cuenta_cajaAhorro(self, moneda):
        if len(self._cuentas) < self._tipo_cuenta.cuentas()["caja_de_ahorro"]:
            if(moneda in ["dolar", "peso"]):
                self._cuentas.append(CajaAhorroPeso(self._name + " " + self._apellido, 0)) if moneda == "peso" else self._cuentas.append(CajaAhorroDolar(self._name + " " + self._apellido, 0))
                print("Cuenta Creada")
            else: print("La moneda ingresada es incorrecta")
            
        else:
            print("No puede agregar otra cuenta")

    def crear_cuenta_corriente(self, moneda):
        if len(self._cuentas) < self._tipo_cuenta.cuentas()["caja_corriente"]:
            if(moneda in ["dolar", "peso"]):
                self._cuentas.append(CuentaCorrientePeso(self._name + " " + self._apellido, 0)) if moneda == "peso" else self._cuentas.append(CuentaCorrienteDolar(self._name + " " + self._apellido, 0))
                print("Cuenta Creada")
            else: print("La moneda ingresada es incorrecta")
            
        else:
            print("No puedes agregar otra cuenta")

    def retirar_dinero_cajero(self, monto):
        if monto <= self._tipo_cuenta.retiros()["monto_limite_retiro_cajero"]:
            bandera = self._cuentas[0].retirar(monto)
            if bandera:
                print('Retiro de cajero exitoso')
            else:
                print("Su saldo es insuficiente")

            dic = {
                    "estado": "ACEPTADA" if bandera else "RECHAZADA",
                    "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
                    "cuentaNumero": self._tipo_cuenta.id,
                    "permitidoActualParaTransaccion": self._tipo_cuenta.retiros()["monto_limite_retiro"],
                    "monto": monto,
                    "fecha": datetime.now(),
                    "numero": len(self.movimientos["transacciones"]) + 1
                    }
            self.movimientos["transacciones"].append(dic)

        else:
            print("Tu limite es:", self._tipo_cuenta.retiros()["monto_limite_retiro_cajero"])

    def consultar_saldo(self):
        print(self._cuentas[0].consultar_saldo())

    def depositar(self, monto):
        print(self._cuentas[0].depositar(monto))
        dic = {
                "estado": "ACEPTADA",
                "tipo": "DEPOSITO",
                "cuentaNumero": self._tipo_cuenta.id,
                "permitidoActualParaTransaccion": "INDEFINIDO",
                "monto": monto,
                "fecha": datetime.now(),
                "numero": len(self.movimientos["transacciones"]) + 1
                }
        self.movimientos["transacciones"].append(dic)
    
    def solicitar_tarjeta_debito(self):
        if len(self._tarjeta_debito) < self._tipo_cuenta.tarjeta_debito:
            self._tarjeta_debito.append(Tarjeta_Debito())
            print("Tarjeta de debito solicitada.")
        else:
            print("Usted no puede solicitar mas tarjetas de debito.")

    def solicitar_tarjeta_credito(self, tipo):
        props = self._tipo_cuenta.tarjeta_credito()
        if props:
            if tipo in self._tipo_cuenta.tarjetas_credito_disponibles:
                self._tipo_cuenta.tarjetas_credito_disponibles.remove(tipo)
                self._tarjetas_credito.append(Tarjeta_Credito(tipo))
            else:
                print("No dispones de este tipo de tarjeta de credito.")
        else:
            print("No dispones de tarjetas de credito.")
    
    def compra_en_cuotas(self, monto, tipo):
        props = self._tipo_cuenta.tarjeta_credito()
        if self._tarjetas_credito:
            bandera = monto <= props["limite_en_cuotas"]
            if bandera:
                print("Compra Exitosa.")
            else:
                print("El monto maximo para compra en cuotas es de:", props["limite_en_cuotas"])
            
            dic = {
                "estado": "ACEPTADA" if bandera else "RECHAZADA",
                "tipo": "COMPRA_EN_CUOTAS_TARJETA_" + tipo,
                "cuentaNumero": self._tipo_cuenta.id,
                "permitidoActualParaTransaccion": "NO TIENE PERMISOS" if props else props["limite_en_cuotas"],
                "monto": monto,
                "fecha": datetime.now(),
                "numero": len(self.movimientos["transacciones"]) + 1
                }
            self.movimientos["transacciones"].append(dic)

        else:
            print("Usted no posee tarjeta de credito.")

    def compra_en_un_pago(self, monto, tipo):
        props = self._tipo_cliente.tarjeta_credito()
        if self._tarjetas_credito:
            bandera = monto <= props["limite_un_pago"]
            if bandera:
                print("Compra Exitosa.")
            else:
                print("El monto maximo para compra en un pago es de:", props["limite_un_pago"])
            
            dic = {
                "estado": "ACEPTADA" if bandera else "RECHAZADA",
                "tipo": "COMPRA_TARJETA_CREDITO_" + tipo,
                "cuentaNumero": self._tipo_cuenta.id,
                "permitidoActualParaTransaccion": "NO TIENE PERMISOS" if props else props["limite_en_cuotas"],
                "monto": monto,
                "fecha": datetime.now(),
                "numero": len(self.movimientos["transacciones"]) + 1
                }
            self.movimientos["transacciones"].append(dic)

        else:
            print("Usted no posee tarjeta de credito.")
    
    def getTarjetasDebito(self):
        return self._tarjeta_debito

    def getTarjetasCredito(self):
        return self._tarjetas_credito
    
    def solicitar_chequera(self):
        if self.chequeras <= self._tipo_cuenta.chequera:
            self.chequeras.append(Chequera(self._idCliente, len(self.chequeras) + 1))
            print("Chequera agregada")
        else:
            print("No puede agregar otra chequera")
    
    def comprar_dolares(pesos):
        impuesto_pais = 0.45  # Impuesto 45%
        ganancias = 0.55  # Impuesto 55%
        valReal = pesos - (pesos * impuesto_pais) - (pesos * ganancias)
        dolares = valReal / 1000
        return dolares
    
    def venta_dolares(dolares):
        pesos = dolares * 1000
        return pesos



c1 = Cliente("Aldo", "Andres", "44614368", 1, 30000)
print(c1.getNombre() + " " + c1.getApellido())
c1.consultar_saldo()
c1.retirar_dinero(15000)
c1.depositar(20000)
c1.retirar_dinero(10000)
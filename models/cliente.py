import unittest

class Cliente:
  def __init__(self, name, surname, dni, idCliente, ingresos = 0, tipoCuenta = "classic"):
    #¿Habría que ponerlos como privados?
    self._name = name
    self._surname = surname
    self._dni = dni
    self._idCliente = idCliente 
    self._ingresos = ingresos
    self._tipoCuenta = tipoCuenta
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
    return self.__tarjetas

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
  


  def presentarse(self):
    print(f"Hola, soy {self._name} {self._surname}")

  def calcular_monto_total(self, precioDolar, cantDolar):
    #Valor y porcentaje de los impuestos
    impGanancias = 1980000
    porcentajeGanancias = 1.3
    porcentajePais = 1.3

    #Se calcula el importe mínimo a pagar
    montoTotal = cantDolar * precioDolar * porcentajePais

    #Se verifica si el cliente debe o no pagar imp a Ganancias
    if(self._ingresos > impGanancias):
      montoTotal *= porcentajeGanancias

    return montoTotal

class TestCalcularMontoTotal(unittest.TestCase):

    def test_calculo_monto_total_sin_impuestos_ganancia(self):
        # Prueba cuando los ingresos son menores que el límite para impuestos_ganancia
        precio_dolar = 100  # Precio dólar
        cantidad_dolar = 10  # Cantidad dólares
        ingresos = 1000  # Ingresos cliente

        c = Cliente("Aldo", "Andres", "44614368", 1)
        c.editIngresos(ingresos)
        monto_total = c.calcular_monto_total(precio_dolar, cantidad_dolar)

        # El monto total debe ser igual al precio_dolar * cantidad_dolar * porcentajePais
        self.assertEqual(monto_total, precio_dolar * cantidad_dolar * 1.3)

    def test_calculo_monto_total_con_impuestos_ganancia(self):
      # Prueba cuando los ingresos superan el límite para impuestos_ganancia
      precio_dolar = 100  # Precio del dólar
      cantidad_dolar = 10  # Cantidad de dólares
      ingresos = 2000000  # Ingresos del cliente
    
      c = Cliente("Aldo", "Andres", "44614368", 1)
      c.editIngresos(ingresos)
      monto_total = c.calcular_monto_total(precio_dolar, cantidad_dolar)

        # El monto total debe ser igual al precio_dolar * cantidad_dolar * porcentajePais * porcentajeGanancias
      self.assertEqual(monto_total, precio_dolar * cantidad_dolar * 1.3 * 1.3)

if __name__ == '__main__':
    unittest.main()
  
c = Cliente("Aldo", "Andres", "44614368", 1)
c.editIngresos(1980080)
print(c.calcular_monto_total(100, 10))


from cuentas import *
from tipo_clientes import *
from tarjetas import Tarjeta
from cliente import Cliente

class ProgramaBanco:
    def __init__(self, cliente):
        self.cliente = cliente

    def datos_cliente(self):
        print("\nNombre:",cliente.getNombre(),
            "\nApellido:",cliente.getApellido(),
            "\nDNI:",cliente.getDni(),
            "\nCuenta:",cliente.getTipoCuenta())
        
    def editar_datos_cliente(self):
        while True:
            print("\nMenú:"
                "\n1. Modificar Nombre:"
                "\n2. Modificar Apellido"
                "\n3. Modificar Ingresos mensuales"
                "\n4. Cancelar.")
            opciones = input("\nQue dato desea actualizar:")

            match opciones:
                case "1":
                    nombreActualizado = input("Indique su nombre ACTUALIZADO: ")
                    cliente.editName(nombreActualizado)
                    print(f"\nNombre actualizado correctamente: {nombreActualizado}")
                    break
                case "2":
                    apellidoActualizado = input("Indique su apellido ACTUALIZADO: ")
                    cliente.editSurname(apellidoActualizado)
                    print(f"\nApellido actualizado correctamente: {apellidoActualizado}")
                    break
                case "3":
                    ingresosActualizado = int(input("Indique sus ingresos ACTUALIZADOS: "))
                    cliente.editIngresos(ingresosActualizado)
                    print(f"\nIngresos actualizados correctamente: {ingresosActualizado}")
                    break
                case "4":
                    break

    def mostrar_menu(self):
        print("\nMenú:"
            "\n1. Mis datos"
            "\n2. Actualizar mis datos"
            "\n3. Consultar saldo"
            "\n4. Depositar dinero"
            "\n5. Retirar dinero"
            "\n6. Crear caja"
            "\n7. Mejorar cuenta"
            "\n8. Salir")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Selecciona una opción (1, 2, 3, 4, 5): ")

            match opcion:

                case "1":
                    self.datos_cliente()
                case "2":
                    self.editar_datos_cliente()
                case "3":
                    self.cliente.consultar_saldo()
                case "4":
                    deposito = int(input("Cuanto dinero desea depositar: "))
                    self.cliente.depositar(deposito)
                case "5":
                    monto = int(input("Ingrese el monto a retirar: "))
                    self.cliente.retirar_dinero(monto)
                case "6":
                    self.cliente.crear_cuenta_cajaAhorro("peso")
                case "7":
                    self.cliente.upgradear()
                case "8":
                    break
                case _:
                    print("Opción no válida. Por favor, elige una opción válida.")
            
if __name__ == "__main__":
    cliente = Cliente("Nico", "Andres", "44614368", 1, 30000)
    programa = ProgramaBanco(cliente)
    programa.ejecutar()
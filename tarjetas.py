import random

class Tarjeta:
    def generar_numero(self, tipo):
        if tipo not in ['Visa', 'Mastercard', 'American Express']:
            raise ValueError("Tipo de tarjeta no válido")

        if tipo == 'Visa':
            numero = '4'
            for _ in range(15):
                numero += str(random.randint(0, 9))
        elif tipo == 'Mastercard':
            numero = '3'
            for _ in range(15):
                numero += str(random.randint(0, 9))
        elif tipo == 'American Express':
            numero = '2' + random.choice(['4', '7'])
            for _ in range(13):
                numero += str(random.randint(0, 9))
        return numero

tarjeta = Tarjeta()
tipo_elegido = input("Elija el tipo de tarjeta (visa, mastercard, american")
numero_tarjeta = tarjeta.generar_numero(tipo_elegido)

print(f'Tipo: {tipo_elegido}')
print(f'Número: {numero_tarjeta}')

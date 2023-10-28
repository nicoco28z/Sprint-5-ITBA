import random

class Tarjeta():

    def generar_numero(self, tipo):
        if tipo not in ['Visa', 'Mastercard', 'American Express']:
            print("Tipo de tarjeta no válido")

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

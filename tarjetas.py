import random

class Tarjeta_Debito():
    def __init__(self):
        numero = '5'
        for _ in range(15):
            numero += str(random.randint(0, 9))

class Tarjeta_Credito():
    def __init__(self, tipo) -> None:
        self._extenciones = []

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

        self.numero_tarjeta = numero

    def consultar_extenciones(self):
        return self._extenciones

    def solicitar_extencion(self):
        self._extenciones.append("Extencion")
        print("Extencion creada.")
    

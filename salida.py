a = {"numero": 100001,
    "nombre": "Nicolas",
    "apellido": "Gaston",
    "dni": "29494777",
    "tipo": "BLACK",
    "transacciones": [{"estado": "ACEPTADA",
                        "tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
                        "cuentaNumero": 190,
                        "permitidoActualParaTransccion": 9000,
                        "monto": 1000,
                        "fecha": "10/10/2022 16: 00: 55",
                        "numero": 1},
                        {"ESTADO": "RECHAZADA",
                        "tipo": "COMPRA_EN_CUOTAS_TARJETA_VISA",
                        "permitidoActualParaTransccion": 9000,
                        "monto": 750000,
                        "fecha": "10/10/2022 16: 14: 35",
                        "numero": 2}]}


with open('salida.html', 'w') as salida:

    salida.write("<!DOCTYPE html>\n")
    salida.write('<html lang="en">\n')
    salida.write("<head>\n")
    salida.write('\t<meta charset="UTF-8">\n')
    salida.write('\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    salida.write("\t<title>Document</title>\n")
    salida.write("</head>\n")
    salida.write("<body>\n")
    salida.write(f"<p>{a}</p>\n")
    salida.write("</body>\n")
    salida.write("</html>\n")
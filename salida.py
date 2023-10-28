import json

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

formatted_json = json.dumps(a, indent=4) # convierte el diccionario en un archivo json

with open('salidasHTML/salida.html', 'w') as salida: #Pendiente: agregar varias salidas

    salida.write("<!DOCTYPE html>\n")
    salida.write('<html lang="es">\n')
    salida.write("<head>\n")
    salida.write('\t<meta charset="UTF-8">\n')
    salida.write('\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    salida.write("\t<title>Document</title>\n")
    salida.write("</head>\n")
    salida.write("<body>\n")
    salida.write(f"<pre>{formatted_json}</pre>\n") # la etiqueta pre impide que se formatee el texto, esto es para respetar la consigna
    salida.write("</body>\n")
    salida.write("</html>\n")
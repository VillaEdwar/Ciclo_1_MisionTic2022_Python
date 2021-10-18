#Utilizando python, escriba una función que 
# reciba como parámetro un diccionario en el cuál 
# las llaves son los nombres de las variables mencionadas anteriormente. Retorne un nuevo 
# diccionario con las llaves “banco”, “usuario” y “mensaje” dónde esta última tenga como 
# valor una variable de tipo “str” que muestre el mensaje de cada una de las condiciones.

#definicion de funcion
def cajero(informacion: dict)->dict: # Debe devolver un diccionario
    #str
    p1 = str(informacion["banco"])
    p2 = str(informacion["usuario"])
    #int
    p3 = int(informacion["clave"])
    p4 = int(informacion["retiro"])
    p5 = int(informacion["saldo_inicial"])
    p6 = int(informacion["nuevo_saldo"])
    mensaje = str("mensaje")
    # Creacion del diccionario de salida
    nuevo_diccionario:dict = {
        "banco": p1,
        "usuario": p2,
        "mensaje": mensaje
    }
    # Verifica si la clave es correcta
    if p3 == 1234:
        # Condiciona si el saldo a retirar es mayor a 200000
        if p4 > 200000: 
            p4 = p4 + 2000
            # Si el saldo inicial es menor que el saldo a retirar entonces continua
            if p4 <= p5:
                # El nuevo saldo sera
                p6 = p5 - p4
                # Asigna un nuervo valor a la llave "mensaje" en el diccionario informacion
                nuevo_diccionario["mensaje"] = "Su saldo actual es: {} Muchas Gracias!".format(p6)
            else:
                # Asigna un nuervo valor a la llave "mensaje" en el diccionario informacion
                nuevo_diccionario["mensaje"] = "El valor solicitado más el costo de la transacción es mayor al saldo"
        else:
            # Si el saldo inicial es menor que el saldo a retirar entonces continua
            if p4 <= p5:
                p6 = p5 - p4
                # Asigna un nuervo valor a la llave "mensaje" en el diccionario informacion
                nuevo_diccionario["mensaje"] = "Su saldo actual es: {} Muchas Gracias!".format(p6)
            else:
                # Asigna un nuervo valor a la llave "mensaje" en el diccionario informacion
                nuevo_diccionario["mensaje"] = "El valor solicitado es mayor al saldo actual"
    else:
        # Asigna un nuervo valor a la llave "mensaje" en el diccionario informacion
        nuevo_diccionario["mensaje"] = "Clave incorrecta"

    return nuevo_diccionario


informacion:dict = {
        "banco": "Banco ABC",
        "usuario": "Carlos",
        "clave": 1234,
        "retiro": 798000,
        "saldo_inicial": 800000,
        "nuevo_saldo": 0
}
print(cajero(informacion))
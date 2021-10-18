#Utilizando python, escriba una función que 
# reciba como parámetro un diccionario en el cuál 
# las llaves son los nombres de las variables mencionadas anteriormente. Retorne un nuevo 
# diccionario con las llaves “banco”, “usuario” y “mensaje” dónde esta última tenga como 
# valor una variable de tipo “str” que muestre el mensaje de cada una de las condiciones.


def cajero(p1: str, p2: str, p3: int, p4: int, p5: int, p6: int)->dict:
    informacion = {
        "banco": p1,
        "usuario":p2,
        "mensaje":""
    }
    if p3 == 1234:
        if p4 > 200000:
            p4 = p4 + 2000
            if p4 <= p5:
                p6 = p5-p4
                informacion ["mensaje"] = "su saldo actual es {} muchas gracias".format(p6)
                print("su saldo actual es: {}".format(p6))
            else:
                informacion ["mensaje"] = "el valor del costo mas el costo del valor es mayor al saldo"
        else:
            if p4 <= p5:
                p6 = p5 - p4
                informacion ["mensaje"] = "su saldo actual es {} muchas gracias".format(p6)
                print("su saldo actual es: {}".format(p6))
            else:
                print("el valor solicitado es mayor al saldo actual")
    else:
        informacion ["mensaje"] = "clave incorrecta"

    return print(informacion)
print(cajero("Banco ABC","Carlos", 1254,798000,800000,0))
'''
A continuacion vamos a calcular el factor de recoleccion
factor_recoleccion = str((a + b + c + d + e) * 0.10)
# A continuacion calculamos el promedio de recoleccion  
promedio_recoleccion = ((a + b + c + d + e)/5)
Calculo del promedio de las recolecciones redondeado a un decimal
promedio_dias_redondeado = round(promedio_recoleccion,1)
# A continuacion convertimos el resultado a cadena
promedio = str(promedio_dias_redondeado)
return "El factor de recolección es {} y el promedio de las recolecciones para la semilla de {} es de: {}".format(factor_recoleccion,semilla,promedio)
print(promedioRecoleccion("frijol", 1250, 1010, 800, 220, 530))
'''
#Reto 4
def max_transacciones_anuales (datos: dict) -> tuple:
    #Definiendo variables
    nombre = str()
    nit = str()
    url = str()
    transacciones = list()
    sede1 = str()
    sede2 = str()
    sede3 = str()
    sede4 = str()
    lista = list()

    #auxiliares
    cod_nit = str()
    promedio = int()

    #Acumuladores
    total = 0

    #Obteniendo el codigo
    #total numeros impares
    for i in range(len(nit)):
        #print(nit[i])
        numero = int(nit[i])
        if numero %2 == 1:
            total = total + numero

    #obteniendo el producto del total con numeros pares
    for i in range(len(nit)):
            #print(nit[i])
            numero = int(nit[i])
            if numero %2 == 0:
                producto = numero*total
                cadena_aux = str(producto)
                listando = list(cadena_aux)
                lista.append(listando)
                #parte_2 = "".join(lista)
                print(listando)
                print(lista)


    #obetniendo pares del nit
    num_pares = datos["01"]["nit"]

    #Recorrido de todas las transacciones en el año y asi obtener el promedio
    for k in datos:
        total = total + k[sede1] + k[sede2] + k[sede3] + k[sede4]

    #Inicializacion del diccionario






    #Tupla de salida
    tuple = (cod_nit, nombre, promedio)

    return total 


#Prueba
datos = {
    "01": {
        "nombre": "Ahorrar",
        "nit": "34545678",
        "url": "www.ahorrar.com.co",
        "transacciones": [
            {
                "enero": {
                    "sede1": 250,
                    "sede2": 200,
                    "sede3": 100,
                    "sede4": 150
                    }
            },
            {
                "febrero": {
                    "sede1": 200,
                    "sede2": 50,
                    "sede3": 200,
                    "sede4": 250
                    }
            },
            {
                "marzo": {
                    "sede1": 100,
                    "sede2": 500,
                    "sede3": 20,
                    "sede4": 250
                    }
            },
            {
                "abril": {
                    "sede1": 1000,
                    "sede2": 50,
                    "sede3": 200,
                    "sede4": 250
                    }
            },
            {
                "mayo": {
                    "sede1": 400,
                    "sede2": 500,
                    "sede3": 20,
                    "sede4": 250
                    }
            },
            {
                "junio": {
                    "sede1": 1000,
                    "sede2": 50,
                    "sede3": 200,
                    "sede4": 250
                    }
            },
            {
                "julio": {
                    "sede1": 300,
                    "sede2": 50,
                    "sede3": 2000,
                    "sede4": 150
                    }
            },
            {
                "agosto": {
                    "sede1": 100,
                    "sede2": 150,
                    "sede3": 200,
                    "sede4": 250
                    }
            },
            {
                "septiembre": {
                    "sede1": 100,
                    "sede2": 510,
                    "sede3": 1000,
                    "sede4": 250
                    }
            },
            {
                "octubre": {
                    "sede1": 100,
                    "sede2": 500,
                    "sede3": 100,
                    "sede4": 250
                    }
            },
            {
                "noviembre": {
                    "sede1": 100,
                    "sede2": 50,
                    "sede3": 100,
                    "sede4": 250
                    }
            },
            {
                "diciembre": {
                    "sede1": 100,
                    "sede2": 500,
                    "sede3": 100,
                    "sede4": 350
                    }
            }
        ]
    }
}

print(datos)
print (datos["01"])
print (datos["01"]["nombre"])
print (datos["01"]["nit"])
print (datos["01"]["url"])
print (datos["01"]["transacciones"])
print (datos["01"]["transacciones"][0])
print (datos["01"]["transacciones"][0]["enero"])
print (datos["01"]["transacciones"][0]["enero"]["sede1"])


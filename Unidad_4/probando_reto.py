''' #version prueba para aprender
nombre_del_banco = "Guardar"

#parte 1, obtener las primeras letras
Codigo = nombre_del_banco[0:3]
print(Codigo)

#parte 2, obtener los numeros con las condiciones
nit = str(34567123)
##print(nit)
#print(nit[0])
#print(nit[1])

lista=list()
total=0
for i in range(len(nit)):
    #print(nit[i])
    numero = int(nit[i])
    if numero %2 == 1:
        total = total + numero
        print(total)
        print("es impar: ", type(numero))
        #print(type(auxiliar))

cadena = ""
for i in range(len(nit)):
    #print(nit[i])
    numero = int(nit[i])
    
    if numero %2 == 0:
        producto = numero*total
        print(producto)
        cadena_aux = str(producto)
        lista.append(cadena_aux)
        print(lista)

cadena = "".join(lista)
print("-----------------")
print(lista)
print(cadena)

#parte 3, uniendo todas las partes
cod_nit = Codigo+cadena
print(cod_nit)
'''

#parte final
def max_transacciones_anuales (datos) -> str:
    promedio_transacciones:list = []
    for clave, valor in datos.items():
        total_transacciones: int = 0
        cont: int =0
        for transacciones in valor["transacciones"]:
            for mes, sedes in transacciones.items():
                for sede, ventas in sedes.items():
                    total_transacciones += ventas
                    cont += 1

        nombre_del_banco = valor["nombre"][0:3]

        #parte 1, obtener las primeras letras
        Codigo = nombre_del_banco[0:3]

        #parte 2, obtener los numeros con las condiciones
        nit = valor["nit"]
        lista=list()
        total=0

        for i in range(len(nit)):
            numero = int(nit[i])
            if numero %2 == 1:
                total = total + numero

        cadena = ""
        for i in range(len(nit)):
            numero = int(nit[i])
            
            if numero %2 == 0:
                producto = numero*total
                cadena_aux = str(producto)
                lista.append(cadena_aux)

        cadena = "".join(lista)

        return Codigo+cadena



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
#haciendo lo mismo pero en comprehension de listas

print(max_transacciones_anuales(datos))
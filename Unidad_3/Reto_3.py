# Funcion calcular ingresos

def calcular_ingresos(datos: list) -> dict:

    # Definicion de variables
    
    total = int()
    promp = int()
    promm = int()

    # Acumuladores
    total = 0
    sumap=0
    sumam=0

    # Contadores
    k=0
    i=0
    j=0

    # Diccionario de salida
    diccionario: dict = {
        "total": total,
        "promedio_seguro_persona": promp,
        "promedio_seguro_mascota": promm
    }

    # Recorrido para todos los valores a pagar de la lista
    for k in datos: 
        total = total + k["valor_a_pagar"]

    # Recorrido de cada elemento de la lista de manera especifica
    for recorrido in range(len(datos)):
        if datos[recorrido]["seguro"] == "persona":
            sumap = sumap + datos[recorrido]["valor_a_pagar"]
            i=i+1
            promp = sumap / i
            if promp != 0:
                promp = float(promm)

        elif datos[recorrido]["seguro"] == "mascota":
            sumam = sumam + datos[recorrido]["valor_a_pagar"]
            print(sumam)
            j=j+1
            promm = sumam / j
            if promm !=0:
                promm = float(promm)
            

    # Se haran los siguiesntes cambios en el diccionario de salida
    diccionario["total"] = total
    diccionario["promedio_seguro_persona"] = round(promp,1)
    diccionario["promedio_seguro_mascota"] = round(promm,1)
            
    return diccionario


'''
datos: list = [
    {
        "seguro": "persona",
        "valor_a_pagar": 32000
    },
    {
        "seguro": "persona",
        "valor_a_pagar": 25000
    },
    {
        "seguro": "persona",
        "valor_a_pagar": 32000
    },
    {
        "seguro": "persona",
        "valor_a_pagar": 18000
    },
    {
        "seguro": "persona",
        "valor_a_pagar": 25000
    },
    {
        "seguro": "persona",
        "valor_a_pagar": 33000
    },
    {
        "seguro": "persona",
        "valor_a_pagar": 28000
    }
]
print(calcular_ingresos(datos))
'''

'''
datos: list = [
    {
        "seguro": "persona",
        "valor_a_pagar": 20000
    },
    {
        "seguro": "mascota",
        "valor_a_pagar": 25000
    },
    {
        "seguro": "persona",
        "valor_a_pagar": 32000
    },
    {
        "seguro": "persona",
        "valor_a_pagar": 18000
    },
    {
        "seguro": "mascota",
        "valor_a_pagar": 5000
    },
    {
        "seguro": "persona",
        "valor_a_pagar": 33000
    },
    {
        "seguro": "mascota",
        "valor_a_pagar": 8000
    }
]
'''

datos: list =[
    {
        "seguro": "persona",
        "valor_a_pagar": 20000
    },
    {
        "seguro": "mascota",
        "valor_a_pagar": 25000
    },
    {
        "seguro": "persona",
        "valor_a_pagar": 32000
    },
    {
        "seguro": "persona",
        "valor_a_pagar": 18000
    },
    {
        "seguro": "mascota",
        "valor_a_pagar": 5000
    },
    {
        "seguro": "persona",
        "valor_a_pagar": 33000
    },
    {
        "seguro": "mascota",
        "valor_a_pagar": 8000
    }
]


print(calcular_ingresos(datos))
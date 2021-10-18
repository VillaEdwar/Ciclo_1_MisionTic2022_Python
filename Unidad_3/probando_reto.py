#funcion calcular ingresos

def calcular_ingresos(datos: list) -> dict:

    # Definicion de variables
    
    total = int()
    promp = float()
    promm = float()

    # Acumuladores
    total = 0
    sumap=0
    sumam=0

    # Contadores
    k=0
    i=0
    j=0

    # Recorrido para todos los valores a pagar de la lista
    for k in datos: 
        total = total + k["valor_a_pagar"]

    #Recorrido de cada elemento de la lista de manera especifica
    for recorrido in range(len(datos)):
        if datos[recorrido]["seguro"] == "persona":
            sumap = sumap + datos[recorrido]["valor_a_pagar"]
            i=i+1
            promp = round(sumap / i,1)

        elif datos[recorrido]["seguro"] == "mascota":
            sumam = sumam + datos[recorrido]["valor_a_pagar"]
            j=j+1
            promm = round(sumam / j,1)
            
    return {"total":total, "promedio_seguro_persona":promp, "promedio_seguro_mascota":promm}

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
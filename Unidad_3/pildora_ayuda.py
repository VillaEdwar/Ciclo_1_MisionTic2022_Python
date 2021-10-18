def calcular_ingresos(datos: list) -> dict:
    total = 0
    mensaje = "El saldo total es"
    # Estructura para recorrer la lista
    for i in datos: #las letras i del for no se declaran, solo es para hacer el recorrido
        total = total + i["valor_a_pagar"]
        #total += i["valor_a_pagar"]

    respuesta: dict = {
        "mensaje": mensaje,
        "total": total
    }
    return respuesta

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
print(calcular_ingresos(datos))
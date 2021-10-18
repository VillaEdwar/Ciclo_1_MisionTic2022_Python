#Reto 4

from functools import reduce

def max_transacciones_anuales (datos: dict) -> tuple:
    promedio_transacciones:list = []
    for clave, valor in datos.items():
        total_transacciones: int = 0
        cont: int =0
        for transacciones in valor["transacciones"]:
            for mes, sedes in transacciones.items():
                for sede, ventas in sedes.items():
                    total_transacciones += ventas
                    cont += 1

        nit = list(valor["nit"])

        pares = [int(x) for x in list(filter(lambda x: int(x) & 2 == 0, nit))]
        impares = [int(x) for x in list(filter(lambda x: int(x) & 2 == 1, nit))]

        codificacion = list(map(lambda n: n*(reduce(lambda acum=0, element=0: acum + element, impares)), pares))

        cod_nit = "".join(map(str,codificacion))

        codigo = valor["nombre"][0:3] + cod_nit
        promedio = lambda totalventas, cont: total_transacciones / cont
        tupla: tuple = (codigo, valor["nombre"], promedio(total_transacciones, cont))
        promedio_transacciones.append(tupla)
    
    return obtener_promedio_mayor(promedio_transacciones)

def obtener_promedio_mayor(promedio_transacciones: list) -> tuple:
    mayor = 0
    tupla =tuple()
    for nit, nombre, promedio in promedio_transacciones:
        if promedio > mayor:
            mayor = promedio
            tupla = (nit, nombre, round(promedio,2))
    return tupla

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

print(max_transacciones_anuales(datos))
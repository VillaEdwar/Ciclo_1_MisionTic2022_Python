
def mejor_promedio_anual(datos: dict) -> tuple:
    promedio_ventas: list = []
    for clave, valor in datos.items():
        total_ventas: int = 0
        cont: int = 0
        for ventas in valor["ventas"]:
            for mes, articulos in ventas.items():
                for articulo, precio in articulos.items():
                    total_ventas += precio
                    cont += 1
        promedio: float = round((total_ventas/cont), 2)
        codigo_unico: str = valor["nombre_sede"][0:2] + valor["direccion"][0:4]
        tupla: tuple = (codigo_unico, valor["nombre_sede"], promedio)
        promedio_ventas.append(tupla)

    return obtener_promedio_mayor(promedio_ventas)


def obtener_promedio_mayor(promedio_ventas: list) -> tuple:
    mayor = 0
    tupla = tuple()
    for codigo, nombre, promedio in promedio_ventas:
        if promedio > mayor:
            mayor = promedio
            tupla = (codigo, nombre, promedio)
    return tupla


# Caso 1
datos = {
    "Escra20": {
        "nombre_sede": 'Estadio',
        "direccion": 'cra20 #44-92',
        "ventas": [
            {
                "enero": {
                    "aseo": 1500000,
                    "frutas": 2450000,
                    "carnes": 8500000,
                    "lacteos": 1300000
                }
            },
            {
                "febrero": {
                    "aseo": 134000,
                    "frutas": 600000,
                    "carnes": 700000,
                    "lacteos": 900000
                }
            },
            {
                "marzo": {
                    "aseo": 1000000,
                    "frutas": 1400000,
                    "carnes": 1600000,
                    "lacteos": 1800000
                }
            },
            {
                "abril": {
                    "aseo": 1900000,
                    "frutas": 2450000,
                    "carnes": 1400000,
                    "lacteos": 300000
                }
            },
            {
                "mayo": {
                    "aseo": 1800000,
                    "frutas": 2750000,
                    "carnes": 1200000,
                    "lacteos": 200000
                }
            },
            {
                "junio": {
                    "aseo": 1700000,
                    "frutas": 2000000,
                    "carnes": 1900000,
                    "lacteos": 500000
                }
            },
            {
                "julio": {
                    "aseo": 1600000,
                    "frutas": 2780000,
                    "carnes": 1500000,
                    "lacteos": 700000
                }
            },
            {
                "agosto": {
                    "aseo": 1500000,
                    "frutas": 2250000,
                    "carnes": 1100000,
                    "lacteos": 200000
                }
            },
            {
                "septiembre": {
                    "aseo": 1100000,
                    "frutas": 2540000,
                    "carnes": 1200000,
                    "lacteos": 400000
                }
            },
            {
                "octubre": {
                    "aseo": 1400000,
                    "frutas": 2120000,
                    "carnes": 1400000,
                    "lacteos": 500000
                }
            },
            {
                "noviembre": {
                    "aseo": 1300000,
                    "frutas": 2230000,
                    "carnes": 1700000,
                    "lacteos": 200000
                }
            },
            {
                "diciembre": {
                    "aseo": 1000000,
                    "frutas": 2480000,
                    "carnes": 12500000,
                    "lacteos": 100000
                }
            }
        ]
    },
    "Pocll1": {
        "nombre_sede": 'Popular',
        "direccion": 'cll100 #90-14',
        "ventas": [
            {
                "enero": {
                    "aseo": 980000,
                    "frutas": 4200000,
                    "carnes": 940000,
                    "lacteos": 500000
                }
            },
            {
                "febrero": {
                    "aseo": 910000,
                    "frutas": 6400000,
                    "carnes": 140000,
                    "lacteos": 480000
                }
            },
            {
                "marzo": {
                    "aseo": 920000,
                    "frutas": 4300000,
                    "carnes": 240000,
                    "lacteos": 410000
                }
            },
            {
                "abril": {
                    "aseo": 980000,
                    "frutas": 4200000,
                    "carnes": 540000,
                    "lacteos": 402000
                }
            },
            {
                "mayo": {
                    "aseo": 920000,
                    "frutas": 4700000,
                    "carnes": 540000,
                    "lacteos": 980000
                }
            },
            {
                "junio": {
                    "aseo": 900000,
                    "frutas": 4600000,
                    "carnes": 650000,
                    "lacteos": 290000
                }
            },
            {
                "julio": {
                    "aseo": 890000,
                    "frutas": 4200000,
                    "carnes": 190000,
                    "lacteos": 720000
                }
            },
            {
                "agosto": {
                    "aseo": 130000,
                    "frutas": 9200000,
                    "carnes": 960000,
                    "lacteos": 870000
                }
            },
            {
                "septiembre": {
                    "aseo": 210000,
                    "frutas": 5400000,
                    "carnes": 180000,
                    "lacteos": 980000
                }
            },
            {
                "octubre": {
                    "aseo": 250000,
                    "frutas": 3400000,
                    "carnes": 140000,
                    "lacteos": 450000
                }
            },
            {
                "noviembre": {
                    "aseo": 430000,
                    "frutas": 1500000,
                    "carnes": 2500000,
                    "lacteos": 420000
                }
            },
            {
                "diciembre": {
                    "aseo": 560000,
                    "frutas": 8900000,
                    "carnes": 720000,
                    "lacteos": 400000
                }
            }
        ]
    }
}

print(mejor_promedio_anual(datos))


#-----------------------Caso 2------------------------------------
datos = {
    "Escra20": {
        "nombre_sede": 'Olimpico',
        "direccion": 'cra18 #45-92',
        "ventas": [
            {
                "enero": {
                    "aseo": 1500000,
                    "frutas": 2450000,
                    "carnes": 4500000,
                    "lacteos": 1300000
                }
            },
            {
                "febrero": {
                    "aseo": 134000,
                    "frutas": 600000,
                    "carnes": 1000000,
                    "lacteos": 900000
                }
            },
            {
                "marzo": {
                    "aseo": 1000000,
                    "frutas": 1400000,
                    "carnes": 1600000,
                    "lacteos": 2000000
                }
            },
            {
                "abril": {
                    "aseo": 1900000,
                    "frutas": 2450000,
                    "carnes": 1400000,
                    "lacteos": 300000
                }
            },
            {
                "mayo": {
                    "aseo": 1800000,
                    "frutas": 2750000,
                    "carnes": 1200000,
                    "lacteos": 200000
                }
            },
            {
                "junio": {
                    "aseo": 1700000,
                    "frutas": 2000000,
                    "carnes": 1900000,
                    "lacteos": 500000
                }
            },
            {
                "julio": {
                    "aseo": 1600000,
                    "frutas": 2780000,
                    "carnes": 1500000,
                    "lacteos": 700000
                }
            },
            {
                "agosto": {
                    "aseo": 1500000,
                    "frutas": 2250000,
                    "carnes": 1100000,
                    "lacteos": 200000
                }
            },
            {
                "septiembre": {
                    "aseo": 1100000,
                    "frutas": 2540000,
                    "carnes": 1200000,
                    "lacteos": 400000
                }
            },
            {
                "octubre": {
                    "aseo": 1400000,
                    "frutas": 2120000,
                    "carnes": 1400000,
                    "lacteos": 500000
                }
            },
            {
                "noviembre": {
                    "aseo": 1300000,
                    "frutas": 2230000,
                    "carnes": 1700000,
                    "lacteos": 200000
                }
            },
            {
                "diciembre": {
                    "aseo": 1000000,
                    "frutas": 2480000,
                    "carnes": 12500000,
                    "lacteos": 100000
                }
            }
        ]
    },
    "Pocll1": {
        "nombre_sede": 'Sindical',
        "direccion": 'cll22 #50-14',
        "ventas": [
            {
                "enero": {
                    "aseo": 980000,
                    "frutas": 4200000,
                    "carnes": 840000,
                    "lacteos": 500000
                }
            },
            {
                "febrero": {
                    "aseo": 910000,
                    "frutas": 6400000,
                    "carnes": 140000,
                    "lacteos": 480000
                }
            },
            {
                "marzo": {
                    "aseo": 920000,
                    "frutas": 4300000,
                    "carnes": 240000,
                    "lacteos": 410000
                }
            },
            {
                "abril": {
                    "aseo": 980000,
                    "frutas": 4200000,
                    "carnes": 540000,
                    "lacteos": 402000
                }
            },
            {
                "mayo": {
                    "aseo": 920000,
                    "frutas": 6700000,
                    "carnes": 540000,
                    "lacteos": 980000
                }
            },
            {
                "junio": {
                    "aseo": 900000,
                    "frutas": 4600000,
                    "carnes": 650000,
                    "lacteos": 290000
                }
            },
            {
                "julio": {
                    "aseo": 890000,
                    "frutas": 4200000,
                    "carnes": 190000,
                    "lacteos": 720000
                }
            },
            {
                "agosto": {
                    "aseo": 130000,
                    "frutas": 9200000,
                    "carnes": 960000,
                    "lacteos": 870000
                }
            },
            {
                "septiembre": {
                    "aseo": 210000,
                    "frutas": 5400000,
                    "carnes": 180000,
                    "lacteos": 980000
                }
            },
            {
                "octubre": {
                    "aseo": 250000,
                    "frutas": 3400000,
                    "carnes": 140000,
                    "lacteos": 450000
                }
            },
            {
                "noviembre": {
                    "aseo": 430000,
                    "frutas": 3500000,
                    "carnes": 2500000,
                    "lacteos": 420000
                }
            },
            {
                "diciembre": {
                    "aseo": 560000,
                    "frutas": 8900000,
                    "carnes": 720000,
                    "lacteos": 400000
                }
            }
        ]
    }
}

print(mejor_promedio_anual(datos))


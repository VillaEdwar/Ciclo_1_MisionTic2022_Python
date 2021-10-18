def imc(info: dict) -> tuple:
    # Se accede la información de las cedulas por medio del metodo keys()
    cedulas = info.keys()
    resultado = {}

    # Se crea el for inicial que tome todas las cedulas
    for i in cedulas:
        pesosTotal = list(info[i]['infoSalud']['peso'])
        alturasTotal = list(info[i]['infoSalud']['altura'])
        IMC = []

        # Se crea el for interno con el objetivo de almacenar el IMC
        for j in range(len(pesosTotal)):
            IMC.append(pesosTotal[j] / alturasTotal[j] ** 2)
        resultado[i] = round(sum(IMC) / len(IMC), 1)
        IMC = []

    pesoEntre18y25 = dict(filter(lambda peso: (peso[1] < 18.5) or (peso[1] > 25.0), resultado.items()))

    return (resultado, pesoEntre18y25)
"""
print("---- CASOS PUBLICOS ----")
info1 = {
    1144154: {
        "nombreCompleto": "Lina Maria Valencia",
        "infoSalud":
            {
                "peso": [60, 55, 45, 43, 55],
                "altura": [1.8, 1.8, 1.8, 1.8, 1.8]
            }
    },
    1088852: {
        "nombreCompleto": "Mariana Sandoval",
        "infoSalud":
            {
                "peso": [80, 88, 65, 62, 70],
                "altura": [1.7, 1.7, 1.7, 1.7, 1.7]
            }
    },
    1664558: {
        "nombreCompleto": "Sara Torres",
        "infoSalud":
            {
                "peso": [45, 40, 44, 40, 50],
                "altura": [1.50, 1.51, 1.52, 1.55, 1.6]
            }
    }
}
print(imc(info1))
info2 = {
    6668145: {
        "nombreCompleto": "Pablo Perez",
        "infoSalud":
            {
                "peso": [60, 61, 62, 63, 64],
                "altura": [1.6, 1.6, 1.6, 1.6, 1.6]
            }
    },
    7412589: {
        "nombreCompleto": "Juan Esteban Sanchez",
        "infoSalud":
            {
                "peso": [40, 50, 41, 42, 43],
                "altura": [1.45, 1.46, 1.47, 1.48, 1.5]
            }
    },
    9632145: {
        "nombreCompleto": "Daniel Molano",
        "infoSalud":
            {
                "peso": [56, 57, 62, 63, 60],
                "altura": [1.55, 1.55, 1.55, 1.55, 1.55]
            }
    }
}
print(imc(info2))
print("---- CASOS PRIVADOS ----")
info3 = {
    6547896: {
        "nombreCompleto": "Juan Pablo Huertas",
        "infoSalud":
            {
                "peso": [79, 75, 80, 85, 86],
                "altura": [1.8, 1.8, 1.8, 1.8, 1.8]
            }
    },
    1088852: {
        "nombreCompleto": "Ana Sanchez",
        "infoSalud":
            {
                "peso": [60, 58, 50, 50, 52],
                "altura": [1.7, 1.7, 1.7, 1.7, 1.7]
            }
    },
    1664558: {
        "nombreCompleto": "Cristian Martinez",
        "infoSalud":
            {
                "peso": [60, 50, 58, 62, 65],
                "altura": [1.8, 1.81, 1.82, 1.82, 1.84]
            }
    }
}
print(imc(info3))
info4 = {
    1258478: {
        "nombreCompleto": "Pablo Perez",
        "infoSalud":
            {
                "peso": [75, 75, 70, 75, 70],
                "altura": [1.5, 1.58, 1.6, 1.6, 1.6]
            }
    },
    8521547: {
        "nombreCompleto": "Juan Esteban Sanchez",
        "infoSalud":
            {
                "peso": [55, 60, 58, 54, 53],
                "altura": [1.45, 1.46, 1.47, 1.48, 1.5]
            }
    },
    8963214: {
        "nombreCompleto": "Daniel Molano",
        "infoSalud":
            {
                "peso": [45, 43, 42, 41, 40],
                "altura": [1.55, 1.55, 1.55, 1.55, 1.55]
            }
    }
}
print(imc(info4))
"""
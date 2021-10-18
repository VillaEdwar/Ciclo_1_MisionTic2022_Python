##################
#Ciclo 1         #
#Reto 4          #
#Grupo P47       #
##################
#Formador de Programacion: Jhonatan Stivens Barrera Ordoñez

from functools import reduce

edadAnimales = {
    'Vertebrados': {
        'Reptiles': [('Cocodrilo', 70), ('Tortuga', 150), ('Tuatara', 117), ('Yacare', 80)],
        'Anfibios': [('Triton', 8), ('Tapalcua', 12), ('Rana', 10)]
    },
    'Invertebrados': {
        'Anelidos': [('Errantes', 50), ('Lombriz', 4), ('Sanguijuela', 26)],
        'Artropodos': [('Escorpion', 6), ('Libelula', .5), ('Cigarra', 10), ('Mariposa', 1)]
    },
    'Other Structure': {
        'TypeAnimal_1': [('Animal1_SG1', 4585), ('Animal2_SG1', 5824), ('Animal3_SG1', 4875)],
        'TypeAnimal_2': [('Animal1_SG2', 254851), ('Animal2_SG2', 3458)]
    }
}


def calculaPromedio(datos:list)->int:
    promedio = round(reduce(lambda x, y: x + y, datos) / (len(datos)),2)
    return promedio


def consultaAnimales(opt:int, db:dict, estructura:str=''):
    
    promedios = {}

    try:
        if opt == 2 and estructura != '':
            return 'La opción no recibe estructura'
    
        if opt == 2:
            for estructura in db:
                animales =  []
                tipoAnimales = db[estructura]
                for animal in tipoAnimales:
                    for i in range(len(tipoAnimales[animal])):
                        animales.append(tipoAnimales[animal][i][1])
                promedios[estructura] = calculaPromedio(animales)
            solucion = promedios

        elif opt == 3:
            tipoAnimales = db[estructura]
            for animal in tipoAnimales:
                animales = []
                for i in range(len(tipoAnimales[animal])):
                    animales.append(tipoAnimales[animal][i][1])
                promedios[animal] = calculaPromedio(animales)
            solucion = promedios

        elif opt == 1:
            localidadMax = ('',0)
            estados = db[estructura]
            for estado in estados:
                localidades = estados[estado]
                for localidad in localidades:
                    if localidad[1]>localidadMax[1]:
                        localidadMax=localidad
            solucion = localidadMax

        else:
            solucion = 'La opción no es valida'

    except:
        return 'La opción ingresada requiere de una estructura animal valida'

    return solucion

# Pruebas Publicas
print(consultaAnimales(2, edadAnimales, 'Vertebrados'))
print(consultaAnimales(1, edadAnimales))
print(consultaAnimales(2, edadAnimales))
print(consultaAnimales(1, edadAnimales, 'Vertebrados'))
print(consultaAnimales(3, edadAnimales, 'Invertebrados'))

# Pruebas Privadas
print(consultaAnimales(0, edadAnimales))
print(consultaAnimales(1, edadAnimales, 'Other Structure'))
print(consultaAnimales(3, edadAnimales, 'Vertebrados'))
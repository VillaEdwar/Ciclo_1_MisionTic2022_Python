##################
#Ciclo 1         #
#Reto 4          #
#Grupo P17       #
##################
#Formador de Programacion: Jhonatan Stivens Barrera Ordoñez

from functools import reduce

positivos_C19 = {
    'Colombia': {
        'Risaralda': [('Pereira', 45), ('Dosquebradas', 15), ('La Virginia', 30)],
        'Quindio': [('Armenia', 75), ('Montenegro', 86)]
    },
    'Mexico': {
        'Quintana Roo': [('Benito Juarez', 101), ('Solidaridad', 56)],
        'Nayarit': [('Compostela', 23), ('San Blas', 35), ('Xalisco', 74), ('Del Nayar', 46)]
    },
    'Other Country': {
        'State_1': [('City1_SG1', 4585), ('City2_SG1', 5824), ('City3_SG1', 4875)],
        'State_2': [('City1_SG2', 254851), ('City2_SG2', 3458)]
    }
}

def calculaPromedio(datos:list)->int:
    promedio = round(reduce(lambda x, y: x + y, datos) / (len(datos)),2)
    return promedio


def analizaPacientes(opt:int, db:dict, pais:str=''):
    
    promedios = {}

    try:
        if opt == 0 and pais != '':
            return 'La opción no recibe pais'
    
        if opt == 0:
            for pais in db:
                pacientes =  []
                ciudades = db[pais]
                for ciudad in ciudades:
                    for i in range(len(ciudades[ciudad])):
                        pacientes.append(ciudades[ciudad][i][1])
                promedios[pais] = calculaPromedio(pacientes)
            solucion = promedios

        elif opt == 1:
            ciudades = db[pais]
            for ciudad in ciudades:
                pacientes = []
                for i in range(len(ciudades[ciudad])):
                    pacientes.append(ciudades[ciudad][i][1])
                promedios[ciudad] = calculaPromedio(pacientes)
            solucion = promedios

        elif opt == 2:
            localidadMax = ('',0)
            estados = db[pais]
            for estado in estados:
                localidades = estados[estado]
                for localidad in localidades:
                    if localidad[1]>localidadMax[1]:
                        localidadMax=localidad
            solucion = localidadMax

        else:
            solucion = 'La opción no es valida'

    except:
        return 'La opción ingresada requiere de un país valido'

    return solucion

# Pruebas Publicas
print(analizaPacientes(0, positivos_C19))
print(analizaPacientes(2, positivos_C19, 'Colombia'))
print(analizaPacientes(1, positivos_C19, 'Mexico'))
print(analizaPacientes(2, positivos_C19, 'Mexico'))
print(analizaPacientes(5, positivos_C19))

# Pruebas Privadas
print(analizaPacientes(1, positivos_C19))
print(analizaPacientes(0, positivos_C19, 'Colombia'))
print(analizaPacientes(1, positivos_C19, 'Other Country'))
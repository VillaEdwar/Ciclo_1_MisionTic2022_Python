##################
#Ciclo 1         #
#Reto 4          #
#Grupo P77       #
##################
#Formador de Programacion: Jhonatan Stivens Barrera Ordoñez

from functools import reduce

dinos = {
    'Ornithischia': {
        'Tireoforos': [('Chialingosaurus', 150), ('Ankylosaurus', 6800), ('Scelidosaurus', 270)],
        'Neornitisquios': [('Iguanodon', 4200), ('Pachycephalosaurus', 820), ('Triceratops', 7800)]
    },
    'Saurischia': {
        'Teropodos': [('Tyrannosaurus', 6700), ('Velociraptor', 15), ('Gigantoraptor', 1900), ('Archaeopterix', 1)],
        'Sauropodomorfos': [('Saturnalia', 10), ('Apatosaurus', 20200), ('Diplodocus', 113000)]
    },
    'Another Principal Group': {
        'SubGroup_1': [('Dino1_SG1', 4585), ('Dino2_SG1', 5824), ('Dino3_SG1', 4875)],
        'SubGroup_2': [('Dino1_SG2', 254851), ('Dino2_SG2', 3458)]
    }
}


def calculaPromedio(datos:list)->int:
    promedio = round(reduce(lambda x, y: x + y, datos) / (len(datos)),2)
    return promedio


def busquedaDinos(opt:int, db:dict, grupo_principal:str=''):
    
    promedios = {}

    try:
        if opt == 2 and grupo_principal != '':
            return 'La opción no recibe grupo principal'

        if opt == 2:
            for grupo_principal in db:
                dinosaurios =  []
                tipodinosaurios = db[grupo_principal]
                for dinosaurio in tipodinosaurios:
                    for i in range(len(tipodinosaurios[dinosaurio])):
                        dinosaurios.append(tipodinosaurios[dinosaurio][i][1])
                promedios[grupo_principal] = calculaPromedio(dinosaurios)
            solucion = promedios

        elif opt == 3:
            tipodinosaurios = db[grupo_principal]
            for dinosaurio in tipodinosaurios:
                dinosaurios =  []
                for i in range(len(tipodinosaurios[dinosaurio])):
                    dinosaurios.append(tipodinosaurios[dinosaurio][i][1])
                promedios[dinosaurio] = calculaPromedio(dinosaurios)
            solucion = promedios

        elif opt == 1:
            dinoMax = ('',0)
            subtipos = db[grupo_principal]
            for subtipo in subtipos:
                dinosaurios = subtipos[subtipo]
                for dinosaurio in dinosaurios:
                    if dinosaurio[1]>dinoMax[1]:
                        dinoMax=dinosaurio
            solucion = dinoMax

        else:
            solucion = 'La opción no es valida'

    except:
        return 'La opción ingresada requiere el nombre de un grupo principal valido'

    return solucion


# Pruebas publicas

print(busquedaDinos(1, dinos))
print(busquedaDinos(3, dinos, 'Saurischia'))
print(busquedaDinos(2, dinos))
print(busquedaDinos(1, dinos, 'Ornithischia'))
print(busquedaDinos(7, dinos))

# Pruebas privadas
print(busquedaDinos(3, dinos, 'Ornithischia'))
print(busquedaDinos(1, dinos, 'Saurischia'))
print(busquedaDinos(2, dinos, 'No Se Envia'))
#Estructura para los diccionarios

cursos = {
    "plan":4,
    "nombre":{
        "asignatura1":"Matemáticas",
        "asignatura2":"Sociales",
        "asignatura3":"Ciencias"
    },
    "codigo_curso":430567
}

#print(type(cursos))
print(cursos["nombre"]["asignatura3"])
print(cursos["codigo_curso"])
print(cursos)

# Estructura para los diccionarios

cursos = {
    "plan": 4,
    "nombre": {
        "asignatura1": "Matemáticas",
        "asignatura2": "Sociales",
        "asignatura3": "Ciencias"
    },
    "codigo_curso": 430567
}

# print(type(cursos))
#print(cursos["nombre"]["asignatura3"])
#print(cursos["codigo_curso"])
#print(cursos)

if cursos["plan"] == 5:
    matricula = {"id":cursos["codigo_curso"],"materia":cursos["nombre"]["asignatura1"]}
else:
    matricula = {"id":cursos["codigo_curso"],"materia":cursos["nombre"]["asignatura3"]}

print(matricula)
#CREACION DE UNA FUNCION
#Requerimiento -> Determinar si un correo tiene le número de arrobas adecuado (1)
#Obtener el usuario y el dominio si es válido (2)
#(3) Solicitar varios correos y almacenar en una lista de diccionarios aquellos que son válidos

def correoValido(correo):
    numArrobas = 0
    for i in range(len(correo)):
        if correo[i] == "@":
            numArrobas += 1
    if numArrobas == 1:
        return True
    else:
        return False
            
#ESTE ES MI APRENJIZAJE PARA COLECCIONAR EN LISTAS UNA CADENA
#una de las formas
#Solicitar 3 correos y clasificarlos -> guardarlos en una lista de diccionarios
listaCorreoValido = list()
for _ in range(3):
    #soliciar correo
    correo = input("ingresar correo: ")
    elementosCorreo = list()
    diccionarioCorreo = dict()
    if correoValido(correo):
        elementosCorreo = correo.split("@")
        diccionarioCorreo = {"nombre de usuario":elementosCorreo[0],"dominio":elementosCorreo[1]}
        listaCorreoValido.append(diccionarioCorreo)
    else:
        print("correo invalido")

#Mostrar contenedor final (coleccion correso validos)
listaCorreoValido = tuple(listaCorreoValido)
print(listaCorreoValido)

'''
#RECORRIDO CONTENEDOR DE CONTENEDORES
for correo in listaCorreoValido:
    #SUPONGAMOS QUE NO SEPAMOS LA UBICACION DE CADA CORREO
    #SABEMOS QUE ES UN DICCIONARIO
    #PUEDO RECORRER TODAS LAS LALVES, PUEDO RECORRER TODOS LOS VALORES O PUEDO CRECORRER TODAS LAS PAREJAS
    for llave, valor in correo.item()
    print()
'''
#RECORRIDO CONTENEDOR DE CONTENEDORES(otra forma) como yo se que correo es una lista o tupla puedo obtener una
#enumeracion
for i,correo in enumerate(listaCorreoValido):
    print("----")
    print(f"correo valido No. {i+1}")
    for llave, valor in correo.items():
        print(f"{llave}: {valor}")
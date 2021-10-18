#ESTE ES MI APRENJIZAJE PARA COLECCIONAR EN LISTAS UNA CADENA
#una de las formas
#Solicitar correo al ussuario
correo = input("ingrese correo: ")
numArrobas = 0
#for caracter in correo:
 #   if caracter  == "@":
  #      numArrobas +=1

#Otra forma de hacerlo
for i in range(len(correo)):
    if i  == "@":
        numArrobas +=1

elementosCorreo = list()
if numArrobas == 1:
    print("correo valido")
    #Split es una propiedad de las cadenas y lo que me hace es coleccionar en una lista, separandolos
    elementosCorreo = correo.split("@")
    print("nombre de usuario",elementosCorreo[0])
    print("dominio del correo",elementosCorreo[1])
else:
    print("correo invalido")


#ESTE ES MI APRENJIZAJE PARA COLECCIONAR EN DICCIONARIOS UNA CADENA (MANERA 1)
#una de las formas
#Solicitar correo al ussuario
correo = input("ingrese correo: ")
numArrobas = 0
#for caracter in correo:
 #   if caracter  == "@":
  #      numArrobas +=1

#Otra forma de hacerlo
for i in range(len(correo)):
    if i  == "@":
        numArrobas +=1

elementosCorreo = list()
diccionarioCorreo = dict()
if numArrobas == 1:
    print("correo valido")
    #Split es una propiedad de las cadenas y lo que me hace es coleccionar en una lista, separandolos
    elementosCorreo = correo.split("@")
    #YA DEFINI UN DICCIONARIO VACIO, SI EXISTE EL ELMENTO SE ACTUALIZA Y SI NO, SE AGREGA
    #diccionarioCorreo["llave"]
    diccionarioCorreo["nombre de usuario"]=elementosCorreo[0]
    diccionarioCorreo["dominio"]=elementosCorreo[1]
    
else:
    print("correo invalido")

#GUARDAR LA INFORMACION EN UN DICCIONARIO
print("accediendo a cada posicion")
print("nombre de usuario",diccionarioCorreo["nombre de usuario"])
print("dominio",diccionarioCorreo["dominio"])

#ESTE ES MI APRENJIZAJE PARA COLECCIONAR EN DICCIONARIOS UNA CADENA (MANERA 2)
#una de las formas
#Solicitar correo al ussuario
correo = input("ingrese correo: ")
numArrobas = 0
#for caracter in correo:
 #   if caracter  == "@":
  #      numArrobas +=1

#Otra forma de hacerlo
for i in range(len(correo)):
    if i  == "@":
        numArrobas +=1

elementosCorreo = list()
diccionarioCorreo = dict()
if numArrobas == 1:
    print("correo valido")
    #Split es una propiedad de las cadenas y lo que me hace es coleccionar en una lista, separandolos
    elementosCorreo = correo.split("@")
    #YA DEFINI UN DICCIONARIO VACIO, SI EXISTE EL ELMENTO SE ACTUALIZA Y SI NO, SE AGREGA
    #diccionarioCorreo["llave"]
    diccionarioCorreo = {
        "nombre de usuario":elementosCorreo[0],
        "dominio":elementosCorreo[1]
    }
    
else:
    print("correo invalido")

#GUARDAR LA INFORMACION EN UN DICCIONARIO
print("accediendo a cada posicion")
print("nombre de usuario",diccionarioCorreo["nombre de usuario"])
print("dominio",diccionarioCorreo["dominio"])


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
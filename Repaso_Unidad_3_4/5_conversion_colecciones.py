'''
#Principales

#Cadena a lista: aprovechando la mutabilidad de la lista para actualizar la cadena
cadena = 'misionTIC'
lista = list(cadena)
#actualizar cadena
lista[0] = lista[0].upper() #mayuscula primera posicion
lista[-1] = lista[-1].lower() #minuscula ultima posicion
cadena = ''.join(lista)
print(cadena)

#Eliminar repeticiones convirtiendo cadena a conjunto (perdemos el orden)
cadena = 'hhoolaaa'
conjunto = set(cadena)
print("Versión conjunto de la cadena: ",conjunto)
cadena = ''.join(conjunto)
print("Versión de la cadena sin repeticiones: ",cadena)

#Convertir cadena a diccionario -> satisfacer la llave
cadena = 'prueba' # podemos usarlos como llaves o como valores
diccionario = dict()
for i,caracter in enumerate(cadena):
    diccionario[i] = caracter #sacamnos caracter por caracter
print('Diccionario resultante: ',diccionario)
'''

#podemos usar la funcion zip pero necesitamos parejitas(otra forma)
cadena = 'misionTIC'
diccionario = dict( zip( range(len(cadena)) , cadena )  )
print('Conversión a Diccionario en una sola línea',diccionario)

#Convertir diccionario a cadena
print("Llaves: ",list( diccionario.keys() ))
print("Valores: ",list( diccionario.values() ))
print("Items: ",list( diccionario.items() ))
cadenaValoresDiccionario = ''.join(list(diccionario.values()))
print("Cadena Valores Diccionario: ",cadenaValoresDiccionario)
'''
cadena = "Programando"

lista = list(cadena)

#print(cadena)

#print(lista)

#print(''.join(lista))

# cadenas a tuplas

tupla = tuple(cadena)

#print(tupla)
'''

diccionario = {"01": "Tarea1", "02": "Tarea2"}
print(diccionario)
print(list(diccionario))
print(list(diccionario.keys()))
print(list(diccionario.values()))

print(diccionario.items())
print(list(diccionario.items()))
print(list(diccionario.items())[0])
print(list(diccionario.items())[1])

c = list(diccionario.items())[1]
print(''.join(list(c)))
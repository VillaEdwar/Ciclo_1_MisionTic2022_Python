#Cadenas -> Flujos de caracteres o palabras (orden inmutables) 
cadena = "hola Mundo"
print(cadena[0])
print(cadena[-1])
print(cadena[2])
print(cadena[0:4])
# Para yo cambiar la prmera mayuscula debo construir toda la cadena desde cero(reconstruir)
cadena = cadena[0].upper() + cadena[1:]
print(cadena)

#Listas -> obedecen a un orden también se pueden modificar (mutables)
lista = [12,'hola','casa',45]
print(lista[0]) 
print(lista[-1])
print(lista[0:2])
lista[0] = 24
print(lista)
#agrega nuevo eleemtno
lista.append('nuevo elemento')
print(lista)
#puedo agregar en cuaqluier possicion
lista.insert(0,[6,7,8])
print(lista)
# POdemos eliminar elemnetos de la lista
lista.pop(0)
print(lista)

#Tuplas -> equivalentes a listas que no se pueden modificar
a = 12
b = 12
tupla = (a,b,lista)
print(tupla)

#No siguen un orden -> conjutnos, diccionarios

#Conjuntos puedo revisar si esta o no esta un elemento
conjunto = {'Armenia','Bogotá','Cali'}
for elemento in conjunto:
    print(elemento)
print('--------------')
conjunto.add('Ibagué')
conjunto.remove('Armenia')
for elemento in conjunto:
    print(elemento)
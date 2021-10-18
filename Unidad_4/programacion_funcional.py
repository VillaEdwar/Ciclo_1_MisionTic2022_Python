'''****************** Programación Funcional *****************'''

#def suma(val1=0,val2=0):
#    return val1 + val2
#print(suma(10,20))

# función suma
def suma(val1 = 0, val2 = 0):
    return val1 + val2
# función resta
def resta(val1 = 0, val2 = 0):
    return val1 - val2
# fución operación
def operacion(funcion, val1=0, val2=0):
    return funcion(val1,val2)
funcion_suma = suma
funcion_resta = resta

num1 = int(input("num1.."))
num2 = int(input("num2.."))
resultado = operacion(funcion_suma, num1, num2)
print(resultado)
resultado = operacion(funcion_resta, num1, num2)
print(resultado)


#Funciones de orden superior, pasando como parámetros funciones hijas

def mejor_promedio():
    #función hija
    def promedio(val1,val2):
        return (val1+val2)/2

    return ventas(promedio)

def ventas(funcion):
    return funcion(5,2)

print(mejor_promedio())

#Funciones lambda
convertir = lambda valor: f"${valor}"
print(convertir(5000))

suma_numeros = lambda n1,n2: n1 + n2
print(suma_numeros(2,3))

promedio = lambda v1,v2,v3: (v1+v2+v3)/3
print( promedio(5,10,15) )

#Retorne una lista de Ni hasta Nf
nueva_lista = lambda i,f: [x for x in range(i,f) if x%3 == 0]
print( nueva_lista(1,201) )

elevar_al_cubo = lambda n: n**3
#print(elevar_al_cubo(3))

# map
# Creamos la lista
lista_numeros: list = [2, 3, 4, 5, 6, 7, 8, 9]
#map(funcion_a_aplicar, un_iterable)
print(list(map(elevar_al_cubo, lista_numeros)))

def filtrar(dato):
    if dato=="á":
        return "a"
    elif dato=="é":
        return "e"
    elif dato=="í":
        return 'i'
    elif dato=='ó':
        return 'o'
    elif dato=='ú':
        return 'u'
    else: return dato
#Función anónima
caracteres = lambda letras : list( map(filtrar,letras) )
#Palabra a procesar
palabra = "olímpica"
#Llama la función lambda con la palabra casteada a lista
#Y obtiene una nueva lista con los caracteres sin tilde
result = caracteres( list(palabra) )
print( ''.join(result))

fruit = {"01":"Aola1", "02":"hola2"}
#fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_object = map(lambda s: s[0] == "A", fruit.values())
print(list(map_object))


numeros = [1,2,3,4,5,6,7,8,9,10]
resultado = filter(lambda x: x%2 == 0, numeros)
print(list(resultado))

resultado = [x for x in numeros if x%2 == 0]
print(resultado)

from functools import reduce

lista = [1,2,3,4]
def acumulador(acumulador = 0,elemento = 0):
    return acumulador + elemento

resultado = reduce(acumulador, lista)
print(resultado)

resultado = reduce(lambda acumulador = 0, elemento = 0: acumulador + elemento, lista)
print(resultado)


nombres = ["Raul", "Pedro", "Sofia"]
apellidos = ["López Briega", "Perez", "Gonzalez"]

nombreApellido = zip(nombres, apellidos)
print(list(nombreApellido))

#Operador Ternario
resultado = "True" if 1==2 else "False"
print(resultado)

lista = [1==1, 2==2, True, True, True]
if all(lista):
    print("Todos son True")
else:
    print("Al menos uno no es True")

#Cantidad indefinida de argumentos-> *args
"""
De forma análoga funcionan los keyword arguments, 
que son representados con dos asteriscos (**) y el nombre kwargs. 
Cabe destacar que los nombres de estos parámetros son indiferentes; 
args y kwargs son utilizados simplemente por convención.
"""
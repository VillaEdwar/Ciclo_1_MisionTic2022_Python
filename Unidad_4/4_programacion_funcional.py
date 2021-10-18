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

resultado = operacion(funcion_suma, 10,20)
print(resultado)
resultado = operacion(funcion_resta, 10,20)
print(resultado)

'''
num1 = int(input("num1.."))
num2 = int(input("num2.."))
resultado = operacion(funcion_suma, num1, num2)
print(resultado)
resultado = operacion(funcion_resta, num1, num2)
print(resultado)
'''

'''
def mejor_promedio():
    #función hija
    def promedio(val1,val2):
        return (val1+val2)/2

    ventas(promedio)

def ventas(funcion):
    return funcion(5,2)

print(mejor_promedio())
def mejor_promedio():
    #función hija
    def promedio(val1,val2):
        return (val1+val2)/2

    return ventas(promedio)

def ventas(funcion):
    return funcion(5,2)

print(mejor_promedio())
'''

# Solucion punto 1
x = 43
x = x + 1
print(x)
#---------------------------------------------------

# Solucion punto 2

var1 = 10
var2 = 4
var3 = 5.5
var4 = 67

promedio = (var1 + var2 + var3 + var4)/4

print("el promedio es: " + str(promedio))
#---------------------------------------------------

# Solucion punto 3
# Calcular el area y el perimetro de un cuadrado
# entrada
L = 38
# procesp
A = L * L
P = 4 * L
# salida
print(A)
print(P)
print(A, P)
print("El perimetro del cuadrado con lado {} es {} ".format(L,P))
print("El perimetro del cuadrado con lado {} es {} ".format(L,A))
#---------------------------------------------------

# Solucion punto 4

var1 = 10
var2 = 30
var3 = 120
var4 = 500

maximo = max(var1, var2, var3, var4)
minimo = min(var1, var2, var3, var4)
print(maximo)
print(minimo)
#---------------------------------------------------

# Solucion punto 5

def areacuadrado(lado):
    a = lado * lado
    return a

print(areacuadrado(38))

def perimetrocuadrado(lado):
    p = 4 * lado
    return p

print(perimetrocuadrado(38))

#---------------------------------------------------

# Solucion punto 5 (ahorrando declarar variables)
def areacuadrado(lado):
    return lado * lado

print(areacuadrado(38))

def perimetrocuadrado(lado):
    return 4 * lado

print("el perimetro es: " + str(perimetrocuadrado(38)))
print("el area es {}".format(areacuadrado(38)))
A = areacuadrado(38)
print("el area es {}".format(A))
#---------------------------------------------------

# Solucion punto 7

def imprime_Cosas():
    print("La clase está genial")   #Se debe explicar de la indentacion de python y de como se ejecutan las instrucciones
    print('Python es lo máximo')

imprime_Cosas()

def repetir_funciones():
    imprime_Cosas()
    imprime_Cosas()

repetir_funciones()
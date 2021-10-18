'''
n = 5
while n > 0:
    print(n)
    n = n - 1
print("Despegue")

n = 1
while n <= 10:
    print(n)
    n = n + 1

# 5 X 1 = 5
# 5 X 2 = 10
# 5 X 3 = 15

n = 1
while n <= 10:
    r = 5 * n
    print("5 X {} = {}".format(n,r))
    n = n + 1
'''
#si solo necesito mostrar un print no es necesario -> ni el return 
# pero si es un str o int entocnes s para que el return

def tabla_multiplicar(numero:int, limite_inf:int, limite_sup:int):
    n = limite_inf
    while n <= limite_sup:
        r = numero * n
        print("{} X {} = {}".format(numero,n,r))
        n = n + 1

tabla_multiplicar(5, 1, 10)
'''
def suma_numeros(a:int, b:int, c:int) -> int:
    return a + b + c

print(suma_numeros(3,5,6))
def tabla(numero:int,n:int,hasta:int):
    inicio=n
    while n<=hasta:
        resultado=numero*n
        print("{}x{} = {}".format(numero,n,resultado))
        n+=1
    return print("Terminó tabla del {} desde el {} hasta el {}".format(numero,inicio,hasta))

tabla(int(input("Ingrese numero de la tabla de multiplicar deseada: ")),int(input("indique inicio: ")),int(input("indique el limite: ")))
para  ingresar valores desde consola 
'''
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
'''
# 5 X 1 = 5
# 5 X 2 = 10
# 5 X 3 = 15
'''
numero = int(input("Tabla de multiplicar? "))
n = 1
while n <= 10:
    r = numero * n
    print("{} X {} = {}".format(numero,n,r))
    n = n + 1
'''
def tabla_multiplicar(numero:int, limite_inf:int, limite_sup:int):
    if limite_inf > limite_sup:
        print("La tabla de multiplicar no se generó!!")
    else:
        n = limite_inf
        while n <= limite_sup:
            r = numero * n
            print("{} X {} = {}".format(numero,n,r))
            n = n + 1

a = int(input("numero "))
b = int(input("limite inferior "))
c = int(input("limite superior "))

tabla_multiplicar(a, b, c)
'''
def suma_numeros(a:int, b:int, c:int) -> int:
    return a + b + c

print(suma_numeros(3,5,6))
'''
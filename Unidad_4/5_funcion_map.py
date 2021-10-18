elevar_al_cubo = lambda n: n**3
print(elevar_al_cubo(3))
#map
# Creamos la lista
lista_numeros: list = [2, 3, 4, 5, 6, 7, 8, 9]
#map(funcion_a_aplicar, un_iterable)
print(list(map(elevar_al_cubo, lista_numeros)))
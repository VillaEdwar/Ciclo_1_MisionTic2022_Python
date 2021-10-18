'''Una compañía internacional requiere una aplicación para
obtener el factor de recolección que es el 10% del total de semillas recolectadas en la semana
y calcular el promedio de las semillas que recolectan de lunes a viernes.
Escriba una función qué reciba cómo parámetros: una cadena con el nombre de la semilla y
la cantidad de semillas recolectadas por cada día (a, b, c, d, e) que representan evidentemente
los cinco dias de la semana y retorne una cadena de caracteres que le proporciona la compañia
para la información que se desea obtener. La cadena debe tener la siguiente estructura: "El
factor de recolección es {factor} y el promedio de las recolecciones para la semilla de
{semilla} es de: {promedio}" dónde, el promedio reportado debe estar redondeado a un
decimal.........
print("El factor de recolección es {} y el promedio de las recolecciones para la semilla de {} es de: {}".format(factor,total,promedio))
'''
'''
def promedioRecoleccion(semilla,a,b,c,d,e):
'''
def promedioRecoleccion(semilla: str, a: int, b: int, c: int, d: int, e: int)->str():
    # A continuacion vamos a calcular el factor de recoleccion
    factor_recoleccion = str((a + b + c + d + e) * 0.10)
    # A continuacion calculamos el promedio de recoleccion  
    promedio_recoleccion = ((a + b + c + d + e)/5)
    # Calculo del promedio de las recolecciones redondeado a un decimal
    promedio_dias_redondeado = round(promedio_recoleccion,1)
    # A continuacion convertimos el resultado a cadena
    promedio = str(promedio_dias_redondeado)
    return "El factor de recolección es {} y el promedio de las recolecciones para la semilla de {} es de: {}".format(factor_recoleccion,semilla,promedio)
print(promedioRecoleccion("frijol", 1250, 1010, 800, 220, 530))
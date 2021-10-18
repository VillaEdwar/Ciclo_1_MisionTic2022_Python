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
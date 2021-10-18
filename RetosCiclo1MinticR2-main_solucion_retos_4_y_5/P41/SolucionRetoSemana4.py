# Solución del reto en la plataforma
import numpy as np

def generarResultados(datos):
    datos_ajustados = []

    for participante in datos:
        participante = list(map(lambda puntaje: 4 if puntaje < 5 else puntaje, participante))
        datos_ajustados.append(participante)

    matriz = np.array(datos_ajustados)
    promedio = round(matriz.mean(), 2)
    calificacion = np.sum(matriz, axis = 1)
    ganador = calificacion.argmax() + 1

    resultados = { 'puntaje promedio': promedio, 'puntaje participante 1': calificacion[0], 'puntaje participante 2': calificacion[1],'puntaje participante 3': calificacion[2], 'participante ganador': ganador}

    return resultados
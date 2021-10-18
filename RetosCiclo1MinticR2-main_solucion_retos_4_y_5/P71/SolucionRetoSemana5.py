# Solución del reto en la plataforma
import pandas as pd

def analizarDatos(archivo, porcentaje):
    df = pd.read_csv(archivo, sep=';')
    usos = df.groupby(['HORA']).size()
    hora_pico = usos.idxmax()
    valor_hora_pico = usos.max()
    proyeccion = valor_hora_pico * (1 + porcentaje)

    return { 'Hora pico': hora_pico, 'valor': valor_hora_pico, 'proyección': proyeccion }
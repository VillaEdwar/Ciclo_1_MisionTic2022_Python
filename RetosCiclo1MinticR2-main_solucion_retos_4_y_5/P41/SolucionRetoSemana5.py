# Solución del reto en la plataforma
import pandas as pd

def analizarDatos(archivo, porcentaje):
    df = pd.read_csv(archivo, sep=';')
    ventas = df.groupby(['MES']).size()
    mes_mayor = ventas.idxmax()
    valor_mes_mayor = ventas.max()
    proyeccion = valor_mes_mayor * (1 + porcentaje)

    return { 'Mes mayor venta': mes_mayor, 'Cantidad de ventas': valor_mes_mayor, 'proyección': proyeccion }
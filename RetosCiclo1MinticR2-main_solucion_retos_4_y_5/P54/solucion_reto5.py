import pandas as pd

def analisis_datos(data: pd.core.frame.DataFrame)->dict:
    lista_tipo = data.Tipo
    lista_edad = data.Edad
    tipo_edad = list(zip(lista_tipo, lista_edad))
    c_tipo1 = 0
    c_tipo2 = 0
    c_tipo3 = 0
    edades1 = 0
    edades2 = 0
    edades3 = 0
    for tipo, edad in tipo_edad:
        if tipo == 'En estudio':
            c_tipo1 += 1
            edades1 += edad
        elif tipo == 'Importado':
            c_tipo2 += 1
            edades2 += edad
        elif tipo == 'Relacionado':
            c_tipo3 += 1
            edades3 += edad
    dic = {
        'casos_en_estudio': c_tipo1,
        'prom_edades_casos_en_estudio': int(edades1/c_tipo1),
        'casos_importados': c_tipo2,
        'prom_edades_casos_importados': int(edades2/c_tipo2),
        'casos_relacionados': c_tipo3,
        'prom_edades_casos_relacionados': int(edades3/c_tipo3),
        'total_casos': c_tipo1 + c_tipo2 + c_tipo3
    }
    return dic
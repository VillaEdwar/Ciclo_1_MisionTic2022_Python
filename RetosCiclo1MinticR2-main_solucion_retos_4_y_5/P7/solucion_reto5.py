import pandas as pd

def analisis_datos(data: pd.core.frame.DataFrame)->dict:
    lista_edad = list(data.loc[:, "Edad"])
    lista_sexo = list((data.loc[:, "Sexo"]))
    edad_sexo = list(zip(lista_edad, lista_sexo))
    m = 0
    ac_edad_m = 0
    ac_edad_f = 0
    f = 0
    cantidad_datos = len(lista_edad)
    for edad, sexo in edad_sexo:
        if sexo == 'M' or sexo == 'm':
            m += 1
            ac_edad_m += edad
        if sexo == 'F' or sexo == 'f':
            f += 1
            ac_edad_f += edad
    dic = {
        'cant_hombres': m,
        'prom_edad_hombres': int(ac_edad_m / m),
        'cant_mujeres': f,
        'prom_edad_mujeres': int(ac_edad_f / f),
        'tam_muestra': cantidad_datos
    }
    return dic
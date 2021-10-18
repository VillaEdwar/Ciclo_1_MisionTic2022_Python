import pandas as pd


def informes_covid(datos: str) -> dict:
    if datos.endswith('.csv'):
        try:
            df = pd.read_csv(datos)
        except:
            return "Error al obtener los datos"
        # Obtiene el valor que más se repite
        dia_mas_contagios = df["Fecha de notificación"].mode()
        dia_mas_contagios = dia_mas_contagios[0]
        # Filtra los registros que sean de bogotá
        filtro_dia = df.loc[:,'Fecha de notificación'] == dia_mas_contagios
        dia_mayor_contagios = df[filtro_dia]
        # Cuenta los registros (numeros de contagios)
        # Número de fallecidos
        filtro_fallecidos = dia_mayor_contagios.loc[:,'atención'] == 'Fallecido'
        fallecidos = dia_mayor_contagios[filtro_fallecidos]
        #numero de recuperados
        filtro_recuperados = dia_mayor_contagios.loc[:,"atención"] == "Recuperado"
        recuperados = dia_mayor_contagios[filtro_recuperados]

        # Crea el diccionario respuesta
        respuesta: dict = {
            "mayor_contagio": dia_mas_contagios,
            "cantidad_contagios": dia_mayor_contagios['Fecha de notificación'].count(),
            "fallecidos": fallecidos['atención'].count(),
            "recuperados": recuperados['atención'].count()
        }
    else:
        return "Extensión de archivo inválida"
    
    return respuesta


print(informes_covid("https://misiontic.000webhostapp.com/casos_covid.csv"))
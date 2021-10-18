import pandas as pd

def informes_covid(datos:str) -> dict:
    if datos.endswith(".csv"):
        try:
            df = pd.read_csv(datos)
        except:
            return "Error al obtener los datos"
        #Obtiene el valor que más se repite
        mas_contagios = df["Fecha de notificación"].mode()
        mas_contagios = mas_contagios[0]
        #filtra los registros que sean de la fecha de notificacion con mas contagios
        filtro = df.loc[:,"Fecha de notificación"] == mas_contagios
        contagios = df[filtro]
        #cuenta de registros (numeros de contagios)
        # Numero de fallecidos
        filtro_fallecidos = contagios.loc[:,"atención"] == "Fallecido"
        fallecidos = contagios[filtro_fallecidos]
        #numero de recuperados
        filtro_recuperados = contagios.loc[:,"atención"] == "Recuperado"
        recuperados = contagios[filtro_recuperados]

        #Crea el diccionario respuesta
        respuesta : dict = {
            "mayor_contagio": mas_contagios,
            "cantidad_contagios": contagios["Fecha de notificación"],
            "fallecidos": fallecidos["atención"].count(),
            "recuperados": recuperados["atención"].count()
        }
    else:
        return "Extensión de archivo invalido"

    return respuesta

print(informes_covid("https://misiontic.000webhostapp.com/casos_covid.csv"))
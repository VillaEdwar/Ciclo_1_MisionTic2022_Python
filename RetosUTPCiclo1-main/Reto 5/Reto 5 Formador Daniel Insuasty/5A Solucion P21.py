def calificaciones(ruta_archivo: str)->dict:
    import pandas as pd
    df = pd.read_csv(ruta_archivo)

    promedioLecturaCritica = round(df.lecturaCritica.mean(),1)
    promedioMatematicas = round(df.matematicas.mean(),1)
    promedioSociales = round(df.sociales.mean(),1)
    promedioNaturales = round(df.naturales.mean(),1)
    promedioIngles = round(df.ingles.mean(),1)
    promedioGeneral = round(((promedioLecturaCritica+promedioMatematicas+promedioSociales+promedioNaturales+promedioIngles)/5),1)

    respuesta ={'promedioGeneral':promedioGeneral,'promedioNaturales':promedioNaturales,
                'promedioMatematicas':promedioMatematicas}

    return respuesta

print(calificaciones("https://bitbucket.org/insuasti/datosreto5mintic/raw/c7a27c4a984ee1f427eedca949f8aed22f31f244/calificaciones.csv"))

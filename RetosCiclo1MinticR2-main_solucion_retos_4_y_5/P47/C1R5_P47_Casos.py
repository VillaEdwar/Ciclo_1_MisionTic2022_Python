import json
import pandas as pd
import numpy as np

def preProcesado(DF):
    
    generosDF = DF['genres'].apply(pd.Series)
    generosDF['title'] = DF['title']
    generosDF = generosDF.drop_duplicates(['title'])
    generosDF.set_index('title', inplace=True)

    genres = [generosDF[genre].unique() for genre in generosDF.columns]
    genres = [genre for lista in genres for genre in lista if all([pd.isnull(genre) == False, genre != ' ', genre != '', len(str(genre)) > 1])]
    genres = list(set(genres))

    return generosDF, genres

def codificaMatriz(DF, genres: list, producto: list):

    mgenres = pd.DataFrame(
        np.zeros((len(genres), len(producto))),
        index=genres,
        columns=list(producto))

    for movie in DF.index:
        for index in DF:
            genre = DF[index][movie]
            if genre in genres:
                mgenres[movie][genre] = 1

    return mgenres

def recomiendaPeliculas(url_puntuacion:str, url_perfil:str, url_recomendacion:str)->json:

    dataPerfil = pd.read_json(url_perfil)
    dataPerfil, genresPuntuacion = preProcesado(dataPerfil)
    # print(dataPerfil, genresPuntuacion)
    
    peliculasPuntuacion = dataPerfil.index

    mgenres = codificaMatriz(dataPerfil, genresPuntuacion, peliculasPuntuacion)
    # print(mgenres)

    puntuacionPelicula = pd.read_csv(url_puntuacion, sep=';', names=['title', 'peso'], index_col=['title'])
    # print(puntuacionPelicula)

    for movie in mgenres.columns:
        if movie in puntuacionPelicula.index:
            mgenres[movie] = mgenres[movie].apply(lambda point: float(point * puntuacionPelicula['peso'][movie]))
    
    mgenres['ponderacionPerfilUsuario'] = [mgenres.loc[genre,:].sum() for genre in mgenres.index]
    mgenres['ponderacionPerfilUsuario'] = mgenres['ponderacionPerfilUsuario'].apply(lambda point: point / mgenres['ponderacionPerfilUsuario'].sum())
    # print(mgenres['ponderacionPerfilUsuario'])
    dataRecomendacion = pd.read_json(url_recomendacion)
    dataRecomendacion, genres = preProcesado(dataRecomendacion)
    # print(dataRecomendacion, genres)
    peliculas = dataRecomendacion.index

    mRecomentacion = codificaMatriz(dataRecomendacion, genres, peliculas)
    mRecomentacion['ponderacion'] = mgenres['ponderacionPerfilUsuario']
    mRecomentacion = mRecomentacion.transpose()

    for movie in mRecomentacion.columns:
        if movie in genresPuntuacion:
            mRecomentacion[movie] = mRecomentacion[movie].apply(lambda point: float(point * mRecomentacion[movie]['ponderacion']))
        else:
            mRecomentacion[movie] = mRecomentacion[movie].apply(lambda point: point * 0)
    
    mRecomentacion = mRecomentacion.drop(['ponderacion'])
    mRecomentacion = mRecomentacion.transpose()
    # print(mRecomentacion)
    
    recomendacionUsuario = pd.DataFrame(mRecomentacion.columns, columns=['pelicula'])
    recomendacionUsuario['peso'] = [mRecomentacion.loc[:,movie].sum() for movie in mRecomentacion.columns]
    # print(recomendacionUsuario)

    aRecomendar = recomendacionUsuario[recomendacionUsuario.peso > 0].sort_values('peso', ascending=False)
    aRecomendar['peso'] = aRecomendar['peso'].round(5)
    aRecomendar = {aRecomendar['pelicula'][i]:aRecomendar['peso'][i] for i in aRecomendar.index}
    return json.dumps(aRecomendar, indent=4)

# Publicos
# print(recomiendaPeliculas('https://git.io/JZKcF', 'https://git.io/JZKZV', 'https://git.io/JZKWX'))
# print(recomiendaPeliculas('https://git.io/JZKCJ', 'https://git.io/JZKnj', 'https://git.io/JZKW5'))

# # Privadas
# print(recomiendaPeliculas('https://git.io/JZKlE', 'https://git.io/JZKcq', 'https://git.io/JZKWh'))
# print(recomiendaPeliculas('https://git.io/JZKlM', 'https://git.io/JZKc8', 'https://git.io/JZKlJ'))
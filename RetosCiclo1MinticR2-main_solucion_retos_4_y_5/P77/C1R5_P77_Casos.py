import json
import pandas as pd
import numpy as np

def preProcesado(DF):
    
    categoriesDF = DF['categories'].apply(pd.Series)
    categoriesDF['title'] = DF['title']
    categoriesDF = categoriesDF.drop_duplicates(['title'])
    categoriesDF.set_index('title', inplace=True)

    categories = [categoriesDF[categorie].unique() for categorie in categoriesDF.columns]
    categories = [categorie for lista in categories for categorie in lista if all([pd.isnull(categorie) == False, categorie != ' ', categorie != '', len(str(categorie)) > 1])]
    categories = list(set(categories))

    return categoriesDF, categories

def codificaMatriz(DF, categories: list, producto: list):

    mCategories = pd.DataFrame(
        np.zeros((len(categories), len(producto))),
        index=categories,
        columns=list(producto))

    for book in DF.index:
        for index in DF:
            categorie = DF[index][book]
            if categorie in categories:
                mCategories[book][categorie] = 1

    return mCategories

def recomiendaLibro(url_puntuacion:str, url_perfil:str, url_recomendacion:str)->json:

    dataPerfil = pd.read_json(url_perfil)
    dataPerfil, categoriesPuntuacion = preProcesado(dataPerfil)
    
    librosPuntuacion = dataPerfil.index

    mCategories = codificaMatriz(dataPerfil, categoriesPuntuacion, librosPuntuacion)

    puntuacionLibro = pd.read_csv(url_puntuacion, sep=';', names=['title', 'peso'], index_col=['title'])

    for book in mCategories.columns:
        if book in puntuacionLibro.index:
            mCategories[book] = mCategories[book].apply(lambda point: float(point * puntuacionLibro['peso'][book]))

    mCategories['ponderacionPerfilUsuario'] = [mCategories.loc[categorie,:].sum() for categorie in mCategories.index]
    mCategories['ponderacionPerfilUsuario'] = mCategories['ponderacionPerfilUsuario'].apply(lambda point: point / mCategories['ponderacionPerfilUsuario'].sum())

    # Obtener libros a recomendar
    dataRecomendacion = pd.read_json(url_recomendacion)
    dataRecomendacion, categories = preProcesado(dataRecomendacion)
    
    libros = dataRecomendacion.index

    mRecomentacion = codificaMatriz(dataRecomendacion, categories, libros)
    mRecomentacion['ponderacion'] = mCategories['ponderacionPerfilUsuario']
    mRecomentacion = mRecomentacion.transpose()

    for book in mRecomentacion.columns:
        if book in categoriesPuntuacion:
            mRecomentacion[book] = mRecomentacion[book].apply(lambda point: float(point * mRecomentacion[book]['ponderacion']))
        else:
            mRecomentacion[book] = mRecomentacion[book].apply(lambda point: point * 0)
    
    mRecomentacion = mRecomentacion.drop(['ponderacion'])
    mRecomentacion = mRecomentacion.transpose()
    # print(mRecomentacion)
    
    recomendacionUsuario = pd.DataFrame(mRecomentacion.columns, columns=['libro'])
    recomendacionUsuario['peso'] = [mRecomentacion.loc[:,book].sum() for book in mRecomentacion.columns]
    # print(recomendacionUsuario)

    aRecomendar = recomendacionUsuario[recomendacionUsuario.peso > 0].sort_values('peso', ascending=False)
    aRecomendar['peso'] = aRecomendar['peso'].round(5)
    aRecomendar = {aRecomendar['libro'][i]:aRecomendar['peso'][i] for i in aRecomendar.index}
    return json.dumps(aRecomendar, indent=4)

# Publicos
print(recomiendaLibro('https://git.io/JZrTy','https://git.io/JZrOh','https://git.io/JZr32'))
print(recomiendaLibro('https://git.io/JZrn7','https://git.io/JZrK0','https://git.io/JZr6U'))

# Privadas
print(recomiendaLibro('https://git.io/JZryK','https://git.io/JZrST','https://git.io/JZrSC'))
print(recomiendaLibro('https://git.io/JZryF','https://git.io/JZrSO','https://git.io/JZrS6'))
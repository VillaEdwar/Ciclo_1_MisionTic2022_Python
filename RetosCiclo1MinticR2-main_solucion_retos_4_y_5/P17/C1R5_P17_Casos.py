import json
import pandas as pd
import numpy as np

def preProcesado(DF):
    
    categoriasDF = DF['categories'].apply(pd.Series)
    categoriasDF['business_id'] = DF['business_id']
    categoriasDF = categoriasDF.drop_duplicates(['business_id'])
    categoriasDF.set_index('business_id', inplace=True)

    categories = [categoriasDF[categorie].unique() for categorie in categoriasDF.columns]
    categories = [categorie for lista in categories for categorie in lista if all([pd.isnull(categorie) == False, categorie != ' ', categorie != '', len(str(categorie)) > 1])]
    categories = list(set(categories))

    return categoriasDF, categories

def codificaMatriz(DF, categories: list, producto: list):

    mcategories = pd.DataFrame(
        np.zeros((len(categories), len(producto))),
        index=categories,
        columns=list(producto))

    for business in DF.index:
        for index in DF:
            categorie = DF[index][business]
            if categorie in categories:
                mcategories[business][categorie] = 1

    return mcategories

def recomiendaNegocio(url_puntuacion:str, url_perfil:str, url_recomendacion:str)->json:

    dataPerfil = pd.read_json(url_perfil)
    dataPerfil, categoriesPuntuacion = preProcesado(dataPerfil)
    # print(dataPerfil, categoriesPuntuacion)
    businessPuntuacion = dataPerfil.index

    mcategories = codificaMatriz(dataPerfil, categoriesPuntuacion, businessPuntuacion)

    puntuacionNegocio = pd.read_csv(url_puntuacion, sep=';', names=['business_id', 'peso'], index_col=['business_id'])
    
    for business in mcategories.columns:
        if business in puntuacionNegocio.index:
            mcategories[business] = mcategories[business].apply(lambda point: float(point * puntuacionNegocio['peso'][business]))

    mcategories['ponderacionPerfilUsuario'] = [mcategories.loc[categorie,:].sum() for categorie in mcategories.index]
    mcategories['ponderacionPerfilUsuario'] = mcategories['ponderacionPerfilUsuario'].apply(lambda point: point / mcategories['ponderacionPerfilUsuario'].sum())

    dataRecomendacion = pd.read_json(url_recomendacion)
    dataRecomendacion, categories = preProcesado(dataRecomendacion)
    # print(dataRecomendacion, categories)
    negocios = dataRecomendacion.index

    mRecomentacion = codificaMatriz(dataRecomendacion, categories, negocios)
    mRecomentacion['ponderacion'] = mcategories['ponderacionPerfilUsuario']
    mRecomentacion = mRecomentacion.transpose()

    for business in mRecomentacion.columns:
        if business in categoriesPuntuacion:
            mRecomentacion[business] = mRecomentacion[business].apply(lambda point: float(point * mRecomentacion[business]['ponderacion']))
        else:
            mRecomentacion[business] = mRecomentacion[business].apply(lambda point: point * 0)
    
    mRecomentacion = mRecomentacion.drop(['ponderacion'])
    mRecomentacion = mRecomentacion.transpose()
    # print(mRecomentacion)
    
    recomendacionUsuario = pd.DataFrame(mRecomentacion.columns, columns=['business_id'])
    recomendacionUsuario['peso'] = [mRecomentacion.loc[:,business].sum() for business in mRecomentacion.columns]
    # print(recomendacionUsuario)

    aRecomendar = recomendacionUsuario[recomendacionUsuario.peso > 0].sort_values('peso', ascending=False)
    aRecomendar['peso'] = aRecomendar['peso'].round(5)
    aRecomendar = {aRecomendar['business_id'][i]:aRecomendar['peso'][i] for i in aRecomendar.index}
    return json.dumps(aRecomendar, indent=4)

# Publicos
print(recomiendaNegocio('https://git.io/JZKue', 'https://git.io/JZK0H', 'https://git.io/JZKE4'))
print(recomiendaNegocio('https://git.io/JZKuk', 'https://git.io/JZK0A', 'https://git.io/JZKEg'))

# # Privadas
# print(recomiendaNegocio('https://git.io/JZKuY', 'https://git.io/JZKEJ', 'https://git.io/JZKEJ'))
# print(recomiendaNegocio('https://git.io/JZKuz', 'https://git.io/JZKEY', 'https://git.io/JZKE5'))
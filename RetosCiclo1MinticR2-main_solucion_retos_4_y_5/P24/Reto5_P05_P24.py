def EstaCiudad(ruta_archivo:str,Ciudad : str):
    import pandas as pd
    import csv
    df2 = pd.read_csv(ruta_archivo,names = ['IdCiudad,NomCiudad','Cod_Ciudad','Habitantes'])
    a = df2.groupby(['Cod_Ciudad'])['Habitantes'].sum()
    diccionario = a.to_dict()
    sum = 0
    for i in diccionario:
        if i == Ciudad:
            dic_salida = {i:diccionario[i]}
    
    print(dic_salida)

#EstaCiudad('https://github.com/ebustosc/ebustosc/blob/main/Ciudades.csv?raw=true','Bogota01') 
#EstaCiudad('https://github.com/ebustosc/ebustosc/blob/main/Ciudades.csv?raw=true','Buga01') 
#EstaCiudad('https://github.com/ebustosc/ebustosc/blob/main/Ciudades.csv?raw=true','Cali01')
#EstaCiudad('https://github.com/ebustosc/ebustosc/blob/main/Ciudades.csv?raw=true','Medallo01')

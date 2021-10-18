def temp(ruta_archivo:str, opcion:int)->dict:
    import pandas as pd
    
    df2 = pd.read_csv(ruta_archivo,names = ['muestra','temperatura','codigo_maquina'])
    if opcion == 1:
        a = df2.groupby(['codigo_maquina'])['temperatura'].count()
        diccionario = a.to_dict()
    if opcion == 2:
        a = df2.groupby(['codigo_maquina'])['temperatura'].mean()
        diccionario = a.to_dict()
    if opcion == 3:
        a = df2.groupby(['codigo_maquina'])['temperatura'].max()
        diccionario = a.to_dict()
    if opcion == 4:
        a = df2.groupby(['codigo_maquina'])['temperatura'].min()
        diccionario = a.to_dict()
    if opcion == 5:
        a = df2['temperatura'].mean()
        diccionario = {'Promedio total temperatura': a}
  
    return diccionario
    
print(temp('https://raw.githubusercontent.com/marinacharris/retos/main/Temperatura.csv',1))
print(temp('https://raw.githubusercontent.com/marinacharris/retos/main/Temperatura.csv',2))
print(temp('https://raw.githubusercontent.com/marinacharris/retos/main/Temperatura.csv',5))
print(temp('https://raw.githubusercontent.com/marinacharris/retos/main/Temperatura.csv',3))
print(temp('https://raw.githubusercontent.com/marinacharris/retos/main/Temperatura.csv',4))


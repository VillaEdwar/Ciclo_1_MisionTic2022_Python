


def dosis_vacunas(ruta_archivo: str)-> dict:
        import pandas as pd
        pass

        if ruta_archivo.split('.')[-1] != 'csv':
                return 'Extension invalida.'
        else:
                datos = pd.read_csv(ruta_archivo)
                
                df=pd.DataFrame(datos)
                
                #Preparar el dataframe
                
                df['POR_CANT_ENTR']=df['CANT_ENTREGADA']*100/df['CANT_TOTAL']
                df['POR_CANT_ENTR']=round(df['POR_CANT_ENTR'],2)
                df['POR_CANT_PEND']=df['CANT_PENDIENTE']*100/df['CANT_TOTAL']
                df['POR_CANT_PEND']=round(df['POR_CANT_PEND'],2)
                df1=df.groupby(['MUNICIPIO'])[['POR_CANT_ENTR','POR_CANT_PEND']].sum()
                
           
                
                
                df1=df1.to_dict()
                
                return df1
                
                
               
 






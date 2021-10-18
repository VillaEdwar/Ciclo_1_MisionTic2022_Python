

def estaciones(ruta_archivo: str)-> dict:
        import pandas as pd
        pass

        if ruta_archivo.split('.')[-1] != 'csv':
                return 'Extension invalida.'
        else:
                datos = pd.read_csv(ruta_archivo)
                
                df=pd.DataFrame(datos)
               

                #Preparar el dataframe
                
                df['POR_GAL_VEN']=df['GALONES_VENDIDOS']*100/df['TOTAL_GALONES']
                df['POR_GAL_VEN']=round(df['POR_GAL_VEN'],2)
                df['POR_GAL_SOB']=df['GALONES_SOBRANTES']*100/df['TOTAL_GALONES']
                df['POR_GAL_SOB']=round(df['POR_GAL_SOB'],2)
                
                
                
                
                df1=df.groupby(['GASOLINERA'])[['POR_GAL_VEN','POR_GAL_SOB']].sum()
                
                
                df1=df1.to_dict()
                
                return df1

                

               





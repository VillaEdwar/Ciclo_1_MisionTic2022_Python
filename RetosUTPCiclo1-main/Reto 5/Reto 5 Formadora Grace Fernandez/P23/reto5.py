def casos_positivos(ruta_archivo: str)-> dict:
        import pandas as pd
        pass

        if ruta_archivo.split('.')[-1] != 'csv':
                return 'Extension invalida.'
        else:
                datos = pd.read_csv(ruta_archivo)
                
                df=pd.DataFrame(datos)
               

                #Preparar el dataframe
                
                df['POR_INFEC_MUJER']=df['INFECTADO_MUJER']*100/df['TOTAL_GENERAL']
                df['POR_INFEC_MUJER']=round(df['POR_INFEC_MUJER'],2)
                df['POR_INFEC_HOMBRE']=df['INFECTADO_HOMBRE']*100/df['TOTAL_GENERAL']
                df['POR_INFEC_HOMBRE']=round(df['POR_INFEC_HOMBRE'],2)
                
                df['POR_FALL_MUJER']=df['FALLECIDO_MUJER']*100/df['TOTAL_GENERAL']
                df['POR_FALL_MUJER']=round(df['POR_FALL_MUJER'],2)
                df['POR_FALL_HOMBRE']=df['FALLECIDO_HOMBRE']*100/df['TOTAL_GENERAL']
                df['POR_FALL_HOMBRE']=round(df['POR_FALL_HOMBRE'],2)
                
                
                df1=df.groupby(['DEPARTAMENTOS'])[['POR_INFEC_MUJER','POR_INFEC_HOMBRE','POR_FALL_MUJER','POR_FALL_HOMBRE']].sum()
                
                
                df1=df1.to_dict()
                
                return df1
        
        



        

                
 


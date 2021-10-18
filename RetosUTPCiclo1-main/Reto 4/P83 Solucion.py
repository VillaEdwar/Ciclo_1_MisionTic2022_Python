
def validar_victima(victima: dict)->tuple:
    
    fun = victima.copy()
    for codigo, registro in victima.items(): 
                departamento = registro['departamento']  
                for area in departamento:                
                    autorizado = area['autorizado']
                if autorizado == "no":
                    fun.pop(codigo)
    correos=listadoCorreos(fun)
    tupla=(correos,fun)                
    return(tupla)


def listadoCorreos(victima: dict) -> list:
    # Inicializacion Variables
    fun = victima.copy()
    baseCorreos = list()
    correos = set()
    # formato a minusculas sin acentos    
    for codigo in fun.keys():
        
        nombres = fun[codigo]['nombres'].lower()
        nombres = normalize(nombres)
       
        apellidos = fun[codigo]['apellidos'].lower() 
        apellidos = normalize(apellidos)
        
        baseCorreos.append((nombres, apellidos))
              
    for usuario in baseCorreos:
               
        coma = usuario[1].index(',')
        primerNombre = str(usuario[0][0]) # {primera letra del primer nombre}
        primerApellido = str(usuario[1][:coma]) # .{primer apellido}
            
        correos.add(primerNombre + '.' + primerApellido+"@gmail.com")
       
        
  
    correos = list(correos)             
    correosSeleccion = sorted(correos.copy())         
    return correosSeleccion

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("ñ", "n"),
    )
    for a, b in replacements:
        s = s.replace(a, b)
    return s


# Valores booleanos,tablas de verdad, y "&" "o"
'''
P: Hoy está haciendo frio
Q: Hoy es lunes
R: Hoy es un día de hacer deporte

1) Q ∨ R
Rpta: Hoy es lunes or Hoy es un día de hacer deporte

2) ¬ P ∧ ¬ R
Rpta: Hoy No está haciendo frio y Hoy NO es un día de hacer deporte

3) Q ∧ Q
Rpta: Hoy es lunes y Hoy es lunes
'''

#------------------------------------------------------------
#Entrada
# ----> hora militar
#Proceso
# ----> Teniendo en cuenta la hora militar, determinar si es PM o AM
#Salida
# ----> Mostrar si la hora militar es PM o AM

def validar_hora(hora):
    if(hora >= 12):
        mensaje = "PM"
    else:
        mensaje = "AM"
    
    return mensaje

hora_militar = int(input("Digite la hora militar: "))

print(validar_hora(hora_militar))
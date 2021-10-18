#funcion calcular ingresos
def calcular_ingresos(datos:dict) -> dict:
    #definiendo variables
    promedio_seguro_persona:float=0
    promedio_seguro_mascota:float=0
    sumapersonas=0
    sumarmascotas=0
    total:int=0
    contadormascotas=0
    contadorpersona=0
    #Definiendo la funcion
    for x in datos:
        if x["seguro"]== "persona":
            sumapersonas=sumapersonas + x["valor_a_pagar"]
            contadorpersona=contadorpersona+1
        else:
            if x["seguro"] == "mascota":
                sumarmascotas=sumarmascotas + x["valor_a_pagar"]
                contadormascotas=contadormascotas+1
        if contadormascotas==0:
            promedio_seguro_mascota=0
        else:
            promedio_seguro_mascota=round(sumarmascotas/contadormascotas,1)
        if contadorpersona==0:
            promedio_seguro_persona=0
        else:
            promedio_seguro_persona= round(sumapersonas/contadorpersona,1)
        
    total=sumapersonas+sumarmascotas
    respuesta={"total":total,"promedio_seguro_persona":promedio_seguro_persona, "promedio_seguro_mascota":promedio_seguro_mascota}
    return respuesta
datos=[
        {"seguro":"persona",
        "valor_a_pagar":20000
        },
        {"seguro":"mascota",
        "valor_a_pagar":25000
        },
        {"seguro":"persona",
        "valor_a_pagar":32000
        },
        {"seguro":"persona",
        "valor_a_pagar":18000
        },
        {"seguro":"mascota",
        "valor_a_pagar":5000
        },
        {"seguro":"persona",
        "valor_a_pagar":33000
        },
        {"seguro":"mascota",
        "valor_a_pagar":8000
        }
    ]
print(calcular_ingresos(datos))
    





def cajero(informacion:dict)->dict:    
    informacion = {
        "p1":"Banco ABS",
        "p2":"Carlos",
        "p3": 123,
        "p4": 798000,
        "p5": 800000,
        "p6": 0,
        "mensaje1":"El valor del costo, mas el costo de la transaccion es mayor que el saldo",
        "mensaje2": "El valor solicitado es mayor que su saldo acltual",
        "mensaje4":"Clave incorrecta",
        "mensaje5":"Muchas gracias"
        
    }
    if informacion["p3"] == 123:
        if informacion["p4"] > 200000:
            informacion["p4"] = informacion["p4"] + 2000
            if informacion["p4"] <= informacion["p5"]:
                informacion["p6"] = informacion["p5"] - informacion["p4"]
                respuesta={"Banco: ":informacion["p1"], "Usuario: ":informacion["p2"],
                 "Clave: ":informacion["p3"], "Retiro: ":informacion["p4"], 
                 "Saldo inicial: ":informacion["p5"], "Nuevo saldo: ":informacion["p6"],
                  "Su saldo actual es: ":informacion["p6"], ": Mensaje: ":informacion["mensaje5"]}
            else:
                respuesta={"Mensaje: ":informacion["mensaje1"]}
        else:
            if informacion["p4"] <= informacion["p5"]:
                informacion["p6"] = informacion["p5"] * informacion["p4"]
                respuesta={"su saldo actual es: ":informacion["p6"], "Mensaje":informacion["mensaje5"]}
            else:
                respuesta={"Mensaje":informacion["mensaje2"]}
    else:
        respuesta={"Banco: ":informacion["p1"], "Usuario: ":informacion["p2"],
                 "Clave: ":informacion["p3"], "Retiro: ":informacion["p4"], 
                 "Saldo inicial: ":informacion["p5"], "Nuevo saldo: ":informacion["p6"], "Su saldo actual es: ":informacion["p6"], "Mensaje: ":informacion["mensaje4"]}
    print(respuesta)
cajero(informacion=cajero)
        

    
                


    

    



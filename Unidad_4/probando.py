#Prueba
datos = {
    "01": {
        "nombre": "Ahorrar",
        "nit": "34545678",
        "url": "www.ahorrar.com.co",
        "transacciones": [
            {
                "enero": {
                    "sede1": 250,
                    "sede2": 200,
                    "sede3": 100,
                    "sede4": 150
                }
            },
            {
                "febrero": {
                    "sede1": 200,
                    "sede2": 50,
                    "sede3": 200,
                    "sede4": 250
                }
            },
            {
                "marzo": {
                    "sede1": 100,
                    "sede2": 500,
                    "sede3": 20,
                    "sede4": 250
                }
            },
            {
                "abril": {
                    "sede1": 1000,
                    "sede2": 50,
                    "sede3": 200,
                    "sede4": 250
                }
            },
            {
                "mayo": {
                    "sede1": 400,
                    "sede2": 500,
                    "sede3": 20,
                    "sede4": 250
                }
            },
            {
                "junio": {
                    "sede1": 1000,
                    "sede2": 50,
                    "sede3": 200,
                    "sede4": 250
                }
            },
            {
                "julio": {
                    "sede1": 300,
                    "sede2": 50,
                    "sede3": 2000,
                    "sede4": 150
                }
            },
            {
                "agosto": {
                    "sede1": 100,
                    "sede2": 150,
                    "sede3": 200,
                    "sede4": 250
                }
            },
            {
                "septiembre": {
                    "sede1": 100,
                    "sede2": 510,
                    "sede3": 1000,
                    "sede4": 250
                }
            },
            {
                "octubre": {
                    "sede1": 100,
                    "sede2": 500,
                    "sede3": 100,
                    "sede4": 250
                }
            },
            {
                "noviembre": {
                    "sede1": 100,
                    "sede2": 50,
                    "sede3": 100,
                    "sede4": 250
                }
            },
            {
                "diciembre": {
                    "sede1": 100,
                    "sede2": 500,
                    "sede3": 100,
                    "sede4": 350
                }
            }
        ]
    },
    "02": {
        "nombre": "Guardar",
        "nit": "34567123",
        "url": "www.guardar.com.co",
        "transacciones": [
            {
                "enero": {
                    "sede1": 150,
                    "sede2": 1000,
                    "sede3": 200,
                    "sede4": 2500
                }
            },
            {
                "febrero": {
                    "sede1": 1000,
                    "sede2": 550,
                    "sede3": 200,
                    "sede4": 2500
                }
            },
            {
                "marzo": {
                    "sede1": 100,
                    "sede2": 500,
                    "sede3": 400,
                    "sede4": 250
                }
            },
            {
                "abril": {
                    "sede1": 200,
                    "sede2": 50,
                    "sede3": 200,
                    "sede4": 50
                }
            },
            {
                "mayo": {
                    "sede1": 1000,
                    "sede2": 50,
                    "sede3": 100,
                    "sede4": 250
                }
            },
            {
                "junio": {
                    "sede1": 300,
                    "sede2": 500,
                    "sede3": 200,
                    "sede4": 250
                }
            },
            {
                "julio": {
                    "sede1": 50,
                    "sede2": 500,
                    "sede3": 100,
                    "sede4": 150
                }
            },
            {
                "agosto": {
                    "sede1": 100,
                    "sede2": 50,
                    "sede3": 100,
                    "sede4": 250
                }
            },
            {
                "septiembre": {
                    "sede1": 1000,
                    "sede2": 350,
                    "sede3": 100,
                    "sede4": 50
                }
            },
            {
                "octubre": {
                    "sede1": 100,
                    "sede2": 50,
                    "sede3": 20,
                    "sede4": 25
                }
            },
            {
                "noviembre": {
                    "sede1": 100,
                    "sede2": 50,
                    "sede3": 200,
                    "sede4": 250
                }
            },
            {
                "diciembre": {
                    "sede1": 100,
                    "sede2": 50,
                    "sede3": 500,
                    "sede4": 250
                }
            }
        ]
    }
}

print("Mi primera impresion")
print(datos)
print (datos["01"])
print (datos["01"]["nombre"])
print (datos["01"]["nit"])
print (datos["01"]["url"])
print (datos["01"]["transacciones"])
print (datos["01"]["transacciones"][0])
print (datos["01"]["transacciones"][0]["enero"])
print (datos["01"]["transacciones"][0]["enero"]["sede1"])

print(datos["01"]["transacciones"][0]["enero"].values())
a=datos["01"]["transacciones"][0]["enero"].values()
b=list(a)
print(a)
print(b)

print("Mi segunda impresion")
print(datos)
print (datos["02"])
print (datos["02"]["nombre"])
print (datos["02"]["nit"])
print (datos["02"]["url"])
print (datos["02"]["transacciones"])
print (datos["02"]["transacciones"][0])
print (datos["02"]["transacciones"][0]["enero"])
print (datos["02"]["transacciones"][0]["enero"]["sede1"])

print(datos["02"]["transacciones"][0]["enero"].values())
a=datos["02"]["transacciones"][0]["enero"].values()
b=list(a)
print(a)
print(b)
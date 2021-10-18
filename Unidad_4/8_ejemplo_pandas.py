import pandas as pd

ventas = pd.Series([15,12,21], index = ["Ene", "Feb", "Mar"])
print(ventas)

print(ventas[0])

print(ventas["Ene"])

print(ventas.index)
print(ventas.values)

ventas.name = "Ventas 2021"
print(ventas.name)
print(ventas)

ventas.index.name = "Meses"
print(ventas)


datos = { 'manzanas' : [ 3 , 2 , 0 , 1 ], 'naranjas' : [ 0 , 3 , 7 , 2 ] }

compras = pd.DataFrame( datos )

print(compras)

compras = pd.DataFrame( datos , index = [ 'Juno' , 'Robert' , 'Lily' , 'David' ])  

print(compras)

print(compras.index)

print(compras.columns)

compras.index.name = "Clientes"
compras.columns.name = "Frutas"
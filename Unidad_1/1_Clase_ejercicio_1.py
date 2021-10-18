# Esto es un comentario
''' esto es un comentario
de varias lineas+'''
'''
#----------------------------
# Primer ejemplo de declaraciond e variable
var1 = 1.20 
print(var1)
print(type(var1))
var1 = int(var1)
print(var1)
#-----------------------------
var1 = 120
var2 = var1
print(var2)
#-----------------------------
'''
# Entradas
m = 15.5
a = 300.8
# Proceso
f = m * a
# Salida
print(f)
print("El resultado de multiplicar la masa {} y la aceleracion {} fue: {}".format(m,a,f))
print("El resultado de multiplicar la masa",m,"y la aceleracion",a,"fue:",f)
print(f"El resultado de multiplicar la masa {m} y la aceleracion {a} fue: {f}")
print("El resultado de multiplicar la masa " + str(m) + " y la aceleracion " + str(a) + " fue: " + str(f))
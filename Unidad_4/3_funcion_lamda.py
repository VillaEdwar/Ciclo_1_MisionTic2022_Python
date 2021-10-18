#Funciones lambda
convertir = lambda valor: f"${valor}"
print(convertir(5000))

suma_numeros = lambda n1,n2: n1 + n2
print(suma_numeros(2,3))

'''
promedio = lambda v1,v2,v3: (v1+v2+v3)/3
print( promedio(5,10,15) )

#Retorne una lista de Ni hasta Nf
nueva_lista = lambda i,f: [x for x in range(i,f)]
print( nueva_lista(1,201) )

elevar_al_cubo = lambda n: n**3
print(elevar_al_cubo(3))
'''

#Funciones lambda
convertir = lambda valor: f"${valor}"
print(convertir(5000))

suma_numeros = lambda n1,n2: n1 + n2
print(suma_numeros(2,3))

promedio = lambda v1,v2,v3: (v1+v2+v3)/3
print( promedio(5,10,15) )

#Retorne una lista de Ni hasta Nf
nueva_lista = lambda i,f: [x for x in range(i,f) if x%3 == 0]
print( nueva_lista(1,201) )

elevar_al_cubo = lambda n: n**3
#print(elevar_al_cubo(3))
'''
mi_lista = []
for x in range(4, 31, 2):
    mi_lista.append(x)
print(mi_lista)

print ([x for x in range(4, 31, 2)])

print( [x**2 for x in range(4, 31, 2) if x%3 == 0] )
'''
#----- peliculas-----

pelis = ["El perfume", "Mi pobre angelito", "El principe de persia",
"King Kong", "El paseo 5", "El castigador"]

'''
pelisdeldomingo = []
for titulo in pelis:
    if titulo.startswith("E"):
        pelisdeldomingo.append(titulo)

print(pelisdeldomingo)
'''
print([titulo for titulo in pelis if titulo.startswith("E")])


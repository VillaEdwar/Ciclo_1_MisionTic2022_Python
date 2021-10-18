def contar_palabras_repetidas(frase):
    dic = {}
    for palabra in frase.split():
        if palabra[-1] == ',':
            palabra = palabra[:len(palabra)-1]
        c = 0
        for palabra2 in frase.split():
            if palabra2[-1] == ',':
                palabra2 = palabra2[:len(palabra2)-1]
            if palabra == palabra2:
                c += 1
        if c > 1:
            dic[palabra] = c
    return dic

def procesar_frase(frase_celebre_programacion: str)->list:
    palabras_rep = list(map(contar_palabras_repetidas, frase_celebre_programacion.split('xyz')))
    return palabras_rep[0]
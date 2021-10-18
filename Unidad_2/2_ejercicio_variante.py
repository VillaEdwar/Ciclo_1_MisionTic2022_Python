print("Bienvenido al Juego MisiónTIC2022")

total_preguntas = 4 #Cantidad de preguntas
puntaje = 0 #Variable que almacena puntaje obtenido por pregunta

respuesta = int(input("1. ¿En que año estamos? "))
if respuesta == 2021:
    print("Correcto")
    puntaje = puntaje + 1 # puntaje += 1
else:
    print("Incorrecto")

respuesta = input("2. ¿Cuánto es 8 + 4 + 1 - 4 - 2? ")
if respuesta == "7" or respuesta.lower() == "siete":
    print("Correcto")
    puntaje = puntaje + 1
else:
    print("Incorrecto")
respuesta = input("3. ¿Cuál es el mejor lenguaje de programación? ")
if respuesta.lower() == "python":
    print("Correcto")
    puntaje = puntaje + 1
else:
    print("Incorrecto")

respuesta = input("4. ¿Cuál es el deporte favorito de los Colombianos?")
if respuesta.lower() == "fútbol" or respuesta.lower() == "ciclismo":
    print("Correcto")
    puntaje = puntaje + 1
else:
    print("Incorrecto")

porcentaje = (puntaje / total_preguntas) * 100
print("Respuestas {} de {} corresponde al {}%".format(puntaje,total_preguntas,porcentaje))
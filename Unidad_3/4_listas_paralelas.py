nombres = []
edades = []
for x in range(5):
    nom=input("Ingrese el nombre de la persona: ")
    nombres.append(nom)
    ed=int(input("Ingrese la edad de la persona: "))
    edades.append(ed)

print(nombres)
print(edades)

print("Nombres de las personas mayores de edad: ")
for x in range(5):
    if edades[x] >= 18:
        print(nombres[x])
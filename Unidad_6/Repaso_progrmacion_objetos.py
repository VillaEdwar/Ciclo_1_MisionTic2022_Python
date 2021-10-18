# Lenguaje modealdo unificado (UML)
# Todo lo que veamos en un mundo real lo podemos categorizar como una clase
# La clase de objetos va a tener un Nombre, atributo(cracteristicas) y metodo(acciones yu operaciones)
# Diagrams.net es de google, http://draw.io/
# Carro(nombre) marca chasis, color, nuemro de pruebas, tipo(atributos) purcahses parking pass, encender, avanzar, frenar (metodo)
# Instanciar o crear un una clase es convertirla en objeto, es decir podems hablar de carro( la clase es una Fabrica de objetos)
# Hablo de obejtoc cuando materializo la clase

class Carro:

    def __init__(self) -> None:
        self.marca = input("Marca: ")
        self.chasis = input("Chasis: ")
        self.color = input("Color: ")
        self.numeroPuertas = input("Número de Puertas: ")
        self.tipo = input("Tipo de carro: ")
    
    def imprimir(self):
        print("Marca", self.marca)
        print("Chasis", self.chasis)
        print("Color", self.color)
        print("Número de Puertas", self.numeroPuertas)
        print("Tipo de Carro", self.tipo)
    
    def encender(self):
        print("El carro está encendido...")
    
    def avanzar(self):
        print("El carro está avanzando...")

    def frenar(self):
        print("El carro se detuvo")

    def girar(self):
        print("El carro está girando...")

objCarrito1 = Carro()
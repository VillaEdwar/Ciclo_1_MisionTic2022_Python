'''
#las funciones no ejecutan intrusccino, ellas van y cargan en memori las intruscciones

def funcion():
    return ""

#Foco
#Primero propiedades
Class FocoDeLuz:
    #propiedad  privada con __
    __estaEncendido = False
    tamaño = 0; voltaje=0; intensidad=""; potencia =0; #cm, voltios,lumens, wats
    
    #segundo defiimos el constructor(inicializador), el la mayoria de los lenguajes el constructor debe llamarse igual que la clase
    #si no se deine un constructor el sistema lo define como vacio, define variable y da el espacio. puede ir pass
    def __init__(self,tamañoPar,voltajePar,intensidadPar,potenciaPar,tipoFocopar): #(el objeto que se instancia, paraemtro)
        self.tamaño = tamañoPar
        self.voltaje = voltajePar
        self.intensidad = intensidadPar
        self.potencia = potenciaPar
        self.tipoFoco = tipoFocopar
        return
    #funciones, metodos o acciones

    def Prender(self):
        print("el foco se encendio")
    def Apagar(self):
        print("el foco se apago")
    def mostrarPropiedades(self):
        print("El tamaño de es: " + str(self.tamaño))
        print("El voltaje de es: " + str(self.voltaje))
        print("El la itnensidad de es: " + str(self.intensidad))
        print("El tipo de foco es de es: " + str(self.tipoFoco))
        print("--------------------------------")
        

objetoFocoLuz = FocoDeLuz(5,120,"lumens",15, ahorrador)
#direccion de memoria, el punto indica vaya a otra direccion de memoria
objetoFocoLuz.tamaño
'''
#Codigo del profe
class FocoDeLuz:
    #__estaEncendido = False
    #tamano = 0; voltaje = 0; intensidad = ''; potencia = 0; tipoFoco='' #cm, voltios, lumens , watts
    def __init__(self,tamanoPar,voltajePar,intensidadPar,potenciaPar,tipofocoPar):
        self.tamano = tamanoPar
        self.voltaje = voltajePar
        self.intensidad = intensidadPar
        self.potencia = potenciaPar
        self.tipoFoco = tipofocoPar
        self.__estaEncendido = False
    def Prender(self):
        print('El foco se encendio')
        self.__estaEncendido = True
    def Apagar(self):
        print('El foco se apago')
        self.__estaEncendido = False
    def mostrarPropiedades(self):
        print('----------------------')
        print('El tamaño del foco es: ' + str(self.tamano) )
        print('El Voltaje del foco es: ' + str(self.voltaje) )
        print('La intensidad del foco es: ' + str(self.intensidad) )
        print('La potencia del foco es: ' + str(self.potencia) )
        print('El tipo de foco es: ' + str(self.tipoFoco)

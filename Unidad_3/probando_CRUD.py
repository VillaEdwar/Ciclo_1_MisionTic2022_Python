
#Inicialización de tareas (desde el código)
tareas = {
    '01': { 
            'descripcion':'Ir a mercar',
            'estado' : 'pendiente',
            'tiempo' : 60            
           },
    '02': { 
            'descripcion':'Estudiar',
            'estado' : 'pendiente',
            'tiempo' : 180            
           }, 
    '03': { 
            'descripcion':'Hacer ejercicio',
            'estado' : 'pendiente',
            'tiempo' : 50            
           } 
}
mainloop = True
while mainloop: 
    print(" ")
    print("-- Aplicación CRUD TareasPendientes ---")
    print("1. Adicionar Tarea")
    print("2. Consultar Tareas")
    print("3. Actualizar Tarea")
    print("4. Eliminar Tarea")
    print("5. Salir")
    opcion = int(input("Ingrese una opción: "))
    #create
    if opcion == 1:
        print("Creando tarea->")
        identificador = input("ingrese un")
        nuevoDiccionario ={
            "Descripcion"


        }

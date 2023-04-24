
while True:
    print("\nMenu de Acciones\n")
    print("1. Nueva Partida")
    print("2. Cargar Partida")
    print("3. Salir")

    accion=input("Escoja una accion opción con un numero del 1 al 3:  ")
    
    try:
        accion=int(accion)
    except (ValueError) as error:
        print("La accion debe ser un número")
        continue


    










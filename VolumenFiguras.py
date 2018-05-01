# definimos la funcion cubo
import math
def VolumenCubo():
    print("\n\t\tCubo")
    lado = (float)(input("Introduzca un lado del cubo: "))
    volumencubo = math.pow(lado,3)
    print("El volumen del cubo es: ",'%.2f' % volumencubo , "m^3")
# Definimos la funcion menu con las opciones

def menu():
    print("\nMenu\n"
          +"1.VolumenCubo\n"
          +"2.Volumen----\n"
          +"3.Volumen----\n"
          +"4.Salir\n")

# Menu de opciones para usarlas
def MenuFiguras():
    # Inicalizacion de la variable opciones
    opciones = 0
    print("\t\tBienvenido")

    # Uso de while para crear un repeticion de menu
    while opciones != 4:
        # Llamamos a la funcion menu
        menu()
        # Introducimos la opcion en int
        opciones = (int)(input("Elija una opcion: "))
        if opciones == 1:
        # Llamamos a la funcion cubo para realizar la operacion del volumen
            VolumenCubo();
        elif opciones == 4:
            print("Gracias por usar el programa")
        else:
            print("Ingrese una opcion valida")

MenuFiguras()
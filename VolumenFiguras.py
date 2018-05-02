# definimos la funcion cubo
import math

def VolumenCubo():
    print("\n\t\tCubo")
    lado = (float)(input("Introduzca un lado del cubo: "))
    volumencubo = math.pow(lado,3)
    print("El volumen del cubo es: ",'%.2f' % volumencubo , "m^3")

def VolumenEsfera():
    print("\n\t\tEsfera")
    radio = (float)(input("Introduzca el radio de la esfera: "))
    volumenesfera = (4/3)*math.pi*math.pow(radio,3)
    print(f"El volumen de la esfera es: ",volumenesfera,"m^3")

# Definimos la funcion menu con las opciones

def menu():
    print("\nMenu\n"
          +"1.VolumenCubo\n"
          +"2.VolumenEsfera\n"
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
        if opciones == 2:
        # Calculo del volumen de la esfera
            VolumenEsfera();
        elif opciones == 4:
            print("Gracias por usar el programa")
        else:
            print("Ingrese una opcion valida")

#Funcion Principal

if __name__ == '__main__':
    MenuFiguras()
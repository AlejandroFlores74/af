__author__ = 'examen'

from Opciones import *

def menu():
    n = validate(0)
    vector = n * [None]
    bandera = False
    op = -1
    while op != 6:
        print()
        print("1) Cargar por teclado el vector validando que el número de cabina sea efectivamente un número entre 1 y 15).")
        print("2) Mostrar todos los datos de los vehículos que hayan pasado por la cabina 1 sin pagar peaje")
        print("(es decir, los datos de los vehículos que pasaron por esa cabina y tienen registrado un importe o pago igual a 0).")
        print("3) Mostrar todos los datos ordenados por patente de menor a mayor. Utilice el método de ordenamiento que prefiera.")
        print("4) Determine el importe acumulado que se registró por cada cabina (el importe acumulado por vehículos que pasaron")
        print("por la cabina 1, lo mismo para la cabina 2, y así con las 15 cabinas).")
        print("5) Cargue por teclado una patente p y determine cuántas veces la misma está registrada en el ")
        print("vector. Muestre todos sus datos e indique cuántas veces aparece. Si esa patente no existe, informe con un mensaje.")
        print("6) Salir.")
        print("------------------------------------------------------------")
        op = int(input("Ingrese opcion requerida: "))
        if op == 1:
            inicio(vector)
            bandera = True
            print("------------ VECTOR ----------------")
            write(vector)
        elif op == 2:
            if bandera:
                vec = opcion2(vector)
                if len(vec) != 0:
                    print("-------- VEHICULOS QUE PASARON POR CABINA 1 SIN PAGAR ---------")
                    write(vec)
                else:
                    print("No se encontro ningun dato!!")
            else:
                print("Debe cargar el vector!!")
        elif op == 3:
            if bandera:
                v = opcion3(vector)
                print("----------- DATOS ORDENADOS POR PATENTE DE MENOR A MAYOR -----------")
                write(v)
            else:
                print("Debe cargar el vector!!")
        elif op == 4:
            if bandera:
                print("----------- IMPORTE ACUMULADO POR CABINA -----------------")
                opcion4(vector)
            else:
                print("Debe cargar el vector!!")
        elif op == 5:
            if bandera:
                p = int(input("Ingrese patente: "))
                nuevo = opcion5(vector, p)
                if len(nuevo) != 0:
                    print("------------ BUSQUEDA DE PATENTE -----------------")
                    write(nuevo)
                    print()
                    print("La patente aparecio: ", len(nuevo), "veces.")
                else:
                    print("No se encontro ninguna vez la patente!!")
            else:
                print("Debe cargar el vector!!")
        elif op == 6:
            print("Gracias por usar el programa!!")
        else:
            print("Opcion incorrecta!!")

menu()
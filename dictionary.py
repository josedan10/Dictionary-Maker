#___________________ DICTIONARY MAKER ___________________#
#Este programa realiza combinaciones utilizando palabras claves introducidas por
#el usuario.

"""Analisis de posibles combinaciones

1.- Mezcla de datos.
2.- Mezcla de datos inversos.
3.- Numero de datos variables.
4.- Largo de los strings variables.
5.- Mayusculas y minusculas.
6.- Cambiar letras por numeros.
7.- Numero minimo de datos."""



#__________ Procedimientos matematicos a usar __________#
"""
1.- Permutaciones
2.- Permutaciones con repeticion
3.- Variaciones
4.- Variaciones con repeticion
5.- Combinatorios
6.- Combinatorios con repeticion """

from Conteo import *
from lectura import *
from menus import *
#from objetos import *


print("BIENVENIDO A DICTONARY MAKER")
print("Desarrollado por Jose Daniel\n")
print("Este programa esta hecho para generar diccionarios en funcion de informacion recopilada "
      "por el usuario.")


while True:

    menuPrincipal()
    opcion = int(input("\nIntroduzca su opcion: "))

    if (opcion == 1):
        print("Llamar a la funcion que imprime el formato de archivo")

    elif (opcion == 2):
        print("\nIntroduzca el nombre del archivo que contine los datos")
        nombreArchivo = input("Archivo: ")
        victima = leerArchivoDatos(nombreArchivo)

        if (victima == False):
            print("Operacion abortada. Se recomienda actualizar los datos del archivo")
            print("Gracias por usar DictonaryMaker By Jose Quintero\n")
            break

        listaDeDatos = armarListaDeDatos(victima)


    elif (opcion == 3):
        print("Gracias por usar DictonaryMaker By Jose Quintero\n")
        break

    else:
        print("Opcion invalida\n")
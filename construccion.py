def crearDiccionario(listaDeDatos):


    formarVariacionesBase(listaDeDatos)
    clave = ""
    contador = 1 #Contador de lineas

    while not (clave == "\n"):
        ####################################################################
        #       Asignamos la clave base
        variacionesBase = open("variaciones.txt", "r")

        for i in range(0, contador):
            clave = variacionesBase.readline()

        variacionesBase.close()
        ####################################################################
        #       Formamos variaciones con la clave base

        ####################################################################


    return


def variacionPalabras(palabra):


    variacion = []

    variacion.append(palabra)
    variacion.append(palabra.upper()) #Palabra en mayúsculas completamente
    variacion.append(palabra.lower()) #Palabra en minúsculas completamente

    return variacion

def variacionNumerica(numero):

    variacion = []

    variacion.append(numero)
    numeroInverso = ""

    #Numeros invertidos
    for i in numero:
        numeroInverso = i + numeroInverso

    variacion.append(numeroInverso)

    return variacion

def formarVariacionesBase(listaDeDatos):


    # Primera vez creando el archivo
    variaciones = open("variaciones.txt", "w+")

    for elemento in listaDeDatos:

        if type(elemento) == 'int':
            variaciones.write(str(elemento))
            variaciones.write("\n")
            continue

        # Si es un dato de tipo numerico
        if elemento.isnumeric():
            listaVariacion = variacionNumerica(elemento)

        else:
            listaVariacion = variacionPalabras(elemento)

        # Escribimos cada variación en el archivo de variaciones
        for variacion in listaVariacion:
            variaciones.write(variacion)
            variaciones.write("\n")

    variaciones.close()

    return


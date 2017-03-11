from objetos import *
from datetime import datetime

def leerArchivoDatos(nombreDeArchivo):


    cuenta = Cuenta()
    persona = Persona()

    print("\nLeyendo datos ...")


    file = open(nombreDeArchivo, "r")
    file.readline()# La primera linea es la del titulo
    file.readline()

    cuenta.tipo = file.readline()
    cuenta.tipo = cuenta.tipo[cuenta.tipo.find(":")+2:]

    cuenta.usuario = file.readline()
    cuenta.usuario = cuenta.usuario[cuenta.usuario.find(":")+2:]

    cuenta.fechaCreacion = file.readline()
    cuenta.fechaCreacion = cuenta.fechaCreacion[cuenta.fechaCreacion.find(":")+2:]

    fechaArchivo = file.readline()
    fechaArchivo = fechaArchivo[fechaArchivo.find(":")+2:]

    if (datetime.now().year - int(fechaArchivo[6:]) > 5 ):

        continuar = input("\nPuede que los datos del archivo esten desactualizados "
                          "¿desea continuar? [Y/N]: ")

        while(not(continuar.upper() == "Y") and not(continuar.upper() == "N")):

            continuar = input("\nOpcion invalida. ¿Desea continuar con los datos desactualizados? "
                              "[Y/N]: ")

        if (continuar == "N" or continuar == "n"):
            return False

    print(file.readline())

    persona.nombreCompleto = file.readline()
    persona.nombreCompleto = persona.nombreCompleto[persona.nombreCompleto.find(":")+2:]

    persona.ID = file.readline()
    persona.ID = persona.ID[persona.ID.find(":")+2:]

    persona.edad = file.readline()
    persona.edad = int(persona.edad[persona.edad.find(":")+2:])

    persona.sexo = file.readline()
    persona.sexo = persona.sexo[persona.sexo.find(":")+2:]

    persona.fechaNac = file.readline()
    persona.fechaNac = persona.fechaNac[persona.fechaNac.find(":")+2:]

    persona.tlf = file.readline()
    persona.tlf = persona.tlf[persona.tlf.find(":")+2:]

    cuenta.correo = file.readline()
    cuenta.correo = cuenta.correo[cuenta.correo.find(":")+2:]

    victima = Victima(persona, cuenta)

    victima.sobreNombres = file.readline()
    victima.sobreNombres = victima.sobreNombres[victima.sobreNombres.find(":")+2:]

    victima.paisNatal = file.readline()
    victima.paisNatal = victima.paisNatal[victima.paisNatal.find(":")+2:]

    victima.paisRes = file.readline()
    victima.paisRes = victima.paisRes[victima.paisRes.find(":")+2:]

    victima.zona = file.readline()
    victima.zona = victima.zona[victima.zona.find(":")+2:]

    victima.nroFav = file.readline()
    victima.nroFav = victima.nroFav[victima.nroFav.find(":")+2:]

    victima.color = file.readline()
    victima.color = victima.color[victima.color.find(":")+2:]

    victima.musica = file.readline()
    victima.musica = victima.musica[victima.musica.find(":")+2:]

    victima.mascotas = file.readline()
    victima.mascotas = victima.mascotas[victima.mascotas.find(":")+2:]

    victima.hermanos = file.readline()
    victima.hermanos = victima.hermanos[victima.hermanos.find(":")+2:]

    victima.actividades = file.readline()
    victima.actividades = victima.actividades[victima.actividades.find(":")+2:]

    victima.hijos = file.readline()
    victima.hijos = victima.hijos[victima.hijos.find(":")+2:]

    victima.parejas = file.readline()
    victima.parejas = victima.parejas[victima.parejas.find(":")+2:]

    victima.fechasImportantes = file.readline()
    victima.fechasImportantes = victima.fechasImportantes[victima.fechasImportantes.find(":")+2:]

    victima.deportes = file.readline()
    victima.deportes = victima.deportes[victima.deportes.find(":")+2:]

    victima.equipos = file.readline()
    victima.equipos = victima.equipos[victima.equipos.find(":")+2:]

    victima.animales = file.readline()
    victima.animales = victima.animales[victima.animales.find(":")+2:]

    victima.comidas = file.readline()
    victima.comidas = victima.comidas[victima.comidas.find(":")+2:]

    victima.estudios = file.readline()
    victima.estudios = victima.estudios[victima.estudios.find(":")+2:]

    victima.sitios = file.readline()
    victima.sitios = victima.sitios[victima.sitios.find(":")+2:]

    victima.idolos = file.readline()
    victima.idolos = victima.idolos[victima.idolos.find(":")+2:]

    victima.seriesYPelis = file.readline()
    victima.seriesYPelis = victima.seriesYPelis[victima.seriesYPelis.find(":")+2:]

    victima.descripcion = file.readline()
    victima.descripcion = victima.descripcion[victima.descripcion.find(":")+2:]


    return victima

def combinar(palabras, palabrasCopia, extras):
    """Combinacion de todas las palabras que hay en el archivo de datos"""



    return

def armarListaDeDatos(victima):
    """Armamos la lista con los datos de la victima"""

    #Ya agregamos los atributos por separado.
    #TO DO:
        #Quitar los espacios de los elementos que estan separados (ej: Mr. Robot)
        #Quitar los saltos de linea (ej: Naruto\n)

    listaDeDatos = []

    for atributo in victima.__dict__:

        if (type(victima.__dict__[atributo]) == int):
            listaDeDatos.append(victima.__dict__[atributo])
            continue

        if (victima.__dict__[atributo].find(",") > 0):

            #Esto es una lista
            lista = victima.__dict__[atributo].split(', ')

            for elemento in lista:
                if (elemento[len(elemento)-1]=='\n'):
                    elemento = elemento[:len(elemento)-1]

                if (elemento == '-'):
                    continue
                listaDeDatos.append(elemento)

            #print("Esto es una lista")
        else:

            if(victima.__dict__[atributo]=='-'):
                continue

            if (victima.__dict__[atributo][len(victima.__dict__[atributo]) - 1] == '\n'):
                victima.__dict__[atributo] = victima.__dict__[atributo][:len(victima.__dict__[atributo]) - 1]
            listaDeDatos.append(victima.__dict__[atributo])

    return listaDeDatos
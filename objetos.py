class Persona(object):


    def __init__(self):
        self.nombreCompleto = ""
        self.ID = 0
        self.edad = 0
        self.sexo = ""
        self.fechaNac = ""
        self.tlf = ""

class Victima(Persona):



    def __init__(self, persona, cuenta):

        self.nombreCompleto = persona.nombreCompleto
        self.sobreNombres = ""
        self.ID = persona.ID
        self.correo = cuenta.correo
        self.edad = persona.edad
        self.sexo = persona.sexo
        self.fechaNac = persona.fechaNac
        self.tlf = persona.tlf
        self.paisNatal = ""
        self.paisRes = ""
        self.zona = ""
        self.nroFav = 0
        self.color = ""
        self.musica = [] #Array
        self.mascotas = [] #Array
        self.hermanos = [] #Array
        self.actividades = [] #Array
        self.hijos = [] #Array
        self.parejas = [] #Array
        self.fechasImportantes = [] #Array
        self.deportes = [] #Array
        self.equipos = [] #Array
        self.animales = [] #Array
        self.comidas = [] #Array
        self.estudios = [] #Array
        self.sitios = [] #Array
        self.idolos = [] #Array
        self.seriesYPelis = [] #Array
        self.descripcion = [] #Array

    def __str__(self):

        nombre = "Victima: " + self.nombreCompleto + "\n"
        ID = "ID: " + str(self.ID) + "\n"
        sexo = "Sexo: " + self.sexo + "\n"
        edad = "Edad: " + str(self.edad) + "\n"

        return nombre + ID + sexo + edad

class Cuenta(object):


    def __init__(self):
        self.tipo = ""
        self.usuario = ""
        self.correo = ""
        self.password = ""
        self.fechaCreacion = ""

    def __str__(self):

        cuenta = "Datos de la cuenta de " + self.tipo + "\n"
        usuario = "Usuario: " + self.usuario + "\n"
        correo = "Correo: " + self.correo + "\n"
        password = "Password: " + self.password + "\n"
        fecha = "Fecha de creacion: " + self.fechaCreacion + "\n"

        if (usuario == ""):
            return cuenta +  correo + password + fecha

        elif (correo == ""):
            return cuenta + usuario + password + fecha

        else:
            return cuenta + usuario + password + correo + fecha
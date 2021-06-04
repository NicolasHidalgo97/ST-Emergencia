from Persona import*
from ficha import*
class Paciente(Ficha_Medica):

    #Atributos
    def __init__(self,r,n,a,f,fi):
        self.rut=r
        self.nombre="miguelito"
        self.apellido=a
        self.fono=f
        self.ficha=Ficha_Medica(1,2,3,4,5)
    #Getters Setters
    def getRut(self):
        return self.rut
    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido
    def getFono(self):
        return self.fono
    def getFicha(self):
        return self.ficha

    def setRut(self,rut):
        self.rut=rut
    def setNombre(self,nombre):
        self.nombre=nombre
    def setApellido(self, apellido):
        self.apellido=apellido
    def setFono(self, fono):
        self.fono=fono
    def setFicha(self, ficha):
        self.ficha=ficha
    #Metodos
    def editarDatos(self):
        return True
    def emitirAlerta(self):
        return True
    def obtenerUbicacion(self):
        return True
    def monitorearSignos(self):
        return True
    def obtenerFicha(self):
        return True
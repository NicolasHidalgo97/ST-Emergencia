from Persona import*
from ficha import*
class Paciente(Ficha_Medica):

    #Atributos
    def __init__(self,Rut,Nombre,Apellido,Fono):
        super().__init__("","","",0,0)
        self.ficha=Ficha_Medica("a","a","a",0,0)
        self.rut=Rut
        self.nombre=Nombre
        self.apellido=Apellido
        self.fono=Fono
    def __str__(self):
        return self.nombre +" "+ self.apellido+" /rut: "+str(self.rut)+" /fono: "+str(self.fono)
        
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
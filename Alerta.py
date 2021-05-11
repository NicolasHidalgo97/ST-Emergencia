from Paciente import*
from Profesional import*

class Alerta(Paciente, Profesional):

    #Atributos
    def __init__(self,i,u,p,e,f,h):
        self.ide=i
        self.ubicacion=u
        self.prioridad=p
        self.estado=e
        self.fecha=f
        self.hora=h
        cola=[]
    
    #Getters Setters
    def getIde(self):
        return self.ide
    def getUbicacion(self):
        return self.ubicacion
    def getPrioridad(self):
        return self.prioridad
    def getEstado(self):
        return self.estado
    def getFecha(self):
        return self.fecha
    def getHora(self):
        return self.hora
    
    def setIde(self,ide):
        self.ide= ide
    def setUbicacion(self,ubicacion):
        self.ubicacion=ubicacion
    def setPrioridad(self,prioridad):
        self.prioridad= prioridad
    def setEstadp(self,estado):
        self.estado=estado
    def setFecha(self,fecha):
        self.fecha= fecha
    def setHora(self,hora):
        self.hora=hora

    #Metodos
    def getPaciente(self):
        return True
    def cambiarEstado(self):
        return True


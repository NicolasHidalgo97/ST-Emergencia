from Paciente import*
from Profesional import*

class Alerta(Paciente, Profesional):

    #Atributos
    def __init__(self,id,ubicacion,prioridad,estado,fecha,hora):
        self.id=id
        self.paciente=Paciente(1,2,3,4,5)
        self.profesional=Profesional(1,2,3,4)
        self.ubicacion=ubicacion
        self.prioridad=prioridad
        self.estado=estado
        self.fecha=fecha
        self.hora=hora
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
    def setEstado(self,estado):
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
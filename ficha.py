

class Ficha_Medica():

    #Atributos
    def __init__(self,condicion,observaciones,direccion,
                 latitud,longitud):
        self.condicion=condicion
        self.observaciones=observaciones
        self.direccion=direccion
        self.latitud=latitud
        self.longitud=longitud
    
    def getCondicion(self):
        return self.condicion
    def getObservaciones(self):
        return self.observaciones
    def getDireccion(self):
        return self.direccion
    def getLatitud(self):
        return self.latitud
    def getLongitud(self):
        return self.longitud

    def setCondicion(self,condicion):
        self.condicion=condicion
    def setObservaciones(self,observaciones):
        self.observaciones=observaciones
    def setDireccion(self,direccion):
        self.direccion=direccion
    def setLatitud(self,latitud):
        self.latitud=latitud
    def setLongitud(self,longitud):
        self.longitud=longitud

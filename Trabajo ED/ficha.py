class Ficha_Medica():

    #Atributos
    def __init__(self,Condicion,Observaciones,Direccion,
                 Latitud,Longitud):
        super().__init__()
        self.condicion=Condicion
        self.observaciones=Observaciones
        self.direccion=Direccion
        self.latitud=Latitud
        self.longitud=Longitud
    
    def __str__(self):
        return self.condicion 

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

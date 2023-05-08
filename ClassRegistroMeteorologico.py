class Registro():
    __temp = 0
    __hum = 0
    __presionAtm = 0
    
    def __init__(self, temp, hum, presionAtm):
        self.__temp = temp
        self.__hum = hum
        self.__presionAtm = presionAtm
        
    def __str__(self):
        return str(self.__temp)
    
    def getTemperatura(self):
        return self.__temp
    
    def getHumedad(self):
        return self.__hum
    
    def getPresionAtmosferica(self):
        return self.__presionAtm
    
instancia1 = Registro(10, 20, 30)
instancia2 = Registro(40, 50, 60)
instancia3 = Registro(70, 80, 90)
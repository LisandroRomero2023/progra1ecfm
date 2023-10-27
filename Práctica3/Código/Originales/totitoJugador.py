class Jugador:
    def __init__(self, nombre, caracter):
        self.nombre = nombre
        self.caracter = caracter
        self.advertencias = 0
        
    def getCaracter(self):
        return self.caracter
    
    def getNombre(self):
        return self.nombre
    
    def setAdvertencias(self, val):
        self.advertencias += val
    
    def getAdvertencias(self):
        return self.advertencias

import random

class Tablero():
    def __init__(self):
        self.ganador = 0
        self.tablero = None
        self.posiciones = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.posicionesGanadoras = None

    def imprimirTablero(self):
        self.tablero = '''     1   2   3
   +---+---+---+
1  | {p11:} | {p12:} | {p13:} |
   +---+---+---+
2  | {p21:} | {p22:} | {p23:} |
   +---+---+---+
3  | {p31:} | {p32:} | {p33:} |
   +---+---+---+
'''
        m=self.posiciones
        print(self.tablero.format(p11=m[0][0], p12=m[0][1], p13=m[0][2], p21=m[1][0], p22=m[1][1], p23=m[1][2], p31=m[2][0], p32=m[2][1], p33=m[2][2]))
    
    def setGanador(self, valor):
        self.ganador = valor
    
    def getGanador(self):
        return self.ganador
    
    def getPosiciones(self):
        return self.posiciones
    
    def getPosicionesGanadorasHor(self):
        self.posicionesGanadoras = [ [self.posiciones[0][0], self.posiciones[0][1], self.posiciones[0][2]],
                                       [self.posiciones[1][0], self.posiciones[1][1], self.posiciones[1][2]],
                                       [self.posiciones[2][0], self.posiciones[2][1], self.posiciones[2][2]] ]
        return self.posicionesGanadoras
    
    def getPosicionesGanadorasVer(self):
        self.posicionesGanadoras = [[self.posiciones[0][0], self.posiciones[1][0], self.posiciones[2][0]],
                                    [self.posiciones[0][1], self.posiciones[1][1], self.posiciones[2][1]],
                                    [self.posiciones[0][2], self.posiciones[1][2], self.posiciones[2][2]]]
        return self.posicionesGanadoras
    
    def getPosicionesGanadorasDia(self):
        self.posicionesGanadoras = [[self.posiciones[0][0], self.posiciones[1][1], self.posiciones[2][2]],
                                    [self.posiciones[0][2], self.posiciones[1][1], self.posiciones[2][0]]]
        return self.posicionesGanadoras
    
    
    def setPosicion(self, fila, columna, jugador1, jugador2): ## Funciona bien, cambia el valor de la posición que el jugador seleciona
        while self.posiciones[fila-1][columna-1] != ' ':
            m=input("Elija una posición vacía: ").split(' ')
            jugador1.setAdvertencias(1)
            #print("Tienes", jugador1.getAdvertencias(), "advertencias.")
            if jugador1.getAdvertencias()>2:
                break
            fila, columna = int(m[0]), int(m[1])
        self.posiciones[fila-1][columna-1] = jugador1.getCaracter()
    
    def setPosicionCPU(self, fila, columna, caracter): ## Funciona bine, cambia el valor de la posición que la máquina selecciona
        while self.posiciones[fila][columna] != ' ':
            fila, columna = int(m[0]), int(m[1])
        self.posiciones[fila][columna] = caracter
    
    def posicionesLibres(self):
        lista = []
        for i in range(3):
            for j in range(3):
                if self.posiciones[i][j] == ' ':
                    lista.append([i, j])
        return lista
    
    def posJug(self, carac):
        lista = []
        for i in range(3):
            for j in range(3):
                if self.posiciones[i][j] == carac:
                    lista.append([i,j])
        return lista
    
    def posicionesJugador1(self):
        lista = []
        for i in range(3):
            for j in range(3):
                if self.posiciones[i][j] == 'X':
                    lista.append([i, j])
        return lista
    
    def posicionesJugador2(self):
        lista = []
        for i in range(3):
            for j in range(3):
                if self.posiciones[i][j] == 'O':
                    lista.append([i, j])
        return lista
    
    def jugada(self, jugador1, jugador2):
        temp = input("Introduzca la posición en la que desea jugar en formato fila-columna, separada por un espacio: ").split(' ')
        self.setPosicion(int(temp[0]), int(temp[1]), jugador1, jugador2)
    
    def jugadaRandom(self, jugador):
        ## Realiza una jugada aleatoría válida.
        posiciones = self.posicionesLibres()
        posRandom = random.choice(posiciones)
        self.setPosicionCPU(posRandom[0], posRandom[1], jugador.getCaracter())
    
    def jugadaOptima(self, jugador):
        ## Esta función pretendía elegir el mejor movimiento dada la última posición del tablero.
        posiciones = self.posicionesLibres()
        pos1 = self.posicionesJugador1()
        pos2 = self.posicionesJugador2()
        print(posiciones)
        print(pos1, pos2)



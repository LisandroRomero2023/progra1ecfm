'''
Totito Orientado a Objetos

Este programa se encarga de llevar la interfaz gráfica de los movimientos de un tablero de Totito convencional
independiente de si el jugador juega contra una máquina u otro jugador
'''
#from tkinter import *
#from tkinter import ttk
import random

class Tablero():
    def __init__(self, nombre):
        self.nombre = nombre
        self.isEmpty = None
        self.tablero = '''     1   2   3
   +---+---+---+
1  | {p11:} | {p12:} | {p13:} |
   +---+---+---+
2  | {p21:} | {p22:} | {p23:} |
   +---+---+---+
3  | {p31:} | {p32:} | {p33:} |
   +---+---+---+
'''
        self.posiciones = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def imprimirTablero(self):
        m=self.posiciones
        print(self.tablero.format(p11=m[0][0], p12=m[0][1], p13=m[0][2], p21=m[1][0], p22=m[1][1], p23=m[1][2], p31=m[2][0], p32=m[2][1], p33=m[2][2]))

    def setPosicion(self, fila, columna, caracter):
        while self.posiciones[fila-1][columna-1] != ' ':
            m=input("Elija una posición vacía: ").split(' ')
            fila, columna = int(m[0]), int(m[1])
        self.posiciones[fila-1][columna-1] = caracter
    
    def setPosicionCPU(self, fila, columna, caracter):
        while self.posiciones[fila][columna] != ' ':
            m=input("Elija una posición vacía: ").split(' ')
            fila, columna = int(m[0]), int(m[1])
        self.posiciones[fila][columna] = caracter
    
    def getPosiciones(self):
        return self.posiciones
    
    def posicionesLibres(self):
        lista = []
        for i in range(3):
            for j in range(3):
                if self.posiciones[i][j] == ' ':
                    lista.append([i, j])
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
    
    def jugada(self, jugador):
        temp = input("Introduzca la posición en la que desea jugar en formato fila-columna, separada por un espacio: ").split(' ')
        self.setPosicion(int(temp[0]), int(temp[1]), jugador.getCaracter())
    
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

    def ganador(self):
        pos=self.posiciones
        contador = 0
        M=0
        for i in range(3):
            ## Este primer if verifica las filas.
            if pos[0][i]==pos[1][i] and pos[1][i]==pos[2][i]:
                contador +=1
                M=pos[0][i]
                break
            ## Este segundo if verifica las columnas.
            elif pos[i][0]==pos[i][1] and pos[i][1]==pos[i][2]:
                contador +=1
                M=pos[i][0]
                break
            ## Este tercer if verifica la diagonal principal.
            elif pos[0][0] == pos[1][1] and pos[1][1]==pos[2][2]:
                contador +=1
                M=pos[0][0]
                break
            ## Este cuarto if verifica la diagonal secundaria. 
            elif pos[0][2] == pos[1][1] and pos[1][1]==pos[2][0]:
                contador +=1
                M=pos[2][0]
                break
        if contador == 0:
            return [contador, M]
        else:
            return [contador, M]

class Jugador:
    def __init__(self, nombre, caracter):
        self.nombre = nombre
        self.caracter = caracter
        
    def getCaracter(self):
        return self.caracter
    
    def getNombre(self):
        return self.nombre

def juego1v1(jugador1, jugador2, tablero):
    victoria = 0
    caracter = ''
    tablero.imprimirTablero()
    for i in range(1,5):
        tablero.jugada(jugador1)
        if i > 2:
            temp = tablero.ganador()
            victoria = temp[0]
            caracter = temp[1]
        tablero.imprimirTablero()
        if victoria > 0:
            break
        tablero.jugada(jugador2)
        if i > 2:
            temp = tablero.ganador()
            victoria = temp[0]
            caracter = temp[1]
        tablero.imprimirTablero()
        if victoria > 0:
            break
    
    if victoria == 0:
        tablero.jugada(jugador1)
        tablero.imprimirTablero()
        if i > 2:
            temp = tablero.ganador()
            victoria = temp[0]
            caracter = temp[1]

    if caracter == jugador1.getCaracter():
        return print("El ganador fue", jugador1.getNombre())
    elif caracter == jugador2.getCaracter():
        return print("El ganador fue", jugador2.getNombre())
    else:
        return print("Empate")

def juego1vCPU(jugador1, jugador2, tablero, opcion):
    victoria = 0
    caracter = ''
    tablero.imprimirTablero()
    ## Esta sección del código tenía planeado implementar una estrategia ganadora pero no se completó.
    if opcion == 1:
        for i in range(1,5):
            tablero.jugada(jugador1)
            if i > 2:
                temp = tablero.ganador()
                victoria = temp[0]
                caracter = temp[1]
            tablero.imprimirTablero()
            if victoria > 0:
                break
            tablero.jugadaRandom(jugador2)
            tablero.jugadaOptima(jugador2)
            if i > 2:
                temp = tablero.ganador()
                victoria = temp[0]
                caracter = temp[1]
            tablero.imprimirTablero()
            if victoria > 0:
                break
        if victoria == 0:
            tablero.jugada(jugador1)
            tablero.imprimirTablero()
            if i > 2:
                temp = tablero.ganador()
                victoria = temp[0]
                caracter = temp[1]
        if caracter == jugador1.getCaracter():
            return print("El ganador fue", jugador1.getNombre())
        elif caracter == jugador2.getCaracter():
            return print("El ganador fue", jugador2.getNombre())
        else:
            return print("Empate")
    elif opcion == 2:
        for i in range(1,5):
            tablero.jugada(jugador1)
            if i > 2:
                temp = tablero.ganador()
                victoria = temp[0]
                caracter = temp[1]
            tablero.imprimirTablero()
            if victoria > 0:
                break
            tablero.jugadaRandom(jugador2)
            if i > 2:
                temp = tablero.ganador()
                victoria = temp[0]
                caracter = temp[1]
            tablero.imprimirTablero()
            if victoria > 0:
                break
        if victoria == 0:
            tablero.jugada(jugador1)
            tablero.imprimirTablero()
            if i > 2:
                temp = tablero.ganador()
                victoria = temp[0]
                caracter = temp[1]
        if caracter == jugador1.getCaracter():
            return print("El ganador fue", jugador1.getNombre())
        elif caracter == jugador2.getCaracter():
            return print("El ganador fue", jugador2.getNombre())
        else:
            return print("Empate")
    else:
        return print("Elija una opción válida")



tablero = Tablero("A")

ans1 = int(input("¿Jugarán 1 o 2 jugadores? Responda con el número de jugadores "))

if ans1 == 1:
    nombre1 = input("¿Cuál es el nombre del jugador 1? ")
    jugador1 = Jugador(nombre1, 'X')
    jugador2 = Jugador('CPU', 'O')
    print('''La máquina juega con movimientos aleatorios\n''')
    juego1vCPU(jugador1, jugador2, tablero, 2)
elif ans1 == 2:
    nombre1 = input("¿Cuál es el nombre del jugador 1? ")
    jugador1 = Jugador(nombre1, 'X')
    nombre2 = input("¿Cuál es el nombre del jugador 2? ")
    jugador2 = Jugador(nombre2, 'O')
    juego1v1(jugador1, jugador2, tablero)
else:
    print("Elija una cantidad valida de jugadores.")

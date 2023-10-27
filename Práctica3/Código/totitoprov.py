'''
Totito Orientado a Objetos

Este programa se encarga de llevar la interfaz gráfica de los movimientos de un tablero de Totito convencional
independiente de si el jugador juega contra una máquina u otro jugador
'''
from totitoJugador import Jugador
from totitoTablero import Tablero

def imprimirGanador(tablero, victoria):
    if victoria == False:
        return print("Empate")
    else:
        return print("El ganador es", tablero.getGanador().getNombre())

def juego1v1(jugador1, jugador2, tablero):
    vict = False
    tablero.imprimirTablero()
    for i in range(1,5):
        # Realizamos una jugada
        tablero.jugada(jugador1, jugador2)
        # Verificamos si hay un ganador
        vict = victoria(jugador1, jugador2, tablero)
        # Imprimimos el tablero
        tablero.imprimirTablero()
        if vict != False:
            break
        # Realizamos una jugada
        tablero.jugada(jugador2, jugador1)
        vict = victoria(jugador1, jugador2, tablero)
        tablero.imprimirTablero()
        if vict != 0:
            break
    if vict == False:
        tablero.jugada(jugador1, jugador2)
        tablero.imprimirTablero()
        vict = victoria(jugador1, jugador2, tablero)
    imprimirGanador(tablero, vict)

def juego1vCPU(jugador1, jugador2, tablero):
    vict = False
    tablero.imprimirTablero()
    ## Esta sección del código tenía planeado implementar una estrategia ganadora pero no se completó.
    for i in range(1,5):
        tablero.jugada(jugador1, jugador2)
        tablero.imprimirTablero()
        vict = victoria(jugador1, jugador2, tablero)
        if vict != False:
            break
        tablero.jugadaRandom(jugador2)
        vict = victoria(jugador1, jugador2, tablero)
        tablero.imprimirTablero()
        if vict != False:
            break
    if vict == False:
        tablero.jugada(jugador1, jugador2)
        tablero.imprimirTablero()
        vict = victoria(jugador1, jugador2, tablero)
    imprimirGanador(tablero, vict)



tablero = Tablero()

ans = input("¿Jugarán 1 o 2 jugadores? Responda con el número de jugadores ")

try:
    ans1 = int(ans)
    if ans1 == 1:
        nombre1 = input("¿Cuál es el nombre del jugador 1? ")
        jugador1 = Jugador(nombre1, 'X')
        jugador2 = Jugador('CPU', 'O')
        print('''La máquina juega con movimientos aleatorios\n''')
        juego1vCPU(jugador1, jugador2, tablero)
    elif ans1 == 2:
        nombre1 = input("¿Cuál es el nombre del jugador 1? ")
        jugador1 = Jugador(nombre1, 'X')
        nombre2 = input("¿Cuál es el nombre del jugador 2? ")
        jugador2 = Jugador(nombre2, 'O')
        juego1v1(jugador1, jugador2, tablero)
    else:
        print("Elija una cantidad valida de jugadores.")
except ValueError:
    print("Ingrese una cantidad válida de jugadores")

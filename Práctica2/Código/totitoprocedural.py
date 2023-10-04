'''
Totito procedural

Este programa se encarga de llevar el registro de movimientos en un tablero de Totito convencional jugando entre una
persona y una máquina.
'''
import random

def ganador(list):
    pos=list
    contador = 0
    M=0
    for i in range(3):
        if pos[3*i]==pos[3*i+1] and pos[3*i+1]==pos[3*i+2]:
            contador +=1
            M=pos[3*i]
            break
        elif pos[i]==pos[i+3] and pos[i+3]==pos[i+6]:
            contador +=1
            M=pos[i]
            break
        elif pos[0] == pos[4] and pos[4]==pos[8]:
            contador +=1
            M=pos[0]
            break
        elif pos[6] == pos[4] and pos[4]==pos[2]:
            contador +=1
            M=pos[6]
            break
    if contador == 0:
        return [contador, M]
    else:
        return [contador, M]


jugador1='X'
jugador2='O'

pos=[[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

tablero='''+-----+-----+-----+
|     |     |     |
|  {p11:}  |  {p12:}  |  {p13:}  |
|     |     |     |
+-----+-----+-----+
|     |     |     |
|  {p21:}  |  {p22:}  |  {p23:}  |
|     |     |     |
+-----+-----+-----+
|     |     |     |
|  {p31:}  |  {p32:}  |  {p33:}  |
|     |     |     |
+-----+-----+-----+
'''
contador=0
print('''El primer jugador usa el caracter X y el segundo, el caracter O.
Usted es el primer jugador\n''')
print(tablero.format(p11=pos[0][0], p12=pos[0][1], p13=pos[0][2], p21=pos[1][0], p22=pos[1][1], p23=pos[1][2], p31=pos[2][0], p32=pos[2][1], p33=pos[2][2]))
victoria = 0
for i in range(1,5):
    elec1, elec2=input("Escoja una posición libre fila columna separadas por un espacio: ").split(' ')
    while ' ' != pos[elec1-1][elec2-1]:
        elec=int(input("Escoja una posición libre: "))
    pos[elec1-1][elec2-1]=jugador1
    print(tablero.format(p11=pos[0][0], p12=pos[0][1], p13=pos[0][2], p21=pos[1][0], p22=pos[1][1], p23=pos[1][2], p31=pos[2][0], p32=pos[2][1], p33=pos[2][2]))
    if i >2:
        temp = ganador(pos)
        victoria, jugador = temp[0], temp[1]
    if victoria != 0:
        if jugador1 != temp[1]:
            print("Ganó el jugador 2.")
            break
        else:
            print("Ganó el jugador 1.")
            break
    mov2 = random.randrange(0, 9, 1)
    while mov2+1 != pos[mov2]:
        mov2 = random.randrange(0, 9, 1)
    pos[mov2] = jugador2
    print(tablero.format(p1=pos[0], p2=pos[1], p3=pos[2], p4=pos[3], p5=pos[4], p6=pos[5], p7=pos[6], p8=pos[7], p9=pos[8]))
    if i >2:
        temp = ganador(pos)
        victoria, jugador = temp[0], temp[1]
    if victoria != 0:
        if jugador1 != temp[1]:
            print("Ganó el jugador 2.")
            break
        else:
            print("Ganó el jugador 1.")
            break
if victoria == 0:
    elec=int(input("Escoja una posición libre: "))
    while elec != pos[elec-1]:
        elec=int(input("Escoja una posición libre: "))
    pos[elec-1]=jugador1
    print(tablero.format(p1=pos[0], p2=pos[1], p3=pos[2], p4=pos[3], p5=pos[4], p6=pos[5], p7=pos[6], p8=pos[7], p9=pos[8]))
    if i >2:
        temp = ganador(pos)
        victoria, jugador = temp[0], temp[1]
    if victoria != 0:
        if jugador1 != temp[1]:
            print("Ganó el jugador 2.")
        else:
            print("Ganó el jugador 1.")
if victoria==0:
    print("Fue un empate")

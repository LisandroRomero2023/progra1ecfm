'''
¿Cuántas rutas desde la esquina superior izquierda hacia la esquina inferior derecha de un tablero cuadriculado hay, si
solo puede moverse de la intersección actual hacia la intersección en la derecha o abajo de la intersección actual y el
tamaño del tablero de 20x20?

Este programa calcula cuántas de estas rutas hay.
'''

from math import comb

print(comb(40,20))

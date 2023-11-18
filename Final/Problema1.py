'''
Examen Final, Programación Matemática 1
Problema 1
@autor: Lisandro Romero
@versión: 0.1
@fecha: 16 de Noviembre de 2023
'''
## Notemos inicialmente que al tener una 

from math import factorial, ceil
import time

def pilasCompletas(numero):
    n=numero
    contador= 0
    mitad = ceil(numero/2)+1
    for i in range (mitad):
        for j in range(numero-2*i+1):
            parte = factorial(n) // (factorial(i)*factorial(i)*factorial(j)*factorial(n-2*i-j))
            contador += parte
    return contador

ini = time.time()

valor = pilasCompletas(10) -2
modulado = valor % 989898989

fin = time.time()

print("El valor módulo 989898989 es", modulado, "El tiempo requerido para calcularlo es:", fin-ini, sep='\n')

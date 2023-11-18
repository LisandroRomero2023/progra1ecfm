'''
Examen Final, Programación Matemática 1
Problema 2
@autor: Lisandro Romero
@versión: 0.1
@fecha: 16 de Noviembre de 2023
'''

from math import ceil
from math import sqrt
import time


def esAbundante(numero): ## Esto verifica si el número es abundante.
    n=numero
    a=[1]
    for i in range(2, ceil(sqrt(n)+1)):
        if n % i == 0:
            num = n//i
            if i != num:
                a.append(i)
                a.append(num)
            else:
                a.append(i)
    suma=0
    for i in a:
        suma+=i
        
    if numero == 1:
        return False
    elif numero ==2:
        return False
    elif suma > numero:
        return True
    else:
        return False

ini = time.time() ## Inicio de la medición de tiempo

listaAbun=[] ## Se inicia la lista de números abundantes

for i in range(12,28123): ## Verificamos cuáles números entre 12 y 28123 son abundantes.
    if esAbundante(i) == True:
        listaAbun.append(i)

lista2Abun=[] ##  Acá iniciamos la lista con los números que se escriben como suma de dos abundantes.
for i in range(1,28123): ## Verificamos
    for j in range(len(listaAbun)):
        if i-j>0:
            if i-j in listaAbun:
                lista2Abun.append(i)
            break

listaNoAbun=[] ## Iniciamos la lista de los que no se pueden escribir como suma de dos abundantes.        
for i in range(24):
    listaNoAbun.append(i)
for i in range(24,28123): ## Verificamos
    if i not in lista2Abun:
        listaNoAbun.append(i)

noAbunSum=0 ## Creamos la suma de los no abundantes.
for i in listaNoAbun:
    noAbunSum+=i


fin=time.time()

print("La suma de los números que no pueden ser escritos como la suma de dos números abundates es:",noAbunSum, "Encontrar tal número tomó el siguiente tiempo en segundos:",fin-ini, sep="\n")

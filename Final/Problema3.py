'''
Examen Final, Programación Matemática 1
Problema 3
@autor: Lisandro Romero
@versión: 0.1
@fecha: 16 de Noviembre de 2023
'''
import time

ini = time.time()

T = int(input(""))

for i in range(T):
    ent = input().split(' ')
    a, b, c, d = int(ent[0]),  int(ent(1]), int(ent[2]), int(ent[3])
    if a == b:
        if c==d:
            fin=time.time()
            print("YES")
    elif a == c:
        if b==d:
            fin=time.time()
            print("YES")
    elif a == d:
        if b==c:
            fin=time.time()
            print("YES")
    else:
        fin=time.time()
        print("NO")
    
    

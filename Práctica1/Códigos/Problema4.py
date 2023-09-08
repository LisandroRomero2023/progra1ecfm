'''
Posible GCD

'''
from math import sqrt, floor

def distgcd(numa: int, numb: int):
    m=numa-numb
    divisores = 0
    for i in range(1,floor(sqrt(m))+1):
            if m % i == 0:
                if m // i != i:
                    divisores += 2
                else:
                    divisores += 1
    return(divisores)
## Checar si todos los divisores de A-B son GCD.
## Esto en efecto es cierto pues gcd(A+X, B+X) = gcd(A-B, B+X)
## De donde, si l|(A-B) entonces l|(B+X) para algún X entero.
## En módulos esto es B = k [l], entonces X = -k [l].

T = int(input())

for i in range(T):
    num = input().split(' ')
    A, B = int(num[0]), int(num[1])
    if A > B:
        print(distgcd(A,B))
    elif A == B:
        print(0)
    else:
        print(distgcd(B,A))

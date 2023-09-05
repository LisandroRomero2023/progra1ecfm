'''
Posible GCD

'''

from math import gcd

def distgcd(numa: int, numb: int):
    r = []
    for i in range(numa-numb):
        z=0
        l=gcd(numa-numb, numb+i)
        for j in range(len(r)):
            if l == r[j]:
                z = z+1
                break
        if z == 0:
            r.append(l)
    return len(r)

T = int(input())

for i in range(T):
    num = input().split(' ')
    A, B = int(num[0]), int(num[1])
    if A > B:
        print(distgcd(A,B))
    else:
        print(distgcd(B,A))

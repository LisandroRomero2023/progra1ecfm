'''
Logical operators & conditional statements

Problema de CodeChef que verifica si un número N es divisible por los números A y B, diciendo por cuáles es divisible
y por cuales no es divisible
'''

t = int(input())
for i in range(t):
    N, A, B = map(int, input().split())
    if N%A == 0 and N%B == 0:
        print('N is divisible by A and B')
    elif N%B != 0:
        print('N is divisible by only A')
    elif N%A != 0:
        print('N is divisible by only B')
    # The last statement could have been an 'else' statement
    # elif condition used to show usage of 'and' statement
    elif N%A != 0 and N%B != 0:
        print('N is divisible by neither A nor B')

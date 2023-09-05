'''
Chef Diet

Problema de ChefCode.
'''

T = int(input())

for i in range(T):
    val = input().split(' ')
    N, K = int(val[0]), int(val[1])
    cases = input().split(' ')
    b=0
    h=0
    for j in range(N):
        m = int(cases[j]) + h
        if m >= K:
            h= m - K
        else:
            l=j+1
            b = b+1
            print("NO ", l)
            break
    if b==0:
        print("YES")

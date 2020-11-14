import math

T = int(input())
for i in range(0, T):
    N = int(input())
    p = 2
    i = N
    lst = []
    while (p <= (math.floor(math.sqrt(N)))):
        if (i % p == 0):
            i = i // p
            lst.append(i)
        else:
            p = p + 1
    if i != 1:
        print(i)
    else:
        print(lst[-2])
        

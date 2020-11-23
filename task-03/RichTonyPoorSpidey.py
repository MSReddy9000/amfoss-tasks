def multiply(list):
    prevmult = 1
    for x in list:
        prevmult = prevmult * x
    return prevmult

t = int(input())
nk = []
money = []
tw = []
for x in range(0, t):
    nk = (list(map(int, input().split())))
    money = (list(map(int, input().split())))
    money.sort()
    Identifier = 1
    while Identifier == 1:
        if money[-1] > nk[1]:
            money[-1] = money[-1] - nk[-1]
            tw.append(multiply(money))
            Identifier = 0
        else:
            money.pop(-1)
            money.sort()
            Identifier = 1
for x in tw:
    print(x)

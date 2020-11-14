import math
def f(x,b,c):
    return ((x*x + b*x + c)/math.sin(x))
t = int(input())
ans = []
for i in range(0, t):
    domainStart = 0.000001
    domainEnd = 1.570796
    iterations = 1
    bc = list(map(float, input().split()))
    b = bc[0]
    c = bc[1]
    while iterations < 150:
        x = (domainStart + domainEnd)/2
        if (f(x,b,c) > f(x-0.000001,b,c) and f(x,b,c) < f(x+0.000001,b,c)):
            domainEnd = x
        elif (f(x,b,c) < f(x-0.000001,b,c) and f(x,b,c) > f(x+0.000001,b,c)):
            domainStart = x
        else:
            k = ((x*x + b*x + c)/math.sin(x))
            k = round(k, 10)
            ans.append(k)
            break
        iterations = iterations + 1
for x in ans:
    print(x)

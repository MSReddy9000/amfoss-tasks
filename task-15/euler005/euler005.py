import math
from fractions import Fraction

def multiply(someList) :
    result = 1
    for m in someList:
         result = result * m 
    return result

T = int(input())
number_list = []
for x in range(0, T):
    k = int(input())
    number_list.append(k)
k = max(number_list)
nl = []
pnl = []
for x in range(2, k+1):
    nl.append(x)
#Sieving Prime Numbers from nl into pnl
for x in nl:
    truthTable = []
    for y in range(2, x):
        if x % y == 0:
            truthTable.append(False)
        else:
            truthTable.append(True)
    if all(truthTable) == True:
        pnl.append(x)
        nl.remove(x)
    else:
        pass
nl.remove(3)
pnl.insert(1, 3)
answers = []
for x in number_list:
    nbuffer = []
    pnbuffer = []
    for y in nl:
        if y <= x:
            nbuffer.append(y)
        else:
            break
    for y in pnl:
        if y <= x:
            pnbuffer.append(y)
        else:
            break
    ans = multiply(pnbuffer)
    for y in nbuffer:
        a = Fraction(ans, y)
        ans = ans*(a.denominator)
    answers.append(ans)
for x in answers:
    print(x)
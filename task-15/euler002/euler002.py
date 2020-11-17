T = int(input())
N = []
for i in range(0,T):
    N.append(int(input()))
#Generating the Fibonnaci Sequence
Fibonnaci = [1,2]
buff = [1,2]
while buff[-1] < max(N):
    temp = buff[0] + buff[1]
    Fibonnaci.append(temp)
    buff.append(temp)
    buff.pop(0)
for n in N:
    sum = 0
    for x in Fibonnaci:
        if x < n:
            if x % 2 == 0:
                sum = sum + x
    print(sum)

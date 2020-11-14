t = int(input())
for i in range(0,t):
    N = int(input())
    n3 = (N-1)//3
    n5 = (N-1)//5
    n15 = (N-1)//15
    sum3 = (n3*(n3 + 1))//2
    sum5 = (n5*(n5 + 1))//2
    sum15 = (n15*(n15 + 1))//2
    print(3*sum3 + 5*sum5 - 15*sum15)

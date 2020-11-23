n,m = map(int, input().split())
array = list(map(int, input().split()))
identifier = 1
for x in range(0, n-1):
    for y in range(x+1, n):
        if (array[x] + array[y] == m):
            identifier = 1
            print(True)
            break
        else:
            identifier = 0
    if identifier == 1:
        break
if identifier == 0:
    print(False)

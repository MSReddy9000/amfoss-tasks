n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
x = 0
y = n-1
identifier = 0
while x < y:
    if arr[x] + arr[y] == m:
        print(True)
        identifier = 1
        break
    elif arr[x] + arr[y] < m:
        x+=1
    else:
        y-=1
if identifier == 0:
    print(False)

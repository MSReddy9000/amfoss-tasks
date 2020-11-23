t = int(input())
for x in range(0,t):
    n,k = map(str, input().split())
    n = list(map(int, n))
    k = int(k)
    if len(n) <= k:
        print(-1)
    else:
        mns = []
        no_of_nsums = len(n) - k
        x = 0
        identifier = 0
        while x < no_of_nsums:
            mnsum = abs(n[x]-n[x+k])
            if identifier == 0:
                mns.append(mnsum)
            elif mnsum < mns[0]:
                mns.append(mnsum)
                mns.pop(0)
            x = x + 1
            identifier = 1
        print(mns[0])

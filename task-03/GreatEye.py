# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for x in range(0, t):
    k = int(input())
    sentence = list(map(str, input().split()))
    asc2 = 0
    if k <= (len(sentence)-1):
        for y in sentence[k]:
            asc2 = asc2 + ord(y)
        print(asc2)
    else:
        print("-1")

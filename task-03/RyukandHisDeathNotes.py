types = int(input())
required = list(map(int, input().split()))
available = list(map(int, input().split()))
truthTable = []
noteNumber = 0
identifier = 1
while identifier == 1:
    for x in range(0, types):
        available[x] = (available[x] - required[x])
    for x in available:
        if x >= 0:
            pass
        else:
            identifier = 0
            break
    if identifier == 0:
        break
    noteNumber = noteNumber + 1
    identifier = 1
print(noteNumber)

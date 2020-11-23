strlen = int(input())
string = str(input())
zeroArray = []
oneArray = []
for x in string:
    if x == '1':
        oneArray.append(x)
    else:
        zeroArray.append(x)
if len(oneArray) == len(zeroArray):
    print(2)
else:
    print(1)


t = int(input())
array = []
for x in range(0, t):
    array.append(int(input()))
#Generating the Incredible Series
incredibleSeries = [1,2,3]
bufferSeries = [1,2,3]
i = len(incredibleSeries)
while i < 1000000:
    temp = ((sum(bufferSeries))%(10**9 + 7))
    bufferSeries.append(temp)
    incredibleSeries.append(temp)
    bufferSeries.pop(0)
    i = len(incredibleSeries)
for x in array:
    temp = str(incredibleSeries[x-1])
    rtemp = temp[::-1]
    print(rtemp.lstrip("0"))

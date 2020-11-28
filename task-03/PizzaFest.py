from collections import OrderedDict

def deldup(a):
    return list(OrderedDict.fromkeys(a))

n,k = map(int, input().split())
house_owners = list(map(int, input().split()))
orders = list(map(int, input().split()))
owners_list = []
ids = deldup(house_owners)
for x in ids:
    owners_list.append([index+1 for index, value in enumerate(house_owners) if value == x])
p = dict(zip(ids, owners_list))
answers = []
for x in orders:
    a = p.get(x)
    if a != []:
        answers.append(a[-1])
        a.pop(-1)
    else:
        answers.append(-1)
print(*answers)

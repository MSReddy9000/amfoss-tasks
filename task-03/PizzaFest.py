def del_dup(x):
  return list(dict.fromkeys(x))
n,k = map(int, input().split())
#NOTE: these numbers n and k are just the lengths of the next 2 lines and are pretty much useless input
owners = list(map(int, input().split()))
orders = list(map(int, input().split()))
ids = del_dup(owners)
addresses = []
for x in ids:
  buffer = []
  for y in range(0,len(owners)):
    if x == owners[y]:
      buffer.append(y+1)
  buffer.sort(reverse=True)
  addresses.append(buffer)
proper_dict = dict(zip(ids, addresses))
answers = []
for x in orders:
  if len(proper_dict[x]) == 0:
    answers.append(-1)
  else:
    answers.append((proper_dict[x])[0])
    (proper_dict[x]).pop(0)
print(*answers)

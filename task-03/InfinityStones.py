t = int(input())
for x in range(0, t):
    n,m,k = map(int, input().split())
    present_stones = list(map(int, input().split()))
    max_capacity = list(map(int, input().split()))
    if m <= k:
        print("YES")
    else:
        total_stones = sum(present_stones)
        max_protected_boxes = []
        max_capacity.sort(reverse = True)
        for y in range(0,k):
            max_protected_boxes.append(max_capacity[y])
        total_capacity = sum(max_protected_boxes)
        if total_stones <= total_capacity:
            print("YES")
        else:
            print("NO")

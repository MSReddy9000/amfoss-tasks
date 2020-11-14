k = 101101
palindrome_list = []
all_3_digit_numbers = []
for x in range(100, 1000):
    all_3_digit_numbers.append(x)
while k < 1000000:
    palindrome_buffer = []
    temp = str(k)
    if temp == temp[::-1]:
        for x in all_3_digit_numbers:
            if k % x == 0:
                h = k // x
                h = str(h)
                if len(h) == 3:
                    palindrome_buffer.append(k)
                else:
                    pass
            else:
                pass
        if len(palindrome_buffer) != 0:
            palindrome_list.append(max(palindrome_buffer))
    k = k+1
T = int(input())
for x in range(0, T):
    ansbuffer = []
    n = int(input())
    for y in palindrome_list:
        if y < n:
            ansbuffer.append(y)
    print(max(ansbuffer))
num = 1000
i = 1
j = 1
p = 1
while p <= num:
    print(i)
    if p % 20 == 0:
        print(i/j)
    temp = i + j
    i = j
    j = temp
    p = p + 1
import time
fib = input("Hur många Fibonacci tal ska skrivas ut? ")
num = int(fib)
i = 1
j = 1
p = 1
while p <= num:
    time.sleep(0.25)
    print(i)
    print(i/j)
    temp = i + j
    i = j
    j = temp
    p = p + 1
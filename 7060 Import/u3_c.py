import time
i = 1
j = 1
p = 1
n = 10
while p <= n:
    time.sleep(0.25)
    print(i)
    temp = i + j
    i = j
    j = temp
    p = p + 1

fib = input("Hur många Fibonacci tal ska skrivas ut? ")
num = int(fib)
num = num + n

while p <= num:
    time.sleep(0.25)
    print(i)
    temp = i + j
    i = j
    j = temp
    p = p + 1
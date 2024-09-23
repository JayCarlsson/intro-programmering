hel = input("Hur många heltal vill du ha? ")
tal = int(hel)
minsta_tal = input("Vilket är det minsta talet i serien? ")
mintal = int(minsta_tal)

i = mintal
while i < mintal + tal:
    print(i)
    i = i + 1
    
print("klart")
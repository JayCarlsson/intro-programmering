guess = int(input("Gissa vilket tal jag tänker på mellan 1 och 100: "))
num = 4

while guess != num:
    guess = int(input("Du gissade fel, gissa igen! "))

print("Du gissade rätt, jag tänkte på 4")
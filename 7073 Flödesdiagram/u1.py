guess = int(input("Gissa vilket tal jag tänker på mellan 1-100! "))

while guess != 42:
    print("Du gissade fel!")
    print(" ")
    guess = int(input("Gissa vilket tal jag tänker på mellan 1-100! "))
    if guess == 42:
        print("Du gissade rätt!")
print("Klart!")
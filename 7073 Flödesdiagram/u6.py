tal = int(input("Gissa vilket tal jag tänker på mellan 1 och 100! "))
ag = 1
while tal != 42:
    if tal > 42:
        print("För stort!")
    else:
        print("För litet!")
    tal = int(input("Gissa igen! "))
    ag += 1

if tal == 42:
    print("Du gissade rätt, det tog", ag, "gissningar!")
else:
    print("Något gick fel!")
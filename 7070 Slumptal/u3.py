import random
import time

Sten = 1
Sax = 2
Påse = 3
i = 0

while i < 10:
    dval = random.randint(1,3)
    sval = input("Sten, Sax eller Påse? ")

    if sval == "sten" or sval == "Sten":
        if dval == 1:
            print("Båda valde sten!")
        elif dval == 2:
            print("Sax, du vann!")
        else:
            print("Påse, du förlora!")
    elif sval == "sax" or sval == "Sax":
        if dval == 2:
            print("Båda valde sax!")
        elif dval == 3:
            print("Påse, du vann!")
        else:
            print("Sten, du förlora!")
    elif sval == "påse" or sval == "Påse":
        if dval == 3:
            print("Båda valde påse!")
        elif dval == 1:
            print("Sten, du vann!")
        else:
            print("Sax, du förlora!")

    i = i + 1
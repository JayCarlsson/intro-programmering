import random

sspdict = dict({"Sten": 1, "Sax" : 2, "Påse" : 3})

i = 0

while i < 10:
    print(sspdict)
    pv = int(input("Välj siffran för Sten, Sax eller Påse"))

    dv, dvt = random.choice(list(sspdict.items()))

    if pv in sspdict:
        print(f"Matched key: {pv}, Value: {sspdict[pv]}")

    i += 1
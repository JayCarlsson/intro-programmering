import random

sspdict = dict({
    1: "Sten",
    2: "Sax",
    3: "Påse"
})

resdict = dict({
    1: "Du förlora",
    -2: "Du förlora",
    2: "Du vann",
    -1: "Du vann",
    0: "Lika"
})

vinst = 0
förlust = 0

for i in range(10):
    print(sspdict)
    pv = int(input("Välj Sten, Sax eller Påse "))

    rk, rv = random.choice(list(sspdict.items()))

    if pv in sspdict:
        print(f"Spelaren valde {sspdict[pv]}")

    if rk in sspdict:
        print(f"Datorn valde {sspdict[rk]}")

    svar = pv - rk

    if svar in resdict:
        print(f"{resdict[svar]}")

    if resdict[svar] == "Du förlora":
        förlust += 1
    elif resdict[svar] == "Du vann":
        vinst += 1

    print("Förlust: ", förlust, "Vinst ", vinst)

print("Klar")
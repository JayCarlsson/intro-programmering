import random
import time

print("Välkommen till Casino 7!")
print("")
print("Kvällens spel är Lucky Seven.")
print("")
print("Tre tal slumpas. Möjliga slumptal är 0, 1, 2,... och  9. Talen visas. Om alla talen är lika blir det vinst. Tre sjuor ger dubbel vinst.")
print("")
print("Varje spel kostar 2 krona.")
print("")
print("Vinstplan:")
print("Tre sjuor: 100kr")
print("Tre lika: 50kr")
print("Två lika: 5kr")
print("En sjua: 2kr")

spela = input("Vill du spela Lucky Seven? j/n ")

cash = 100

# För simulering
#   ---------
#spel = 0
tvålika = 0
trelika = 0
förlust = 0
sjuvinst = 0
lucky = 0

while spela == "j":
    n1 = random.randint(1,9)
    n2 = random.randint(1,9)
    n3 = random.randint(1,9)

    if cash < 1:
        print("Du har inga pengar kvar, tack för att du spelade!")

    cash = cash - 2
    print("Tärningarna kastas..")
    time.sleep(0.5)
    print("Det blir...")
    time.sleep(0.5)
    print(n1, n2, n3)

    if n1 == n2 == n3 != 7:
        print("Tre lika, 50kr vinst")
        trelika = trelika + 1
        cash = cash + 50
    elif n1 == n2 != n3 or n1 == n3 != n2 or n2 == n3 != n1:
        print("Två lika, 5kr vinst")
        tvålika = tvålika + 1
        cash = cash + 5
    elif n1 == 7 and n1 != n2 and n1 != n3:
        print("Du vann sjuvinst, 2kr vinst")
        sjuvinst = sjuvinst + 1
        cash = cash + 2
    elif n3 == 7 and n1 != n2 and n1 != n3:
        print("Du vann sjuvinst, 2kr vinst")
        sjuvinst = sjuvinst + 1
        cash = cash + 2
    elif n2 == 7 and n1 != n2 and n1 != n3:
        print("Du vann sjuvinst, 2kr vinst")
        sjuvinst = sjuvinst + 1
        cash = cash + 2
    elif n1 == n2 == n3 == 7:
        print("Lucky Seven, 100kr vinst")
        lucky = lucky + 1
        cash = cash + 100
    else:
        print("Du förlora, -2kr")
        förlust = förlust + 1
    
    print(cash, "kr kvar")
    spela = input("Vill du spela igen? j/n ")
    
    if spela == "n":
        time.sleep(1)
        print("Tack för att du spelade, hejdå!")
    
    
    # För simulering
    #    -------
    #spel = spel + 1

#print(trelika, "trelika", tvålika, "tvålika", sjuvinst, "sjuvinst", förlust, "förlust", lucky, "lucky")
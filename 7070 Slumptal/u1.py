import random
i = 0

text = input("Vill du spela ett spel? j/n ")
print("Två lika tärningar ger vinst!")

while text == "j":
    rnum = random.randint(1, 6)
    rnum2 = random.randint(1, 6)
    i = i + 1
    if i == 8:
        print("Tack för att du spelade en stund!")
        break
    print(rnum, rnum2)
    if rnum == rnum2:
        print("Du vann, två lika!")
        text = input("Vill du spela igen? j/n ")
    elif rnum != rnum2:
        print("Förlust!")
        text = input("Vill du spela igen? j/n ")

if text == "n":
        print("Okej, hejdå")
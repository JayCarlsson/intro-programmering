import random
import time
i = 0

print("Välkommen att kasta tärning!")
print("Ett spel kostar 2 krona")
print(" ")
print("Vinstplan:")
print("Två lika - 5 kr")
print("Dubbla sexor - 4 kr")
print("Stege - 4 kr")
print(" ")

stege = 0
sexa = 0
lika = 0
förlust = 0

text = input("Vill du spela ett spel? j/n ")
f = 0

if text == "j":
    cash = int(input("Du behöver sätta in pengar för att spela, hur mycket vill du sätta in? "))

while text == "j":
    n1 = random.randint(1, 6)
    n2 = random.randint(1, 6)
    if cash < 2:
        cash_input = input("Du har för lite pengar kvar,", cash, "vill du sätta in mer? j/n ")
        if cash_input == "j":
            cash = int(input("Hur mycket vill du sätta in? "))
        else:
            print("Du kan inte spela utan pengar!")
            break
    print("Tärningen kastas..")
    time.sleep(0.5)
    print("Det blir...")
    time.sleep(0.5)
    print(n1, n2)
    time.sleep(0.5)
    cash = cash - 2

    if n1 == n2 and n1 != 6:
        print("Du vann, två lika!")
        cash = cash + 5
        print(cash, "kr kvar")
    elif n1 == 6 and n2 == 6:
        print("Du vann sex-vinst, två sexor")
        cash = cash + 4
        print(cash, "kr kvar")
    elif n2 == n1 + 1 or n1 == n2 + 1:
        print("Du vann, stege")
        cash = cash + 4
        print(cash, "kr kvar")
    else:
        print("Förlust!")
        print(cash, "kr kvar")
    text = input("Vill du spela igen? j/n ")
    print(" ")
    if text == "n":
        print("Okej, hejdå")

# Simulation 1, 100 000 spel
# 27885 stege, 2767 sexa, 13748 lika, 55600 förlust
# 100 kr till -8552 kr

# Simulation 2 100 000 spel
# 27711 stege, 2765 sexa, 13840 lika, 55684 förlust
# 100 kr till -8796 kr

# Simulation 3 100 000 spel
# 27709 stege, 2775 sexa, 13993 lika, 55523 förlust
# 100kr till -7999 kr
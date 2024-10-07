import random

i = 0

while i < 10:

    player = int(input("1. för sten, 2. sax, 3. för påse"))
    computer = random.randint(1,3)
    diff = player - computer
    
    if computer == 1:
        print("Sten")
    elif computer == 2:
        print("Sax")
    else:
        print("Påse")

    if diff == -2:
        print("Du förlora")
    elif diff == -1:
        print("Du vann")
    elif diff == 0:
        print("Lika")
    elif diff == 1:
        print("Du förlora")
    elif diff == 2:
        print("Du vann")

    # -2 förlust
    # -1 vinst
    # 0 lika
    # 1 förlust
    # 2 vinst

    i = i + 1
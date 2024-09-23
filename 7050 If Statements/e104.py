
import random

spela_igen = "j"
while spela_igen == "j":
    rnum = random.randint(1, 6)
    rnum2 = random.randint(1, 6)
    rnum3 = random.randint(1, 6)
    if rnum == rnum2 and rnum == rnum3:
        print("Du vann, triss i", rnum)
    elif rnum == 6 and rnum2 == 6 and rnum3 == 6:
        print("Du vann stort! Triss i", rnum)
    elif rnum + 1 == rnum2 and rnum2 + 1 == rnum3:
        print("Stegvinst! Du fick stege", rnum, rnum2, rnum3)
    elif rnum + 1 == rnum3 and rnum3 + 1 == rnum2:
        print("Stegvinst! Du fick stege", rnum, rnum3, rnum2)
    elif rnum2 + 1 == rnum and rnum + 1 == rnum3:
        print("Stegvinst! Du fick stege", rnum2, rnum, rnum3)
    elif rnum2 + 1 == rnum3 and rnum3 + 1 == rnum:
        print("Stegvinst! Du fick stege", rnum2, rnum3, rnum)
    elif rnum3 + 1 == rnum2 and rnum2 + 1 == rnum:
        print("Stegvinst! Du fick stege", rnum3, rnum2, rnum)
    elif rnum3 + 1 == rnum and rnum + 1 == rnum2:
        print("Stegvinst! Du fick stege", rnum3, rnum, rnum2)
    else:
        print("Du förlora, du fick", rnum, rnum2, rnum3)

        spela_igen = input("Vill du spela igen? j/n: ")
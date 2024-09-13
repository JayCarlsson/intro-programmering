import random
rnum = random.randint(1, 6)
rnum2 = random.randint(1, 6)
tnum = rnum + rnum2

if tnum % 2 == 0 and tnum != 6:
    print("Du vann, det blev", tnum)
elif tnum == 6:
    print("Du vann stort! Det blev", tnum)
else:
    print("Du förlora, det blev", tnum)
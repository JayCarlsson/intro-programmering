import random
rnum = random.randint(1, 6)

exec = input("Säg till när jag ska rulla tärningen: ")

if exec == "Nu" or "nu":
    print(rnum)
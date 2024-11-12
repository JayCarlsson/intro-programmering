import random

tärningar = []

for i in range(20):
    tärningar.append(random.randint(1,4))

print(tärningar)
print("min", min(tärningar))
print("summa", sum(tärningar))
print("antal fyror", tärningar.count(4))

antal_ettor = 0

for tärning in tärningar:
    if tärning == 1:
        antal_ettor += 1

print("antal ettor", antal_ettor)


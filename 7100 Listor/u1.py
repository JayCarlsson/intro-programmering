import random

resultat = []

for i in range(10):
    resultat.append(random.randint(1,6))

antal = [0, 0, 0, 0, 0, 0, 0]
 # element with index 0 not used
for tal in resultat:
    antal[tal] += 1
max_index = antal.index(max(antal))
# vilken är vanligast
print("Antal:", antal[1:len(antal)])
print(max(antal))
print("Resultat:", resultat)
print("Sorterat:", sorted(resultat))
print("Summan:", sum(resultat))
print("Minsta talet:", resultat[1])
print("Största talet:", (resultat[9]))
print("Antal sexor:", resultat.count(6))
print("Vanligaste valör", max_index)
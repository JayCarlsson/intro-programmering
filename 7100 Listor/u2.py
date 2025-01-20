tal_lista = [*range(1000, 1, -1)]
primtal = []

while tal_lista != []:
    last = tal_lista.pop()
    primtal.append(last)

    i = len(tal_lista) - 1
    while i > -1:
        if tal_lista[i]%primtal[-1]==0:
            tal_lista.pop(i)
        i -= 1
'''
print(tal_lista)
print(primtal)
'''


for tal in primtal:
    q = 2537%tal == 0

print(q)
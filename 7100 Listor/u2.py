tal_lista = [*range(100, 1, -1)]
primtal = []
print("test")
while tal_lista != []:
    last = tal_lista.pop()
    primtal.append(last)

    i = len(tal_lista) - 1
    while i > -1:
        if tal_lista[i]%primtal[-1]==0:
            tal_lista.pop(i)
        i -= 1

print(tal_lista)
print(primtal)
import random

primes = [61, 53]
p = primes[0]
q = primes[1]

# Temporary for testing key creation.

#Disabled until key creation works, will choose 2 random primes later.
'''
tal_lista = [*range(1000, 100, -1)]
print("test")
while tal_lista != []:
    last = tal_lista.pop()
    primes.append(last)

    i = len(tal_lista) - 1
    while i > -1:
        if tal_lista[i]%primes[-1]==0:
            tal_lista.pop(i)
        i -= 1

print(tal_lista)
print(primes)
'''

n = p * q

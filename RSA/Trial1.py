import random

primes = [83, 11]
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
e = 3
phi_n = 820
d = (2*phi_n+1)/3

if 3 * d == (2*phi_n)+1:
    print("Correct private key")
else:
    print("False")
message = 4
crypt_mes = (message**e)%n
rm = message%n

print(phi_n)
print(n)
print(e)
print(d)
print(message)
print("Encrypted message", c)
if message%n == :
    print("Depcryption complete", rm)

'''
k*d % 820 = 1

phi(913) = (82)*(10)


print(n)
'''
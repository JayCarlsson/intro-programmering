from Cryptodome.Util.number import inverse

m = 19

p = 3
q = 17
n = (p * q)
phi = (p - 1) * (q - 1)

e = 65537
d = inverse(e, phi)
print(d)
c = pow(m, e, n)

print(f"The encrypted message is- {c}")

m = pow(c, d, n)

print(f"The decrypted message is- {m}")

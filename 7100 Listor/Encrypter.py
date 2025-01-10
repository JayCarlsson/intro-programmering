text = input("Type something and I'll encrypt it: ")
text = text.lower()

cstep = int(input("Hur många steg ska det enkrypteras? "))
cstep = cstep % 26

crypt = []

for bokstav in text:
    if bokstav == " ":
        crypt.append(bokstav)
    else:
        tal = ord(bokstav)
        if cstep < 0:
            cstep = cstep * -1
        tal += cstep
        while tal > 122:
            tal = tal - 26
        ny_bokstav = chr(tal)
        crypt.append(ny_bokstav)

delimiter = ""
encrypted = delimiter.join(crypt)
print(encrypted)
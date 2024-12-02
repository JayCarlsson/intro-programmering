text = input("Type something encrypted and I'll decrypt it! ")
text = text.lower()

cstep = int(input("Hur många ska jag dekryptera? "))

crypt = []

for bokstav in text:
    if bokstav == " ":
        crypt.append(bokstav)
    else:
        tal = ord(bokstav)
        if cstep < 0:
            cstep = cstep * -1
        tal -= cstep
        while tal < 97:
            tal = tal + 26
        ny_bokstav = chr(tal)
        crypt.append(ny_bokstav)

delimiter = ""
decrypted = delimiter.join(crypt)
print(decrypted)
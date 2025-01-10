text = input("Type something encrypted and I'll decrypt it! ")
text = text.lower()

crypt = []
i = 0

while i < 26:
    crypt.append(str(i))
    for bokstav in text:
        if bokstav == " ":
            crypt.append(bokstav)
        else:
            tal = ord(bokstav)
            tal -= i
            if tal < 97:
                tal += 26
            ny_bokstav = chr(tal)
            crypt.append(ny_bokstav)
    crypt.append("\n")
    i += 1

delimiter = ""
decrypted = delimiter.join(crypt)
print(decrypted)
print(i)
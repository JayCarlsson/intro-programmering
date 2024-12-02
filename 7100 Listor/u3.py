text = (input("Skriv något så översätter jag det till rövar språk: "))

i = len(text)
svar = []
konsonant = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "z"]


for bokstav in text.lower():
    count = konsonant.count(bokstav)
    if count > 0:
        svar.append(bokstav)
        svar.append("o")
        svar.append(bokstav)
    else:
        svar.append(bokstav)

delimiter = ""
join_str = delimiter.join(svar)
print(text, "blir", join_str, "på rövarspråk!")
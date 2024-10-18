tal = int(input("Skriv ett tal, vad som helst! "))

if tal >= 0 and tal <= 9:
    print(tal, "är ett ensiffrigt tal!")
elif tal >= 10 and tal <= 99:
    print(tal, "är ett tvåsiffrigt tal!")
elif tal >= 100 and tal <= 999:
    print(tal, "är ett tresiffrigt tal!")
elif tal >= 1000:
    print(tal, "är fyrsiffrigt eller större!")
else:
    print(tal, "är ett negativt tal")
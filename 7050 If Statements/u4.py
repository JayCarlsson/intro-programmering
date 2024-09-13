text = input("Skriv ett tal: ")
num = int(text)

if num >= 0 and num <= 9:
    print(num, "är ett ensiffrigt tal")
elif num >= 10 and num <= 99:
    print(num, "är ett tvåsiffrigt tal")
elif num >= 100 and num <= 999:
    print(num, "är ett tresiffrigt tal")
elif num >= 1000:
    print(num, "är ett fyrsiffrigt tal eller större")
elif num < 0:
    print(num, "är ett negativt tal")
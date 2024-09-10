text = input("Skriv den näst sista siffran i ditt personnummer ")
num = int(text)

if num % 2 != 0:
    print("Du är en kille")
elif num % 2 == 0:
    print("Du är en tjej")
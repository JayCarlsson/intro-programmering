text = input("Skriv ett tal")
num = int(text)

if num <= 0:
    print(num, "är negativt")
elif num > 0:
    print(num, "är positivt")
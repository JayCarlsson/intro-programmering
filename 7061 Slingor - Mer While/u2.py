guess = int(input("Gissa vilket tal jag tänker på mellan 1 och 100: "))
num = 42
i = 1

while guess != num:
    if guess < num:
        guess = int(input("För litet "))
    elif guess > num:
        guess = int(input("För stort "))
    i = i + 1
print("Det tog dig", i, "gissningar att hitta rätt svar")
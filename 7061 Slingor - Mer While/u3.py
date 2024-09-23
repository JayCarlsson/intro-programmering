guess = int(input("Gissa vilket tal jag tänker på mellan 1 och 100, du får bara 3 gissningar: "))
num = 42
i = 1

while i < 3:
    while guess != num:
        if i == 3:
            print("Du har använt dina 3 gissningar!")
            break
        if guess < num:
            guess = int(input("För litet "))
        elif guess > num:
            guess = int(input("För stort "))
        i = i + 1

if guess == num:
    print("Det tog dig", i, "gissningar att hitta rätt svar")
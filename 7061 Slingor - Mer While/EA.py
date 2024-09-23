num = int(input("Skriv ett tal så berättar jag om det är ett primtal "))

if num > 1:
    for i in range(2, (num//2)+1):
        if (num % i) == 0:
            print(num, "är inte ett primtal")
            break
    else:
        print(num, "är ett primtal")
else:
    print(num, "är inte ett primtal")

text = input("Skriv ett tal ")
text2 = input("Skriv ett till tal ")
num = int(text)
num2 = int(text2)

if num > num2:
    print(num, "är större än ", num2)
elif num2 > num:
    print(num2, "är större än ", num)
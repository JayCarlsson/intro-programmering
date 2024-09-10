import time
text = input("Ange ett heltal: ")
num = int(text)
time.sleep(2)

if num % 2 == 0:
    print("Talet är jämnt")
else:
    print("Talet är inte jämnt"), exit()

time.sleep(2)
text2 = input("Gissa min favoritfrukt: ")
frukt = str(text2)

time.sleep(2)
if frukt == ("Banan"):
    print("Du gissa rätt, min favoritfrukt är banan!")
elif frukt == ("Äpple"):
    print("Inte riktigt rätt, äpplen är andra plats!")
else:
    print(frukt, "är tyvärr inte min favorit!")
import time
text = input("Ange ett heltal: ")
num = int(text)
if num % 2 == 0:
    time.sleep(2)
    print("Talet är jämnt")
else:
    print("Talet är inte jämnt"), exit()
time.sleep(2)
text2 = input("Gissa min favoritfrukt: ")
frukt = str(text2)

if frukt == ("Banan"):
    time.sleep(2)
    print("Du gissa rätt, min favoritfrukt är banan!")
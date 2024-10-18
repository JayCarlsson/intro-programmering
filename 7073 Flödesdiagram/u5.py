tal = int(input("Skriv ett tal mellan 1-10! "))

while tal != 5:
    print("Du gissade fel!")
    tal = int(input("Gissa igen! "))
if tal == 5:
    print("Du gissade rätt!")
else:
    print("Något gick fel!")
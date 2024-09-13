text1 = input("Skriv ett tal: ")
text2 = input("Skriv ett till tal: ")
text3 = input("Skriv ytterligare ett tal: ")
tal1 = int(text1)
tal2 = int(text2)
tal3 = int(text3)

if tal1 < tal2 and tal1 < tal3:
    print(tal1, "är minst")
elif tal2 < tal1 and tal2 < tal3:
    print(tal2, "är minst")
elif tal3 < tal2 and tal3 < tal1:
    print(tal3, "är minst")

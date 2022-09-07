nr1 = int(input("sayı 1 :"))
nr2 = int(input("sayı 2 :"))
nr3 = int(input("sayı 3 :"))

if nr1>nr2:
    biggestNr = nr1
else:
    biggestNr = nr2
    
if nr3>biggestNr:
    biggestNr = nr3 

print("Biggest number is :" , biggestNr) #Or just print("Biggest number is :", max(nr1 , nr2, nr3))
                                         #max() function

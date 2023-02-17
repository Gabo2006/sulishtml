print("1. feladat")
szoveg=input("Kérek egy szöveget: ")

szam=""
while szam == "":
    try:
        szam=int(input("kerek egy egész szamot: "))
    except:
        print("ez nem egesz szam!")

try:
    print(szoveg[szam-1]*szam)
except:
    print("sajnos nincs ilyen betu! ")

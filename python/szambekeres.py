#szambekero modul
#többfele paraméterezéssel
#2022.11.18 egy BMW-s paraszt



def szambe(szoveg,tort=False,minimum=False,maximum=False):
#    print(szoveg)
#    print(tort)
#    print(minimum)
    hiba=True
    while hiba:
        try:
            if tort:
                szam=float(input(szoveg))
            else:
                szam=int(input(szoveg))
        except:
            print("Valami nem jo gec")
        else:
            hiba=False

szambe("Aggyá meg számót: ",minimum=10,tort=True)


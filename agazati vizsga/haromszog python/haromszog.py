def haromszog():
    
    vissza=[]
    for i in range(3):
        szam=""
        while szam == "":
            try:
                szam=int(input("kerek egy egész szamot: "))
            except:
                print("ez nem egesz szam!")
        vissza.append(szam)


    return vissza

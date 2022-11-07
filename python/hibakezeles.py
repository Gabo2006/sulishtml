

lista=["bence","laszlóóóó","ferii"]
lista.append("oszkar")
try:
    print(lista[3])
except:
    print("valami nem jo dik")
else:
    print("Sikeresen ügyes vagy more")

finally:
    print("ez tökéletes")

szam=""
while szam=="":
    try:
        szam=int(input("dobj egy szamot dik: "))
    except ValueError: 
        print("ez nem szam dik")
    except:
        print("nemtejjesen ismert hiba")

print(szam)

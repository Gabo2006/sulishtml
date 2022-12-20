import random
import math


#bekér 3 szám az első szám jelentse azt hogy mettől kell generálni a második azt hogy meddig a harmadik pedig hogy hány darabot.

minimumertek=int(input("Add meg hogy hol kezdődjön: "))
maximumertek=int(input("Add meg hol legyen a vege: "))
hanydarab=int(input("Add meg mennyi legyen: "))

lista=[]

for i in range(hanydarab):
    lista.append(random.randint(minimumertek, maximumertek))

print(lista)

legnagyobb=max(lista)
egyseg=80//legnagyobb

for e in lista:
    print("*"*(e*egyseg))


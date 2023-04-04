f=open("felfedezesek.csv")
elemek=[]

for e in f:
    elemek.append(e.replace("\n","").split(";"))
   

f.close()

elemek.pop(0)

print(elemek)

print("Elemek szama:{}".format(len(elemek)))

okor=[e for e in elemek if e[0]=="Ókor"]
print("Ókori elemek szama:{}".format(len(okor)))


while True:
    vegyjel = input('5. feladat: Kérek egy vegyjelet: ')
    if (0 < len(vegyjel) <3) and vegyjel.isalpha():
        vegyjel = vegyjel.upper()
        break

keresett=[e for e in elemek if e[2].lower()==vegyjel]
if keresett == []:
    print("nincs ilyen")
else:
    print()

#print(keresett)
 

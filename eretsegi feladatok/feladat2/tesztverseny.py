def pontSzamit(valasz,helyes):
    pont=0
    for sorszam,betu in enumerate(valasz):
          if betu==helyes[sorszam]:
               if sorszam<=5:
                    pont+=3
               elif sorszam<10:
                    pont+=4
               elif sorszam<14:
                   pont+=5
               else:
                   pont+=6
    return pont                
            
          


#1 feladat
f=open("valaszok.txt","r")

adatok=f.read().split("\n")
adatok.remove("")




f.close()

#print(adatok)


helyes=adatok[0]
adatok.remove(helyes)

valaszok=[]
for e in adatok:
     valaszok.append(e.split(" "))
   
    

#print(valaszok)

print("2. feladat: A vetélkedőn "+str(len(valaszok))+" versenyző indult.")






versenyzo=input("3. feladat: A versenyző azonosítója = ")


versenyzoValasza=""



for e in valaszok:
     if e[0]==versenyzo:
         print(e[1]+"\t (a versenyző válasza)")
         versenyzoValasza=e[1]



print("4. feladat")
print(helyes+"\t(a helyes megoldás)")
print(versenyzoValasza)


for sorszam,betu in enumerate(versenyzoValasza):
     #print(betu,str(sorszam))
     if betu==helyes[sorszam]:
          print("+",end="")
     else:
           print(" ",end="")
           
print("\t(a versenyzo helyes valaszai)")

feladat = int(input("5. feladat: A feladat sorszáma"))


db=0
for e in versenyzoValasza:
     if e[1][feladat]==helyes [feladat]:
          db+=1


print("A feladatra {} fő, a versenyzők {1:.2%}-a adott helyes választ.".format(db, db/len(valaszok)))


f=open("pontok.txt","w")

eredmenyek=[]
for e in valaszok:
     pont=pontSzamit(e[1],helyes)
     f.write(e[0]+" "+str(pont)+"\n")
     eredmenyek.append([e[0],pont])
f.close()


#eredmenyek.sort()
#print(eredmenyek[:10])


csakPontok=set()
for e in eredmenyek:
    csakPontok.add(e[1])

print(list(csakPontok)[-3:])











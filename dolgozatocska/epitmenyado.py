#1. feladat
adatok=[]
f=open("utca.txt","r")
for sor in f:
    temp=sor.replace("\n","").split(";")
    adatok.append(temp)
    
#print(adatok)

  

f.close()
adatok.pop(0)

#2.feladat
print("A mintában {} telek szerepel".format(len(adatok)))

#3.feladat
adoszam= "68396"
for adoszam in adatok:
        try:
            int(input("Egy tulajdonos adószáma: "))
        except:
            print("nem szerepel az állományban! ")


#4 feladat
#def ado :

    


     
        
    

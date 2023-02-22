#2 feladat
adatok=[]
f=open("hivas.txt","r")
for sor in f:
    temp=sor.replace("\n","").split(";")
    adatok.append(temp)
    
print(adatok)

  

f.close()
adatok.pop(0)



def ido2mp():
    
#1. feladat
eredmenyek=[]

f=open("triatlon.txt","r")
for egySor in f:
    temp=egySor.replace("\n","").split(";")
    eredmenyek.append(temp)
    

f.close()
eredmenyek.pop(0)

#2. feladat
print("A versemyen {} versenyző indult".format(len(eredmenyek)))


#3.feladat
print("3. feladat")





class MyClass:
    x=5
    def megnovel(self,mennyivel=1):
        self.x+=mennyivel

#print(MyClass.x)

class kutya:
    nev,fajta,agresszivitás,kor,szin=["","",0,0,""]
    def __init__(self,nev,fajta,agresszivitás,kor,szin):
        self.nev=nev
        self.fajta=fajta
        self.agresszivitás=agresszivitás
        self.kor=kor
        self.szin=szin
    def ugat(self):
        print("vau")
    def koszon(self):
        print("Szia uram, {} helo".format(self.nev))
    def talalkozas(self,masik):
        if self.agresszivitás>5 or masik.agresszivitás>5:
            #támadás
            if self.agresszivitás>=masik.agresszivitás:
                print("megöllek kutya!")
            else:
                print("ne bánts báttyaa")
        else:
            if self.agresszivitás>=masik.agresszivitás:
                print("szevasz kutya!")
            else:
                print("szia báttyaa")
            
def __str__(self):
    return "{}, {} ({})".format(self.nev,self.fajta,slef.kor)

class kotorek(kutya):
    def koszon(self):
        print("{} a nevem, kutyaság a mindenem! ".format(self.nev))

    def __init__(self,nev,fajta,ag,kor,szin,szemszin):
        super().__init__(nev,fajta,ag,kor,szin)
        self.szemszin=szemszin


k1=kutya("Buksi","jugoszláv farkasölő",9,10,"fekete")
k2=kutya("Tobi","nemetjuhasz",100,4,"fekete")





k1.ugat()
k1.koszon()
k2.koszon()


k2.talalkozas(k1)
k1.talalkozas(k2)

kotor1=kotorek("Füles", "tacskó",10,4,"barna","zold")
kotor1.koszon()
k1.talalkozas(kotor1)
print(kotor1.szemszin)

print(k1.szemszin)

print(k1)
print(kotor1)



"""
p1 = MyClass()
print(p1.x)
p2 = MyClass()
p2.x=1
print(p2.x)

p1.megnovel()
p1.megnovel(10)
print(p1.x)
"""

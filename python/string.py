nev=input("kérek egy nevet: ")

print("A " + nev + " nevet írtad be.")

print("A {belsonev} nevet írtad be.".format(belsonev=nev))

if len(nev)<5:
    print("Jó rövid név.")
elif len(nev)>=10:
    print("very BIGGGG név.")

be="nemvégjel"    
szavak=[]
while be!="":
    be=input("írj be valamit bástya: ")
    szavak.append(be)

#szavak.remove("")
#szavak.pop(-1)
#szavak.pop(len(szavak)-1)
#szavak=szavak[:-1]
szavak=[x for x in szavak if x!=""]

print(szavak)    

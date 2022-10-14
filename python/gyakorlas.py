
beSzam=0

while beSzam<2 or beSzam>5:
    beSzam= int(input("Adj meg egy számot 2 és 5 között: "))

autok=[]
for i in range(0,beSzam):
    print(i)
    autok.append(input("Kérek a(z) " +str(i+1)+". autómárkát: "))

print(autok)    

szo="almafa"


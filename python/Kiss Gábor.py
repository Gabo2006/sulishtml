
#1. feladat: Kérj be 8 számot egy megfelelő adatszerkezetbe!

szam = 1
for szam in range(8):
    szam= int(input("kérek egy számot: "))
       
     
#2. feladat: A bekért számokat írasd ki egymás mellé!

#3. feladat: A bekért számokat írasd ki 4 oszlopba!

#4. feladat: Számold ki a bekért számok összegét!

#5. feladat: A mellékelt szöveget tárold el a programodban:
szoveg = ("Nulla quis mi augue. Nunc vel pretium lectus. Aenean laoreet ornare ornare. Ut vitae elit et sapien fringilla iaculis ac at felis. Aenean scelerisque, diam non pellentesque rhoncus, risus lorem porttitor leo, ac consectetur nisi massa vitae sem. Nulla tempus diam id bibendum lobortis. Vestibulum porta neque id risus cursus, eget sodales nunc fermentum. Nulla facilisi. Suspendisse egestas orci a luctus fringilla. Cras dapibus ipsum nisl, non dapibus ex fermentum vitae.")
print(szoveg)
#6. feladat: Kérj be egy betűt, és írd ki, hogy mennyiszer található meg az előbbi szövegben!
be=input("kerek egy betűt: ")
print("ennyiszer van az adott betű a szövegben:")
print(szoveg.count(be))




szam=[]
for i in range(8):
    szam.append(int(input("Kerek egy szamot: ")))
print(szam)
print(szam[0:4])

osszeg=sum(szam)
print(osszeg)
szoveg="Nulla quis mi augue. Nunc vel pretium lectus. Aenean laoreet ornare ornare. Ut vitae elit et sapien fringilla iaculis ac at felis. Aenean scelerisque, diam non pellentesque rhoncus, risus lorem porttitor leo, ac consectetur nisi massa vitae sem. Nulla tempus diam id bibendum lobortis. Vestibulum porta neque id risus cursus, eget sodales nunc fermentum. Nulla facilisi. Suspendisse egestas orci a luctus fringilla. Cras dapibus ipsum nisl, non dapibus ex fermentum vitae."

betu=[]
while betu!="end":
    betu=(input("Kerek egy betut: "))
    print(szoveg.count(betu))


print(szoveg[::-1])
szoveg.replace("orna","")
print(len(szoveg))


def fa():
    x = ""
    while x == "":
        x = input("adj meg egy karakter: ")
    fa = """ {x}
              {x}{x}{x}
             {x}{x}{x}{x}{x}
            {x}{x}{x}{x}{x}{x}{x}
              {x}{x}{x}
             {x}{x}{x}{x}{x}
            {x}{x}{x}{x}{x}{x}{x}
              {x}{x}{x}
             {x}{x}{x}{x}{x}
            {x}{x}{x}{x}{x}{x}{x}
               {x}
              {x}{x}{x}   
            """
    print(fa.format(x=x))
fa()

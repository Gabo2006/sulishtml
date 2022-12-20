szam=[]
for i in range(10):
    szam.append(int(input("Kerek egy szamot: ")))
print(szam)
print(szam[0:2])

atlag=sum(szam)/len(szam)
print(atlag)

szoveg="Integer eget pharetra magna. Nulla ex urna, congue ac tincidunt ut, interdum et metus. Phasellus nunc nunc, consectetur eu odio vitae, ullamcorper sagittis nisi. Ut quam tortor, tempus sit amet diam nec, auctor iaculis leo. Donec ut libero velit. Maecenas nisi magna, congue ut tortor quis, maximus maximus arcu. Mauris et commodo nibh. Fusce id est vehicula, consectetur mi et, molestie sapien."


betu=[]
while betu!="":
    betu=input("Kerek egy betut: ")
    szoveg=szoveg.replace(betu,betu.upper())
    print(szoveg)

print(szoveg[::-1])    
szoveg=szoveg.replace(".","").replace(",","")
print(szoveg)


import math

szam="12"
while len(szam) !=3:
    szam=input("kerek egy 3 jegyu szamot: ")

szam=int(szam)
if szam%12==0:
    print("oszthato")
print(szam)













#hf bekér egy szam és kiír egy print tényezős szorzata


szoveg="passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of  (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance"

print(len(szoveg.split(" ")))


szoveg2=szoveg.replace("i","I")
print(szoveg2)

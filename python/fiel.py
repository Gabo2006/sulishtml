f=open("proba.txt","w")
f.write("Hello")
f.write("\n")
f.write("word!")

f.close()


f=open("proba.txt","r")

szoveg=(f.read())

sorok=szoveg.split("\n")

print(sorok)

f.close()

f=open("proba.txt","r")
print(f.readline())
sorok = []
for sor in f:
    sorok.append(sor.replace("\n","").replace("\r",""))

print(sorok)
f.close()

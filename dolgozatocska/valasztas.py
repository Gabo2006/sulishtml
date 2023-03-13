szavazatok=[]
f = open('szavazatok.txt')
for sor in f:
    sor=sor.strip().split(",")
    print(sor)
        



f.close()

print("A helyhatósági választáson {} képviselőjelölt indult ".format(len(sor)))

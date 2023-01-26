import random
import math
f=open("fel.txt","w")
for i in  range(10):
    
    l=[]
    for i in range(1):
        l.append(random.randint(2003,2008))

    h=[]
    for i in range(1):
        h.append(random.randint(1,12))

    if h == 1 or 3 or 5 or 7 or 9 or 11:
        n=[]
        for i in range(1):
            n.append(random.randint(1,31))
    elif h == 2:
        n=[]
        for i in range(1):
            n.append(random.randint(1,28))
    else:
        n=[]
        for i in range(1):
            n.append(random.randint(1,30))
            
    f.write(str(l[0])+"."+str(h[0])+"."+str(n[0])+" "+"\n")
f.close()
f=open("fel.txt","r")
c=f.read()
print(c)
f.close()

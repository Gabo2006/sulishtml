import matplotlib.pyplot as plt


def fv(a,b,c):
    xPont=[]
    yPont=[]

    for x in range(-10,10):
        xPont.append(x)
        yPont.append(a*x**2 + b*x + c)

    return [xPont,yPont]

#többedfokú egyenlet
def fv2(*egyutthatok):
    osszeg=0

    for sorszam,i in enumerate (egyutthatok):
        osszeg+==i * x**(len(egyutthatok)-1-sorszam)
        print(i)
        
    
        
    



x=[1,10] 
y=[10,1]

#plt.plot(x,y)

#plt.show()




xPont=[]
yPont=[]

for x in range(-10,10):
    xPont.append(x)
    yPont.append(16*x**2 - 3 + 16)

plt.plot(xPont,yPont)


#y=16x2 - 3 +16

xPont=[]
yPont=[]

for x in range(-10,10):
    xPont.append(x)
    yPont.append(16*x**2 - 3+16)

plt.plot(xPont,yPont)


pontok=fv(1,1,1)
plt.plot(pontok[0],pontok[1])

#plt.show()

fv2(1,2,3,4,5)






    
    


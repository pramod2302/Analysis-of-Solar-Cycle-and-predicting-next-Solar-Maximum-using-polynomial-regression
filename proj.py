from matplotlib import pyplot as plt
import numpy as np


f= open("data.txt","r")
fl =f.readlines()
v1=[]
v2=[]
for x in fl:
    x1=x.split()
    v1.append(float(x1[2]))
    v2.append(float(x1[3]))
runavg=[]
runavg1=[]
peaks=[]
runavg.append(v2[0])
for x in range(len(v2)-1):
    if x>=1:
        runavg.append((v2[x-1]+v2[x]+v2[x+1])/3)


runavg1.append(runavg[0])
runavg1.append(runavg[1])
runavg1.append(runavg[2])
runavg1.append(runavg[3])
runavg1.append(runavg[4])
runavg1.append(runavg[5])
for x in range(len(runavg)-6):
    if x>=6:
        runavg1.append((runavg[x-6]+runavg[x-5]+runavg[x-4]+runavg[x-3]+runavg[x-2]+runavg[x-1]+runavg[x]+runavg[x+1]+runavg[x+2]+runavg[x+3]+runavg[x+4]+runavg[x+5]+runavg[x+6])/13)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
max=0
min=v2[0]
tmax=0
tmin=0
tmaxr=[]
tminr=[]
maxr=[]
minr=[]
i=0
j=0
for x in range(1,len(runavg1)-1):
    if x % 132 != 0:
        if max<runavg1[x]:
            max=runavg1[x]
            tmax=v1[x]
            j=x
        if min>runavg1[x]:
            min=runavg1[x]
            tmin=v1[x]

            i=x
    else:

        maxr.append(max)
        tmaxr.append(tmax)
        max = 0
        tmax=0
        tmin=0
        min = runavg1[x + 1]
        break




for x in range(i+1,len(runavg1)-1):

    if (x-i)%132==0:
        maxr.append(max)
        tmaxr.append(tmax)

        max = 0
        tmax=0
    else:
        if max<runavg1[x]:
            max=runavg1[x]
            tmax = v1[x]

for x in range(j+1, len(runavg1) - 1):
    if (x - j) % 132 == 0:
        minr.append(min)
        tminr.append(tmin)
        tmin = 0
        min = runavg1[x + 1]
    else:
        if min>runavg1[x]:
            min=runavg1[x]
            tmin = v1[x]
#--------------------------------------------------------------------------------------------------------------------------------------------
minr.append(min)
tminr.append(tmin)
maxr2=[]
minr2=[]
minmaxr=[]
smaxr=0
sminr=0
smaxr2=0
sminr2=0
sminmaxr=0

for x in range(len(maxr)):
    maxr2.append(maxr[x]*maxr[x])
    minr2.append(minr[x] * minr[x])
    minmaxr.append((minr[x]*maxr[x]))
    smaxr=smaxr+maxr[x]
    sminr = sminr + minr[x]
    smaxr2=smaxr2+maxr[x]*maxr[x]
    sminr2 = sminr2 + minr[x] * minr[x]
    sminmaxr=sminmaxr+ minr[x]*maxr[x]

a1=(len(minr)*sminmaxr - smaxr*sminr)/ (len(minr)*sminr2-sminr*sminr)
a0=(sminr2*smaxr-sminr*sminmaxr)/(len(minr)*sminr2 - sminr*sminr)

a24=a0+a1*minr[24]
print(minr[24])
print("Number of Sunspots in the next maxima : ",a24)
lr=[]
tra=[]
for x in range(len(minr)):
    lr.append(a0+a1*minr[x])
for x in range(len(tminr)-1):
    tra.append(tmaxr[x+1]-tminr[x])


coe=np.polyfit(maxr[1:25],tra,2)

p1 = np.poly1d(coe)


var=[]
for x in range(len(tra)):
    var.append(coe[0]*maxr[x+1]*maxr[x+1]+coe[1]*maxr[x+1]+coe[2])

nextt=coe[0]*a24*a24+coe[1]*a24+coe[2]


print("\nFrom quadratic regression Next maxima in : ",nextt)
print("Future Sunsopt maxima : ",tminr[24]+nextt)
n=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

coe=np.polyfit(maxr[1:25],tra,3)

var2=[]
for x in range(len(tra)):
    var2.append(coe[0]*maxr[x+1]*maxr[x+1]*maxr[x+1]+coe[1]*maxr[x+1]*maxr[x+1]+coe[2]*maxr[x+1]+coe[3])

nextt=coe[0]*a24**3+coe[1]*a24**2+coe[2]*a24+coe[3]
print("\nFrom cubic regression Next maxima in : ",nextt)
print("Future Sunsopt maxima : ",tminr[24]+nextt)


coe=np.polyfit(maxr[1:25],tra,4)

nextt=coe[0]*a24**4+coe[1]*a24**3+coe[2]*a24**2+coe[3]*a24+coe[4]
print("\nFrom fourth order regression Next maxima in : ",nextt)
print("Future Sunsopt maxima : ",tminr[24]+nextt)

var3=[]
for x in range(len(tra)):
    var3.append(coe[0]*maxr[x+1]*maxr[x+1]*maxr[x+1]*maxr[x+1]+coe[1]*maxr[x+1]*maxr[x+1]*maxr[x+1]+coe[2]*maxr[x+1]*maxr[x+1]+coe[3]*maxr[x+1]+coe[4])

aa=maxr[1:25]





for x in range(len(aa)-1):
    for y in range(len(aa) - 1):
        if aa[y]>aa[y+1]:
            aa[y],aa[y+1]=aa[y+1],aa[y]
            var[y],var[y+1]=var[y+1],var[y]
            var2[y], var2[y + 1] = var2[y + 1], var2[y]
            var3[y], var3[y + 1] = var3[y + 1], var3[y]
            tra[y],tra[y+1]=tra[y+1],tra[y]

sumsq2=0
sumsq3=0
sumsq4=0
for x in range(len(tra)):
    sumsq2=sumsq2+ (tra[x]-var[x])**2
    sumsq3 = sumsq3 + (tra[x] - var2[x]) ** 2
    sumsq4 = sumsq4 + (tra[x] - var3[x]) ** 2



print("\nLeast square for quadratic : ",sumsq2,"\nLeast square for cubic : ",sumsq3,"\nLeast square for fourth order : ",sumsq4)


vv1 = v1[1:1000]
vv2= v2[1:1000]

plt.plot(vv1,vv2,color='gray')
plt.title("Data")
plt.xlabel("TIME in Years")
plt.ylabel("Number of Sunspots")
plt.plot(vv1,runavg1[1:1000],color='black')
plt.axis([1749.0,1800.0, 0.0, 300.0])
plt.show()
plt.plot(minr,lr,color='gray')
plt.title("Regression between Minimum number of sunspots vs Maximum number of Sunspots")
plt.xlabel("Minimum number of sunspots")
plt.ylabel("Maximum number of Sunspots")
plt.scatter(minr,maxr,color='black')
for i, txt in enumerate(n):
    plt.annotate(txt, (minr[i], maxr[i]))

plt.show()

n=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

plt.plot(aa,var,color='gray')
plt.title("2nd order Regression between Time taken from Solar minima to maxima vs Maximum number of Sunspots")
plt.xlabel("Maximum number of sunspots")
plt.ylabel("Time taken for the rise in number of sunspots")
plt.scatter(aa,tra)
for i, txt in enumerate(n):
    plt.annotate(txt, (aa[i], tra[i]))
plt.show()
plt.plot(aa,var2,color='gray')
plt.title("3rd order Regression between Time taken from Solar minima to maxima vs Maximum number of Sunspots")
plt.xlabel("Maximum number of sunspots")
plt.ylabel("Time taken for the rise in number of sunspots")
plt.scatter(aa,tra)
for i, txt in enumerate(n):
    plt.annotate(txt, (aa[i], tra[i]))
plt.show()
plt.plot(aa,var3,color='gray')
plt.title("4th order Regression between Time taken from Solar minima to maxima vs Maximum number of Sunspots")
plt.xlabel("Maximum number of sunspots")
plt.ylabel("Time taken for the rise in number of sunspots")
plt.scatter(aa,tra)
for i, txt in enumerate(n):
    plt.annotate(txt, (aa[i], tra[i]))
plt.show()

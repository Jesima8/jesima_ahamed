jes=int(input())
fac=[]
for i in range(1,jes+1):
    if(jes%i==0):
        fac.append(i)
for i in fac:
    print(i,end=" ")

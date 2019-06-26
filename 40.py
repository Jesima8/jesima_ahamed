n1=int(input())
a1=1
b1=[]
b1.append(a1)
b1.append(a1)
for i in range(1,n1-1):
    a1=b1[i-1]+b1[i]
    b1.append(a1)
for i in range(n1-1):
    print(b1[i],end=' ')
print(b1[len(b1)-1])

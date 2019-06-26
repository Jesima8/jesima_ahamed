q,r =map(int,input().split())
for x in range(q + 1,r):
   if x > 1:
       for i in range(2,x):
           if (x% i) == 0:
               break
       else:
            print(x,end=" ")

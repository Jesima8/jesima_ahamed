jes=int(input())
total=0
while(jes>0):
    dig=jes%10
    total=total+dig
    jes=jes//10
print(total)

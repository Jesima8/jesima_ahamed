z=int(input())
e=len(str(z))
a=z
b=0 
while z>0:
  c=z%10
  z=z//10
  d=c**e
  b=b+d
if a==b: 
  print('yes')
else:
  print('no')

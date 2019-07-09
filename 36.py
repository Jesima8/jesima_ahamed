but1=input()
cntt2=0
for p3 in range(0,len(but1)):
    if(but1[p3].isdigit() or but1[p3].isalpha() or but1[p3]==' '):
        continue
    else:
        cntt2=cntt2+1
print(cntt2)

m=int(input("enter the number"))
i=0
a={}
while i<=m:
    a.update ({i:i*i})
    i+=1
print(a)
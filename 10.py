a="MISSISSIPPI"
i=0
x={}
for i in a:
    if i not in x:
        x[i]=1
    else:
        x[i]=x[i]+1
print(x)





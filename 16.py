a=["a",1,2.5,"b",2,6.5]
i=0
s=[]
while i<len(a):
    if type(a[i])!=str:
        s.append(a[i])
    i=i+1
print(s)
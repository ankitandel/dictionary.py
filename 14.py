dict = {

    'a':50, 

    'b':58,

    'c': 56,

    'd':40,

    'e':100, 

    'f':20

    }

c=[]
for i in dict.values():
    c.append (i)
print(c)
b=0
for i in range(3):
    for k in range (len(c)-i-1):
        if c[k]>c[k+1]:
            b=c[k]
            c[k]=c[k+1]
            c[k+1]=b
    print(b)
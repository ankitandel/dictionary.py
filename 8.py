dic=[

     {"first":"1"}, 

     {"second": "2"}, 

     {"third": "1"}, 

     {"four": "5"}, 

     {"five":"5"}, 

     {"six":"9"},

     {"seven":"7"}]

i=0
a={}
while i<len(dic):
     a.update(dic[i])
     i=i+1
# print(a)

c=[]
for z in a.values():
     if z not in c:
          c.append(z)
print(c)
     
     

    
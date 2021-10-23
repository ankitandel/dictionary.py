dict1={1:10,1:20}
dict2={3:30,4:40}
dict3={5:50,6:60}

a={}
for i in dict1,dict2,dict3:
    a.update(dict1)
    a.update(dict2)
    a.update(dict3)
print(a)   



dic={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
a={}
for i in range(len(dic)):
    max=0
    for value in dic:
        if max<dic[value]:
            max=dic[value]
            key=value
    a.update({key:max})
    dic.pop(key)
print(a)



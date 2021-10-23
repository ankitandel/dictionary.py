list={'item1':45.50,'item2':35,'item3':41.30,'item4':55,'item5':24}

a={}
for i in range(len(list)):
    max=0
    for value in list:
        if max<list[value]:
            max=list[value]
            key=value
    a.update({key:max})
    list.pop(key)
print(a)

 
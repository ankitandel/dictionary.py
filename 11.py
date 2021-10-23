dict =  {

   'Alex': ['subj1', 'subj2', 'subj3'], 

   'David': ['subj1', 'subj2']}

count=0
list=[]
for i in dict.values():
    list=list+i
print(list)
j=0
while j<len(list):
    count+=1
    j+=1
print("total",count)

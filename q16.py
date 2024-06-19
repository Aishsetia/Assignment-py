#Program to count frequency of each character in string

'''LOGIC-characters of string are put as elements in list.A for loop is run
traversing through the list if the element is already added in the dictionary
created its occurence is counted otherwise it occurs only once.'''

string=str(input("enter a string"))
count=0
l=[]
l=string
d={}
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
        

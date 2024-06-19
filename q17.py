#Program in python that converts a given string to title case

string=str(input("enter a string"))
l=[]
l1=[]
l=string.split()
for i in range(len(l)):
    l=l[i][0].upper()
    l1.append(l[i])
print(str(l1))
